from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
from db import db 

load_dotenv()


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

class Review(db.Model):
    __tablename__ = 'review'  
    __table_args__ = {'extend_existing': True} 
    id = db.Column(db.Integer, primary_key=True)
    product_id = db.Column(db.String(50), nullable=False)
    text = db.Column(db.Text, nullable=False)
    sentiment = db.Column(db.Float)
    themes = db.Column(db.JSON)

    def __repr__(self):
        return f'<Review {self.id}>'

# ✅ API Routes
@app.route('/api/reviews', methods=['GET'])
def get_reviews():
    product_id = request.args.get('product_id') 
    if not product_id:
        return jsonify({'error': 'Missing product_id'}), 400

    reviews = Review.query.filter_by(product_id=product_id).all()
    return jsonify([{
        'id': review.id,
        'product_id': review.product_id,
        'text': review.text,
        'sentiment': review.sentiment,
        'themes': review.themes if isinstance(review.themes, list) else []
    } for review in reviews])


@app.route('/api/analyze', methods=['POST'])
def analyze():
    print("✅ Handling /api/analyze Request")
    from nlp_analyzer import analyze_reviews  

    with app.app_context():
        analyze_reviews()
    
    return jsonify({'message': 'Reviews analyzed successfully'}), 200

@app.route('/api/scrape', methods=['POST'])
def scrape():
    from scraper import scrape_reviews  
    data = request.get_json()
    product_id = data.get('product_id')
    url = data.get('url')

    if not product_id or not url:
        return jsonify({'error': 'Missing product_id or url'}), 400

    scrape_reviews(product_id, url)
    return jsonify({'message': 'Scraping complete'}), 200

@app.route('/api/themes', methods=['GET'])
def get_themes():
    reviews = Review.query.all()
    all_themes = [theme for review in reviews for theme in (review.themes or [])]
    theme_counts = {theme: all_themes.count(theme) for theme in set(all_themes)}
    sorted_themes = sorted(theme_counts.items(), key=lambda x: x[1], reverse=True)
    return jsonify(sorted_themes[:10])  

if __name__ == '__main__':
    print("✅ Running Flask on port 6061")
    
    with app.app_context():
        db.create_all()
        print("✅ Tables Created in Database")

    app.run(debug=True, host='0.0.0.0', port=6061)