"use client"

function FilterBar({ themes, onSentimentChange, onThemeChange }) {
  return (
    <div className="flex space-x-4 mb-4">
      <select onChange={(e) => onSentimentChange(e.target.value)} className="border p-2 rounded">
        <option value="all">All Sentiments</option>
        <option value="positive">Positive</option>
        <option value="neutral">Neutral</option>
        <option value="negative">Negative</option>
      </select>
      <select onChange={(e) => onThemeChange(e.target.value)} className="border p-2 rounded">
        <option value="all">All Themes</option>
        {themes.map((theme) => (
          <option key={theme[0]} value={theme[0]}>
            {theme[0]}
          </option>
        ))}
      </select>
    </div>
  )
}

export default FilterBar

