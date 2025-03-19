import os
import openai
from sqlalchemy import or_
from app import db, Review  
from dotenv import load_dotenv

# Load OpenAI API Key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def analyze_reviews():
    print("✅ Inside analyze_reviews()") 

    # Fetch reviews that haven't been analyzed yet
    reviews = db.session.query(Review).filter(or_(Review.sentiment == None, Review.sentiment.is_(None))).all()

    print(f"✅ Found {len(reviews)} unprocessed reviews")  

    if not reviews:
        print("❌ No reviews to analyze!")
        return

    for review in reviews:
        print(f"🔎 Analyzing Review {review.id}: {review.text[:50]}...")  

        # ✅ Send Review to OpenAI API for Sentiment & Theme Extraction
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are an AI that performs sentiment analysis and extracts key themes from product reviews."},
                {"role": "user", "content": f"Analyze this review: '{review.text}'. Return the sentiment score (-1 to 1) and a list of key themes."}
            ]
        )

        # ✅ Parse OpenAI API Response
        analysis = response["choices"][0]["message"]["content"]
        print(f"🔍 AI Response: {analysis}")  # Debugging

        # ✅ Extract sentiment and themes from response
        try:
            analysis_data = eval(analysis)  # Convert string response to dictionary
            review.sentiment = analysis_data.get("sentiment", 0)
            review.themes = analysis_data.get("themes", ["General"])
        except Exception as e:
            print(f"⚠️ Error parsing AI response: {e}")
            review.sentiment = 0
            review.themes = ["General"]

    db.session.commit()
    print("✅ Review analysis completed and saved to DB")


