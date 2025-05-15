# 🚶 WalkTheTalk

**WalkTheTalk** is a Flask-based web app that connects with your Google Fit account to fetch your step count using OAuth2 authentication. This app demonstrates how to securely integrate with Google APIs and visualize personal health data.

---
## 📌 About the Project

I created **WalkTheTalk** with a simple idea in mind:  
> *Encourage people to use social media more mindfully—by tying every direct message (DM) they send to real-world movement.*

### 🎯 Inspiration  
In a world where it's easy to scroll endlessly or fire off dozens of DMs without thinking, I wanted to build something that gently nudges people to get moving first. The concept is simple but powerful: **1 step = 1 DM**. It’s a creative way to make physical activity a prerequisite for online engagement.

### 🛠️ How It Was Built  
- **Backend:** Python & Flask  
- **OAuth Integration:** Google OAuth2 for secure login  
- **Health Data:** Google Fit API to fetch real-time step counts  
- **Frontend:** HTML and custom CSS for a clean, mobile-friendly UI

### 📚 What I Learned  
- How to implement OAuth2 in a Flask web app  
- How to securely access and use the Google Fit API  
- How to design a lightweight UI that feels intuitive and motivating  
- The importance of HTTPS when using OAuth (and how to test around it during development)

### ⚠️ Challenges Faced  
- Setting up the OAuth2 flow securely in a local development environment  
- Handling `InsecureTransportError` without compromising security  
- Getting familiar with Google’s scope and permission system  
- Parsing and calculating step data from Google Fit’s detailed datasets

This project was a fun and practical way to mix tech with behavioral change. I hope it sparks ideas for others looking to connect physical health with digital habits.

## 📦 Features

- 🔐 Google OAuth2 Login
- 📊 Fetches step data from Google Fit
- 🌐 Beautiful responsive frontend with HTML/CSS
- 🧪 Local development with HTTP (secure bypass for OAuth)
- ✅ Easily extendable for more health data

---

## ⚙️ Prerequisites

- Python 3.10+
- A Google Cloud Project with OAuth credentials
- `client_secret.json` downloaded from Google Cloud Console

---

## 🛠️ Installation

1. **Clone the repository**

```bash
git clone https://github.com/yourusername/WalkTheTalk.git
cd WalkTheTalk
````

2. **Create a virtual environment and activate it**

```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Add `client_secret.json`**

Place your downloaded Google OAuth credentials file (`client_secret.json`) in the root project directory.

5. **Run the Flask app**

```bash
python app.py
```

---

## 🔐 Google Cloud Setup

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project
3. Enable the following APIs:

   * Google Fit REST API
   * OAuth 2.0 Client IDs
4. Add `http://localhost:5000/oauth2callback` as an authorized redirect URI
5. Download the `client_secret.json` and place it in the project root

---

## 🚧 Development Mode: HTTP & OAuth2

Since OAuth 2.0 requires HTTPS, you'll need this bypass for **local development**:

```python
# Add this at the top of your app.py
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
```

⚠️ Do **not** use this in production.

---

## 📁 Project Structure

```
WalkTheTalk/
│
├── app.py                # Main Flask application
├── templates/
│   └── index.html        # Frontend UI
├── static/
│   └── style.css         # Custom CSS styling
├── client_secret.json    # OAuth credentials (not included in repo)
├── requirements.txt      # Python dependencies
└── README.md             # This file
```

---

## 🌟 Future Improvements

* Add charts to visualize steps over time
* Track other Google Fit metrics (heart rate, calories)
* Deploy securely with HTTPS (e.g. Render, Heroku)

---

## 📝 License

MIT License © 2025 \[Hemen]

