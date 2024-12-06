import streamlit as st
import requests

# Define the NewsAPI key
API_KEY = "140579ed9ae44cbe92847633faab5000"  # Replace this with your actual NewsAPI key
BASE_URL = "https://newsapi.org/v2/everything"


def fetch_climate_news(query="climate change", language="en", page_size=5):
    """Fetches the latest climate-related news using NewsAPI."""
    params = {
        "q": query,
        "apiKey": API_KEY,
        "language": language,
        "pageSize": page_size,  # Limit the number of results
    }
    response = requests.get(BASE_URL, params=params)
    
    # Check if the response is successful
    if response.status_code == 200:
        return response.json()["articles"]
    else:
        st.error("Failed to retrieve news articles.")
        return []


def climate_news_page():
    """Displays the Climate News Aggregator page for GaiaGuard."""

    # --- Page Title ---
    st.title("🌍 Climate News")
    st.write("---")

    # --- Introduction ---
    st.subheader("Stay Updated on the Latest Climate News")
    st.write(
        """
        Read the latest news on climate change, global warming, sustainability, and environmental issues
        from top news outlets worldwide.
        """
    )

    # Fetch the latest climate news
    st.write("### Latest News on Climate Change")
    news_articles = fetch_climate_news()

    if not news_articles:
        st.info("No news articles found. Please try again later.")
    else:
        # Display the latest articles
        for article in news_articles:
            st.write(f"#### {article['title']}")
            st.write(f"**Source**: {article['source']['name']}")
            st.write(f"**Published on**: {article['publishedAt']}")
            st.write(f"{article['description']}")  # Article description (summary)
            st.write(f"[Read more]({article['url']})")  # Link to full article
            st.write("---")

    # --- Footer ---
    st.write("---")
    st.write("🔗 Stay informed, stay empowered. Follow the latest on **climate change**!")
