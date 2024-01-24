from flask import Flask, render_template, request, jsonify
import instaloader
from textblob import TextBlob

app = Flask(__name__)

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/profile_user', methods=['POST'])
def profile_user():
    username_to_analyze = request.form['username']

    try:
        # Fetch user profile information
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username_to_analyze)

        # Fetch user posts
        user_posts = [post.caption for post in profile.get_posts() if post.caption is not None]

        # Check if the user has any non-empty posts
        if not user_posts:
            return jsonify({'error': 'No Posts'})

        # Profile user based on sentiment analysis
        risk_level = sum(analyze_sentiment(post) for post in user_posts) / len(user_posts)

        if risk_level >= 0.2:
            risk = "High Risk"
        elif -0.2 < risk_level < 0.2:
            risk = "Medium Risk"
        else:
            risk = "Low Risk"

        return jsonify({'username': username_to_analyze, 'risk': risk})

    except instaloader.exceptions.ProfileNotExistsException as e:
        return jsonify({'error': f"Error: {e}"})

if __name__ == "__main__":
    app.run(debug=True)
