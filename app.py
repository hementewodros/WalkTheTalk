from flask import Flask, redirect, url_for, request, session, jsonify, render_template, g
import requests
import os
import sqlite3
import time
from google_auth_oauthlib.flow import Flow
from google.oauth2.credentials import Credentials
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

app = Flask(__name__)
app.secret_key = 'your-secret-key'  # Replace with secure key

DATABASE = "steps.db"
CLIENT_SECRETS_FILE = "client_secret.json"
SCOPES = ["https://www.googleapis.com/auth/fitness.activity.read"]
REDIRECT_URI = "http://localhost:5000/oauth2callback"

# ---- DB Utils ----
def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def init_db():
    if not os.path.exists(DATABASE):
        with app.app_context():
            db = get_db()
            db.execute("CREATE TABLE steps (id INTEGER PRIMARY KEY, total INTEGER NOT NULL)")
            db.execute("INSERT INTO steps (total) VALUES (0)")
            db.commit()

def get_step_count():
    cur = get_db().execute("SELECT total FROM steps WHERE id = 1")
    return cur.fetchone()["total"]

def update_steps(amount):
    db = get_db()
    db.execute("UPDATE steps SET total = total + ? WHERE id = 1", (amount,))
    db.commit()

# ---- Routes ----

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/get_steps")
def get_steps():
    return jsonify(steps=get_step_count())

@app.route("/api/add_steps", methods=["POST"])
def add_steps():
    steps = int(request.json.get("steps", 0))
    update_steps(steps)
    return jsonify(success=True, steps=get_step_count())

@app.route("/api/send_step", methods=["POST"])
def send_step():
    current = get_step_count()
    if current > 0:
        update_steps(-1)
        return jsonify(success=True, steps=current - 1)
    return jsonify(success=False, message="No steps left", steps=current)

# ---- Google Fit OAuth ----

@app.route("/authorize")
def authorize():
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI)
    auth_url, _ = flow.authorization_url(prompt='consent')
    return redirect(auth_url)

@app.route("/oauth2callback")
def oauth2callback():
    flow = Flow.from_client_secrets_file(
        CLIENT_SECRETS_FILE,
        scopes=SCOPES,
        redirect_uri=REDIRECT_URI)
    flow.fetch_token(authorization_response=request.url)

    credentials = flow.credentials
    session['credentials'] = credentials_to_dict(credentials)
    return redirect(url_for('fetch_steps'))

def credentials_to_dict(credentials):
    return {
        'token': credentials.token,
        'refresh_token': credentials.refresh_token,
        'token_uri': credentials.token_uri,
        'client_id': credentials.client_id,
        'client_secret': credentials.client_secret,
        'scopes': credentials.scopes
    }

@app.route("/fetch_steps")
def fetch_steps():
    if 'credentials' not in session:
        return redirect("/authorize")

    creds = Credentials(**session['credentials'])

    # Use system time instead of external API
    end_time_ms = int(time.time()) * 1000
    start_time_ms = end_time_ms - (24 * 60 * 60 * 1000)

    data_source = "derived:com.google.step_count.delta:com.google.android.gms:estimated_steps"

    url = "https://www.googleapis.com/fitness/v1/users/me/dataset:aggregate"
    headers = {"Authorization": f"Bearer {creds.token}"}
    body = {
        "aggregateBy": [{"dataTypeName": "com.google.step_count.delta", "dataSourceId": data_source}],
        "bucketByTime": {"durationMillis": 86400000},
        "startTimeMillis": start_time_ms,
        "endTimeMillis": end_time_ms
    }

    res = requests.post(url, headers=headers, json=body)
    data = res.json()

    total_steps = 0
    try:
        for bucket in data["bucket"]:
            for dataset in bucket["dataset"]:
                for point in dataset["point"]:
                    total_steps += point["value"][0]["intVal"]
    except Exception:
        pass

    update_steps(total_steps)
    return f"Fetched and added {total_steps} steps from Google Fit!"

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
