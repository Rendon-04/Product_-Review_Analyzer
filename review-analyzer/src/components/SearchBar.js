"use client"

function SearchBar({ onSearch }) {
  return (
    <div className="mb-4">
      <input
        type="text"
        placeholder="Search reviews..."
        onChange={(e) => onSearch(e.target.value)}
        className="border p-2 w-full rounded"
      />
    </div>
  )
}

export default SearchBar

