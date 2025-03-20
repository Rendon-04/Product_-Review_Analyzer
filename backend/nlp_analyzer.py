import openai
import os
from sqlalchemy import or_
from app import db, Review  
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) 

def analyze_reviews():
    print("✅ Inside analyze_reviews()") 

    reviews = db.session.query(Review).filter(or_(Review.sentiment == None, Review.sentiment.is_(None))).all()

    print(f"✅ Found {len(reviews)} unprocessed reviews")  

    if not reviews:
        print("❌ No reviews to analyze!")
        return

    for review in reviews:
        print(f"🔎 Analyzing Review {review.id}: {review.text[:50]}...")  

        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You analyze product reviews for sentiment (-1 to 1) and extract key themes."},
                {"role": "user", "content": f"Analyze this review: '{review.text}'. Return a JSON object with 'sentiment' and 'themes'."}
            ]
        )

        analysis = response.choices[0].message.content
        print(f"🔍 AI Response: {analysis}")  

        try:
            analysis_data = eval(analysis) 
            review.sentiment = analysis_data.get("sentiment", 0)
            review.themes = analysis_data.get("themes", ["General"])
        except Exception as e:
            print(f"⚠️ Error parsing AI response: {e}")
            review.sentiment = 0
            review.themes = ["General"]

    db.session.commit()
    print("✅ Review analysis completed and saved to DB")
