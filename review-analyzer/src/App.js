"use client"

import { useState, useEffect } from "react"
import axios from "axios"
import FilterBar from "./components/FilterBar"
import SearchBar from "./components/SearchBar"
import ReviewList from "./components/ReviewList"
import ThemeChart from "./components/ThemeChart"

function App() {
  const [reviews, setReviews] = useState([])
  const [filteredReviews, setFilteredReviews] = useState([])
  const [themes, setThemes] = useState([])
  const [productId, setProductId] = useState("")
  const [url, setUrl] = useState("")
  const [sentimentFilter, setSentimentFilter] = useState("all")
  const [themeFilter, setThemeFilter] = useState("all")
  const [searchTerm, setSearchTerm] = useState("")

  useEffect(() => {
    fetchReviews()
    fetchThemes()
  }, [])

  useEffect(() => {
    filterReviews()
  }, [reviews, sentimentFilter, themeFilter, searchTerm])

  const fetchReviews = async () => {
    const response = await axios.get("http://localhost:6061/api/reviews")
    setReviews(response.data)
  }

  const fetchThemes = async () => {
    const response = await axios.get("http://localhost:6061/api/themes")
    setThemes(response.data)
  }

  const handleScrape = async () => {
    await axios.post("http://localhost:6061/api/scrape", { product_id: productId, url })
    fetchReviews()
  }

  const handleAnalyze = async () => {
    try {
      await axios.post("http://localhost:6061/api/analyze", {}, {
        headers: {
          "Content-Type": "application/json"
        },
        withCredentials: false
      });
      console.log("Analysis completed");
    } catch (error) {
      console.error("Error analyzing reviews:", error);
    }
  };
  

  const filterReviews = () => {
    let filtered = reviews

    if (sentimentFilter !== "all") {
      filtered = filtered.filter((review) => {
        if (sentimentFilter === "positive") return review.sentiment > 0.2;
        if (sentimentFilter === "negative") return review.sentiment < -0.2;
        return review.sentiment >= -0.2 && review.sentiment <= 0.2;
      });
    }
    

    if (themeFilter !== "all") {
      filtered = filtered.filter((review) => review.themes?.includes(themeFilter))
    }

    if (searchTerm) {
      filtered = filtered.filter((review) => review.text.toLowerCase().includes(searchTerm.toLowerCase()))
    }

    setFilteredReviews(filtered)
  }

  return (
    <div className="container mx-auto p-4">
      <h1 className="text-3xl font-bold mb-4">Product Review Analyzer</h1>

      <div className="mb-4 flex space-x-2">
        <input
          type="text"
          placeholder="Product ID"
          value={productId}
          onChange={(e) => setProductId(e.target.value)}
          className="border p-2 flex-grow"
        />
        <input
          type="text"
          placeholder="URL"
          value={url}
          onChange={(e) => setUrl(e.target.value)}
          className="border p-2 flex-grow"
        />
        <button onClick={handleScrape} className="bg-blue-500 text-white p-2 rounded">
          Scrape Reviews
        </button>
        <button onClick={handleAnalyze} className="bg-green-500 text-white p-2 rounded">
          Analyze Reviews
        </button>
      </div>

      <div className="mb-4">
        <ThemeChart themes={themes} />
      </div>

      <FilterBar themes={themes} onSentimentChange={setSentimentFilter} onThemeChange={setThemeFilter} />

      <SearchBar onSearch={setSearchTerm} />

      <ReviewList reviews={filteredReviews} />
    </div>
  )
}

export default App

