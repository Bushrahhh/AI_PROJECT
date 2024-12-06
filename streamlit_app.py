import streamlit as st
from views.about import about_page
from views.chatbot import climate_chatbot_page  # Correct import
from views.carbon_calculator import carbon_calculator_page
from views.news_aggregator import climate_news_page  # Corrected import
from views.climate_tracker import climate_tracker_page


def main():
    # Sidebar Navigation
    st.sidebar.title("Navigation")
    selection = st.sidebar.radio(
        "Go to",
        [
            "About",
            "Climate Chatbot",
            "Carbon Footprint Calculator",
            "Climate News",  # Added in sidebar
            "Climate Change Tracker",
        ]
    )

    # Page routing
    if selection == "About":
        about_page()
    elif selection == "Climate Chatbot":
        climate_chatbot_page()  # Correct function call
    elif selection == "Carbon Footprint Calculator":
        carbon_calculator_page()
    elif selection == "Climate News":
        climate_news_page()  # Corrected function call
    elif selection == "Climate Change Tracker":
        climate_tracker_page()


if __name__ == "__main__":
    main()
