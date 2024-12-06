import streamlit as st
from PIL import Image


def about_page():
    """Displays the About page for GaiaGuard."""
    
    # --- Page Title and Logo ---
    st.title("🌍 About GaiaGuard")
    st.write("---")  # A horizontal line for better structure

    # --- Intro Section ---
    st.subheader("Welcome to GaiaGuard!")
    st.write(
        """
        **GaiaGuard** is your one-stop platform for raising climate awareness and taking meaningful action.
        Our mission is to empower individuals and communities with tools, insights, and data to make informed decisions 
        about reducing their environmental impact and combating climate change.
        """
    )

    # --- Features Section ---
    st.subheader("🌟 What We Offer")
    features = {
        "🌿 Carbon Footprint Calculator": "Easily calculate your personal or organizational carbon footprint.",
        "🤖 Climate Chatbot": "Get answers to your climate-related questions instantly.",
        "📰 Climate News Aggregator": "Stay updated with the latest climate and environmental news.",
        "📊 Climate Change Tracker": "Track real-time data and trends on climate change globally.",
        "📚 Resources and Tips": "Learn actionable ways to reduce your carbon emissions and live sustainably."
    }
    for feature, description in features.items():
        st.write(f"{feature}\n- {description}")

    # --- Call-to-Action Section ---
    st.subheader("🚀 Join Us in Making a Difference!")
    st.write(
        """
        Climate change is the defining challenge of our time, but together, we can make a difference. 
        Join GaiaGuard in taking small, impactful actions every day to create a sustainable future for generations to come.
        """
    )
    
    st.write("💚 **Let’s protect our planet, one step at a time.**")

    # --- Footer Section with Contact Info ---
    st.write("---")
    st.subheader("📞 Contact Us")
    st.write(
        """
        Have questions, feedback, or suggestions? We'd love to hear from you!
        - **Email**: support@gaiaguard.com
        - **Website**: [www.gaiaguard.com](http://www.gaiaguard.com)
        - **Socials**: Follow us on [Twitter](http://twitter.com/gaiaguard) | [Instagram](http://instagram.com/gaiaguard)
        """
    )
