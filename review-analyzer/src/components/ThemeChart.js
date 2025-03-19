import { Bar } from "react-chartjs-2"
import { Chart as ChartJS, CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend } from "chart.js"

ChartJS.register(CategoryScale, LinearScale, BarElement, Title, Tooltip, Legend)

function ThemeChart({ themes }) {
  const chartData = {
    labels: themes.map((theme) => theme[0]),
    datasets: [
      {
        label: "Theme Frequency",
        data: themes.map((theme) => theme[1]),
        backgroundColor: "rgba(75, 192, 192, 0.6)",
      },
    ],
  }

  const options = {
    responsive: true,
    plugins: {
      legend: {
        position: "top",
      },
      title: {
        display: true,
        text: "Top Themes",
      },
    },
  }

  return <Bar data={chartData} options={options} />
}

export default ThemeChart

