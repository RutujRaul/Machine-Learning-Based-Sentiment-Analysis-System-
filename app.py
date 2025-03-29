from flask import Flask, render_template, request, redirect, url_for
from textblob import TextBlob
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client["sentiment_analysis_db"]
users_collection = db["users"]

def get_user(username):
    return users_collection.find_one({"username": username})

def check_credentials(username, password):
    user = get_user(username)
    if user and "password" in user and user["password"]:
        return user["password"] == password  # Direct comparison (No Hashing)
    return False 

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if check_credentials(username, password):
            return redirect(url_for('analyze'))
        else:
            return "Invalid credentials, please try again."
    return render_template('login.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        text = request.form.get('review')
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity  # Ranges from -1 to 1

       
        positive = max(0, polarity) * 100
        negative = max(0, -polarity) * 100
        neutral = 100 - positive - negative

   
        if polarity > 0:
            label = "Positive"
        elif polarity == 0:
            label = "Neutral"
        else:
            label = "Negative"

        return render_template(
            'dashboard.html',
            label=label,
            positive=round(positive, 2),
            neutral=round(neutral, 2),
            negative=round(negative, 2)
        )
    return render_template('dashboard.html')

@app.route('/logout')
def logout():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
