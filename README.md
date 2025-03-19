# 📊 Product Review Analyzer

**Product Review Analyzer** is a full-stack web application that scrapes product reviews from Amazon, performs sentiment analysis, and identifies key themes using AI.
<img width="1728" alt="Screenshot 2025-03-19 at 4 00 57 PM" src="https://github.com/user-attachments/assets/6cf6e6c2-2974-439e-b7f8-70c9fd2d4184" />
<img width="1728" alt="Screenshot 2025-03-19 at 4 01 27 PM" src="https://github.com/user-attachments/assets/a74693f0-5524-4d08-8640-0656cb6d99b7" />

## 🚀 Features

- **Scrape Amazon Reviews**: Extracts customer reviews directly from Amazon product pages.
- **Analyze Sentiment**: Uses AI-powered sentiment analysis to categorize reviews as positive, neutral, or negative.
- **Identify Key Themes**: Extracts relevant topics and trends from customer feedback.
- **Interactive Dashboard**: Displays insights using charts and tables for easy review.

## 🛠️ Tech Stack

- **Backend**: Flask, PostgreSQL, SQLAlchemy, BeautifulSoup, OpenAI API
- **Frontend**: React, Chart.js, Axios, Bootstrap

## 🔧 Setup Instructions

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/product-review-analyzer.git
   cd product-review-analyzer
   ```

2. **Setup the Backend**
   - Install dependencies:
     ```bash
     cd backend
     python -m venv env
     source env/bin/activate  # On Windows use `env\Scripts\activate`
     pip install -r requirements.txt
     ```
   - Set environment variables in a `.env` file:
     ```
     DATABASE_URL=postgresql+psycopg2://your_user:your_password@localhost:5432/product_reviews
     OPENAI_API_KEY=your_api_key
     ```
   - Run the Flask server:
     ```bash
     flask run --port=6061
     ```

3. **Setup the Frontend**
   - Install dependencies:
     ```bash
     cd frontend
     npm install
     ```
   - Start the React application:
     ```bash
     npm start
     ```

4. **Run Scraper & Analysis**
   - Scrape reviews:
     ```bash
     curl -X POST http://localhost:6061/api/scrape -H "Content-Type: application/json" -d '{"product_id": "B0BLSQ7J4B", "url": "https://www.amazon.com/your-product-url"}'
     ```
   - Analyze reviews:
     ```bash
     curl -X POST http://localhost:6061/api/analyze
     ```

## 📈 Future Enhancements
- Implement real-time AI-powered review analysis
- Expand to multiple e-commerce platforms
- Improve UI with more visual insights

---

**👨‍💻 Built by Ivan Rendon**  
*Making AI-powered insights accessible for product analysis*  


