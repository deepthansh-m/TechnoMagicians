import instaloader
from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def profile_user(username):
    try:
        # Fetch user profile information
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)

        # Fetch user posts
        user_posts = [post.caption for post in profile.get_posts() if post.caption is not None]

        # Check if the user has any non-empty posts
        if not user_posts:
            return "No Posts"

        # Profile user based on sentiment analysis
        risk_level = sum(analyze_sentiment(post) for post in user_posts) / len(user_posts)

        if risk_level >= 0.2:
            return "High Risk"
        elif -0.2 < risk_level < 0.2:
            return "Medium Risk"
        else:
            return "Low Risk"

    except instaloader.exceptions.ProfileNotExistsException as e:
        return f"Error: {e}"

if __name__ == "__main__":
    # Replace 'target_username' with the Instagram username you want to analyze
    username_to_analyze = 'sellydsouzaaa'

    # Profile the user and print the risk level
    risk_level = profile_user(username_to_analyze)
    print(f"User: {username_to_analyze}")
    print(f"Risk Level: {risk_level}")
