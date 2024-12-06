import streamlit as st


# Predefined responses (simple rule-based for demo purposes)
def get_climate_answer(user_input):
    """Returns a response based on user input."""
    
    responses = {
        "What is climate change?": "Climate change refers to long-term changes in temperature, precipitation, and other atmospheric conditions on Earth.",
        "How can I reduce my carbon footprint?": "You can reduce your carbon footprint by using public transport, switching to renewable energy, reducing meat consumption, and recycling.",
        "What is global warming?": "Global warming refers to the long-term increase in Earth's average temperature due to human activities, mainly burning fossil fuels.",
        "How does deforestation affect climate change?": "Deforestation contributes to climate change by reducing the number of trees that can absorb CO2 from the atmosphere.",
        "What is the Paris Agreement?": "The Paris Agreement is an international treaty aiming to limit global warming to below 2°C compared to pre-industrial levels."
    }

    return responses.get(user_input, "I'm sorry, I don't have an answer for that. Can I help with something else?")


# The correct function name for chatbot page
def climate_chatbot_page():
    """Displays the Climate Chatbot page."""
    
    st.title("🌱 Climate Chatbot")
    st.write("---")

    st.subheader("Ask me anything about climate change!")
    st.write(
        """
        Welcome to the Climate Chatbot. I can help answer questions about climate change, sustainability, and how you can contribute to a greener planet.
        Just type your question below, and I'll do my best to provide an informative answer.
        """
    )

    user_input = st.text_input("Ask your question:")

    if user_input:
        answer = get_climate_answer(user_input)
        st.write(f"🌍 **Bot Response**: {answer}")

    st.write("---")
    st.write("🔗 Stay informed, and take action towards a more sustainable future!")
