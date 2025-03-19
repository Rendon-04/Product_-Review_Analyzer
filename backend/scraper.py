import requests
from bs4 import BeautifulSoup
import time
import random

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

def scrape_reviews(product_id, url):
    from app import db, Review  
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    reviews = soup.find_all('div', {'data-hook': 'review'})

    print(f"✅ Found {len(reviews)} reviews")  # Debugging log

    for review in reviews:
        text_element = review.find('span', {'data-hook': 'review-body'})

        if text_element:
            text = text_element.text.strip()
            print(f"💾 Saving Review: {text[:50]}...")  # Debugging log
            new_review = Review(product_id=product_id, text=text)
            db.session.add(new_review)

    db.session.commit()
    print("✅ Reviews saved in the database!")
