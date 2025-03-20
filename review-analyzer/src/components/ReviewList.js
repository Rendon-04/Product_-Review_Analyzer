function ReviewList({ reviews }) {
    const getSentimentColor = (sentiment) => {
      if (sentiment > 0.5) return "text-green-600"
      if (sentiment < -0.5) return "text-red-600"
      return "text-yellow-600"
    }
  
    return (
      <div>
        <h2 className="text-2xl font-bold mb-2">Reviews</h2>
        <ul className="space-y-4">
          {reviews.map((review) => (
            <li key={review.id} className="border p-4 rounded shadow">
              <p className="mb-2">{review.text}</p>
              <p className={`text-sm ${getSentimentColor(review.sentiment)}`}>
                Sentiment: {review.sentiment?.toFixed(2)}
              </p>
              <p className="text-sm text-gray-600">
                Themes: {(Array.isArray(review.themes) ? review.themes : []).join(", ")}
              </p>
            </li>
          ))}
        </ul>
      </div>
    )
  }
  
  export default ReviewList


