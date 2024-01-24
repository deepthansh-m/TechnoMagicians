import streamlit as st
from textblob import TextBlob
import instaloader

def analyze_sentiment(text):
    analysis = TextBlob(text)
    return analysis.sentiment.polarity

def profile_user(username):
    try:
        loader = instaloader.Instaloader()
        profile = instaloader.Profile.from_username(loader.context, username)

        user_posts = [post.caption for post in profile.get_posts() if post.caption is not None]

        total_posts = profile.mediacount
        followers = profile.followers
        following = profile.followees
        
        if not user_posts:
            return "No Posts with Caption", 0, total_posts, followers, following
        
        sentiments = [analyze_sentiment(post) for post in user_posts]
        average_sentiment = sum(sentiments) / len(sentiments)
        risk = average_sentiment * 100

        if risk >= 20:
            return "High Risk", risk, total_posts, followers, following
        elif -20 < risk < 20:
            return "Medium Risk", risk, total_posts, followers, following
        else:
            return "Low Risk", risk, total_posts, followers, following

    except instaloader.exceptions.ProfileNotExistsException as e:
        return f"Error: {e}", 0, 0, 0, 0

def main():
    st.title("Instagram Profile Analyzer")

    # Get input from the user
    username_to_analyze = st.text_input("Enter Instagram Username:")

    if st.button("Analyze"):
        # Profile the user and display the results
        risk_level, risk_percentage, total_posts, followers, following = profile_user(username_to_analyze)

        st.write(f"User: {username_to_analyze}")
        st.write(f"Risk Level: {risk_level}")
        st.write(f"Risk Percentage: {risk_percentage:.2f}%")
        st.write(f"Total Posts: {total_posts}")
        st.write(f"Followers: {followers}")
        st.write(f"Following: {following}")

if __name__ == "__main__":
    main()
