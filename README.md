# ⚽ Soccer Matches App

![Python](https://img.shields.io/badge/python-3.8+-blue)
![Flask](https://img.shields.io/badge/flask-2.0+-green)
![JavaScript](https://img.shields.io/badge/javascript-ES6+-yellow)

A web application that displays upcoming soccer matches using the [Football-Data.org API](https://www.football-data.org/).

![App Screenshot](./screenshot.png) *(Replace with actual screenshot)*

## ✨ Features

- 📅 View upcoming matches with date/time
- ⚽ See matchups between teams
- 🔄 Auto-refreshing data
- 🎨 Clean, responsive interface
- ⚡ Fast loading with async API calls

## 🛠️ Tech Stack

**Backend**:
- Python 3
- Flask (Micro web framework)
- Requests (HTTP library)

**Frontend**:
- Vanilla JavaScript
- CSS Grid/Flexbox
- Fetch API

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Git
- Football-Data.org API key (free tier available)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/RamCharan-88/Soccer-matches-app.git
   cd Soccer-matches-app


2. **Setup Backend**
    ```bash
    cd backend
    cp .env.example .env  # Create environment file

  **Edit .env and add your API key:**
  
    API_KEY=your_football_data_api_key


3. **Install dependencies**
    ```bash
    pip install -r requirements.txt

4. **Run the backend server**
    ```bash
    python app.py
 Server will run at http://localhost:5000
 
5. **Open frontend**
   
    *Open frontend/index.html in your browser
    *Or use a local server:

    ```bash
    python -m http.server 8000

  Then visit http://localhost:8000/frontend


  ### Project Structure

  Soccer-matches-app/
├── backend/
│   ├── app.py           # Flask application
│   ├── requirements.txt # Python dependencies
│   └── .env.example     # Environment template
├── frontend/
│   ├── index.html       # Main page
│   ├── styles.css       # Styling
│   └── script.js        # Frontend logic
└── README.md            # This file

  
 ### 🤝 Contributing

 Contributions are welcome! Please follow these steps:

1. Fork the project

2. Create your feature branch (git checkout -b feature/AmazingFeature)

3. Commit your changes (git commit -m 'Add some amazing feature')

4. Push to the branch (git push origin feature/AmazingFeature)

5. Open a Pull Request

 ### 📜 License

   Distributed under the MIT License. See LICENSE for more information.
    
   
