# 🪔 Pujo Parikrama 2026

**Pujo Parikrama 2026** is a web application designed to help visitors explore and navigate Durga Puja pandals during the festive season.

The application provides a simple way to discover selected pandals, get directions from the user's current location, explore routes from major starting points, and share reviews.

---

## ✨ Features

* 🏮 **Top Pandal List**
  Explore a curated list of popular Durga Puja pandals.

* 📍 **Pandal Navigation**
  Get directions to a selected pandal using the user's current location.

* 🗺️ **Route Options**
  Visitors coming from different directions can select an appropriate starting route and explore the listed pandals.

* 📱 **Responsive Design**
  Designed to work across both desktop and mobile screens.

* ⭐ **Pandal Reviews**
  Visitors can submit ratings and reviews for pandals.

* 📍 **Location Support**
  Uses browser geolocation to determine the visitor's current location when navigation is requested.

* 🪷 **Bengali-Inspired UI**
  The interface combines traditional Bengali festive elements with a clean modern web design.

* ⚡ **Fast Frontend**
  Built using Vue.js and Vite for a responsive user experience.

---

## 🛠️ Tech Stack

### Frontend

* Vue.js
* Vite
* HTML5
* CSS3
* JavaScript

### Backend

* Python
* Flask
* Flask-SQLAlchemy

### Database

* SQLite

### APIs / Services

* Browser Geolocation API
* Google Maps navigation links

---

## 📂 Project Structure

```text
Durgapujo-2026/
│
├── backend/
│   ├── app.py
│   ├── instance/
│   │   └── reviews.db
│   └── templates/
│       └── review.html
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── index.html
│   ├── package.json
│   ├── package-lock.json
│   └── vite.config.js
│
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

Make sure you have the following installed:

* Node.js
* npm
* Python 3
* Git

---

## 💻 Frontend Setup

Navigate to the frontend directory:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The Vue application will normally be available at:

```text
http://localhost:5173
```

---

## 🐍 Backend Setup

Open another terminal and navigate to the backend:

```bash
cd backend
```

Create a virtual environment:

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

Install the required Python packages:

```bash
pip install flask flask-sqlalchemy flask-cors
```

Run the Flask application:

```bash
python app.py
```

The backend will normally run at:

```text
http://localhost:5000
```

---

## 📍 How Navigation Works

When a visitor chooses to navigate to a pandal, the application can use the browser's current location as the starting point.

The selected destination is then opened through Google Maps, allowing the visitor to continue navigation using the Maps interface.

The application does **not** need to implement turn-by-turn navigation itself.

---

## ⭐ Review System

Pujo Parikrama includes a simple review system powered by Flask and SQLite.

Visitors can submit:

* Rating
* Review
* User information

The backend receives the submitted data and stores it in the SQLite database.

---

## 🔐 Privacy & Permissions

The application may request **location permission** when location-based navigation is used.

Location access is requested through the browser's Geolocation API and is subject to the user's browser permissions.

The application does not require continuous location tracking for basic browsing.

---

## 📱 Responsive Experience

Pujo Parikrama is designed for both:

* 📱 Mobile devices
* 💻 Desktop computers

The interface adapts to different screen sizes while maintaining the same core features and festive visual style.

---

## 🎨 Design

The visual design is inspired by the traditional atmosphere of Durga Puja, incorporating elements such as:

* Maa Durga imagery
* Bengali typography
* Alpona-inspired decorative elements
* Traditional festive colors
* Minimal and clean layouts

The goal is to combine **traditional festival aesthetics with a modern web experience**.

---

## 🔮 Future Improvements

Possible future enhancements include:

* More pandals and detailed information
* Pandal-wise photos
* Improved route planning
* Distance and estimated travel time
* Nearby facilities such as toilets and parking
* User authentication
* Improved review management
* Persistent production database
* Pandal search and filtering
* Festival schedule and event information

---

## 📌 Project Status

**Development / Demo Project**

Pujo Parikrama 2026 is being developed as a practical web application for exploring Durga Puja pandals and experimenting with modern frontend, backend, location, and database technologies.

---

## 👨‍💻 Author

**Jishnujit Mete**

---


