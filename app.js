/* ==========================================================================
   MK MOVIE TICKET BOOKING SYSTEM - FRONTEND APP (PYTHON FLASK REST API INTEGRATION)
   ========================================================================== */
let moviesData = [];
let showTimingsData = {};
let seatTypesData = {};
let currentSelectedMovie = null;
let currentShowChoice = "1";
let currentSeatChoice = "1";
let currentSeatCharge = 0;
let currentTicketCount = 1;
let bookingHistory = [];
// Initialize App & Fetch Movies from Python Backend
document.addEventListener("DOMContentLoaded", () => {
  fetchMoviesFromAPI();
  fetchBookingsFromAPI();
});
// Fetch Movies List from Flask API (`GET /api/movies`)
async function fetchMoviesFromAPI() {
  try {
    const res = await fetch("/api/movies");
    const data = await res.json();
    if (data.status === "success") {
      moviesData = data.movies;
      showTimingsData = data.show_timings;
      seatTypesData = data.seat_types;
      renderMoviesGrid();
    }
  } catch (err) {
    console.error("Failed to load movies from Python backend:", err);
  }
}