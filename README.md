# 🚶 WalkTheTalk

**WalkTheTalk** is a Flask-based web app that connects with your Google Fit account to fetch your step count using OAuth2 authentication. This app demonstrates how to securely integrate with Google APIs and visualize personal health data.

---

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

