🎬 MK Movie Ticket Booking System
A full-stack movie ticket booking web application built with Python Flask, SQLite Database, HTML5, Vanilla CSS (Glassmorphism Cinema Theme), and JavaScript.

🌟 Features
🍿 Now Showing Movies Grid: Browse trending movies with ratings, genre, duration, and poster artwork.
🕒 Showtime & Pricing Matrix: Select from 3 showtimes (Morning, Matinee, Night) with dynamic base pricing.
💺 Seat Category Selection & Visual Map: Choose between Silver (+₹0), Gold (+₹50), and Platinum (+₹100) categories with an interactive visual cinema seat map preview.
🧮 Live Price Calculation: Calculates ticket price per ticket and total amount in real-time matching the original Python script logic.
🎟️ Pass Ticket Generator: Generates an aesthetic digital ticket pass complete with Booking Reference ID (MK-XXXXXX), QR entry code, seat numbers, and instant print capability.
💾 SQLite Database Persistence: Stores all completed ticket bookings securely in a Python SQLite database (database.db).
❌ Booking Cancellation: View past booking records and cancel/delete any booking directly from the app.
🎬 Movies & Pricing Matrix
1. Bhoot Bangla (Horror / Comedy)
1: 09:00 - 11:40 (Morning Show) — ₹150
2: 14:00 - 16:40 (Matinee Show) — ₹210
3: 21:00 - 23:40 (Night Show) — ₹190
2. Spider-Man: Brand New Day (Action / Sci-Fi)
1: 09:00 - 11:40 (Morning Show) — ₹120
2: 14:00 - 16:40 (Matinee Show) — ₹180
3: 21:00 - 23:40 (Night Show) — ₹220
3. Musafir Cafe (Drama / Romance)
1: 09:00 - 11:40 (Morning Show) — ₹200
2: 14:00 - 16:40 (Matinee Show) — ₹200
3: 21:00 - 23:40 (Night Show) — ₹200
📐 Price Calculation Formula
Price per Ticket
=
Base Show Price
+
Seat Charge
Price per Ticket=Base Show Price+Seat Charge
Total Amount
=
Price per Ticket
×
Number of Tickets
Total Amount=Price per Ticket×Number of Tickets
Seat Surcharges:
1. Silver: +₹0
2. Gold: +₹50
3. Platinum: +₹100
📁 Project Structure

mk-movie-booking/
├── app.py                  # Python Flask backend server & REST APIs
├── database.db             # SQLite database storing bookings
├── README.md               # Project documentation
├── templates/
│   └── index.html          # Main HTML5 UI template
└── static/
    ├── style.css           # Glassmorphism cinema styling & animations
    └── app.js              # Frontend JavaScript communicating with Flask API
🚀 Quick Start Guide
Prerequisites
Make sure you have Python 3.8+ installed on your system.

1. Install Dependencies
bash

pip install flask
2. Run the Python Backend Server
Navigate to the project folder and run app.py:

bash

python app.py
3. Open in Browser
Open your browser and visit: 👉 http://localhost:5000

🔌 REST API Reference
Method	Endpoint	Description
GET	/	Renders main frontend web UI
GET	/api/movies	Returns list of movies, showtimes & seat prices
POST	/api/book	Creates a new booking & saves it to SQLite DB
GET	/api/bookings	Fetches all saved booking records from SQLite DB
DELETE	/api/bookings/<id>	Deletes/cancels a booking by Booking ID
📄 License
Created for MK Movie Ticket Booking System. Open source under MIT License.
