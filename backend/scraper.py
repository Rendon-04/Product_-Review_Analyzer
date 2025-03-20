import requests
from bs4 import BeautifulSoup


HEADERS = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9",
}

def scrape_reviews(product_id, url):
    from app import db, Review

    print(f"✅ Scraping {url} for product {product_id}...")

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    reviews = soup.find_all('span', {'data-hook': 'review-body'})

    if not reviews:
        print("❌ No reviews found! Check Amazon page structure.")
        return

    for review in reviews:
        review_text = review.text.strip()
        print(f"📝 Scraped Review: {review_text}") 

        new_review = Review(product_id=product_id, text=review_text)
        db.session.add(new_review)

    db.session.commit()
    print(f"✅ Successfully saved {len(reviews)} reviews to database")

