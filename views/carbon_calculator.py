import streamlit as st


def carbon_calculator_page():
    """Displays the Carbon Footprint Calculator page for GaiaGuard."""

    # --- Page Title ---
    st.title("🌿 Carbon Footprint Calculator")
    st.write("---")

    # --- Introduction ---
    st.subheader("Calculate Your Carbon Footprint")
    st.write(
        """
        Your carbon footprint measures the greenhouse gas emissions from your daily activities.
        Use this tool to estimate your impact and discover ways to reduce it.
        """
    )

    # --- Inputs for Calculator ---
    st.subheader("🌟 Enter Your Details Below")

    # Transportation
    st.write("### 🚗 Transportation")
    car_miles = st.number_input("Miles driven per week (Car)", min_value=0, step=1)
    bus_miles = st.number_input("Miles traveled per week (Bus)", min_value=0, step=1)
    flight_hours = st.number_input("Flight hours per month", min_value=0.0, step=0.1)

    # Energy Usage
    st.write("### 🏠 Home Energy")
    electricity_kwh = st.number_input("Monthly electricity usage (kWh)", min_value=0.0, step=0.1)
    gas_therms = st.number_input("Monthly natural gas usage (therms)", min_value=0.0, step=0.1)
    oil_gallons = st.number_input("Monthly heating oil usage (gallons)", min_value=0.0, step=0.1)

    # Diet
    st.write("### 🍽️ Diet")
    diet_choice = st.selectbox(
        "Select your diet type:",
        ("Meat-heavy", "Average", "Vegetarian", "Vegan")
    )

    # --- Calculation Logic ---
    st.write("---")
    st.subheader("📊 Results")
    
    if st.button("Calculate Carbon Footprint"):
        # Transportation emissions (in kg CO2e per year)
        car_emissions = car_miles * 0.404 * 52  # 0.404 kg CO2e per mile for an average car
        bus_emissions = bus_miles * 0.089 * 52  # 0.089 kg CO2e per mile for bus travel
        flight_emissions = flight_hours * 255  # 255 kg CO2e per hour of air travel

        # Energy emissions (in kg CO2e per year)
        electricity_emissions = electricity_kwh * 0.92 * 12  # 0.92 kg CO2e per kWh
        gas_emissions = gas_therms * 5.3 * 12  # 5.3 kg CO2e per therm
        oil_emissions = oil_gallons * 10.21 * 12  # 10.21 kg CO2e per gallon

        # Diet emissions (in kg CO2e per year)
        diet_emissions = {
            "Meat-heavy": 3000,
            "Average": 2500,
            "Vegetarian": 1500,
            "Vegan": 1000,
        }.get(diet_choice, 2500)

        # Total Emissions
        total_emissions = (
            car_emissions + bus_emissions + flight_emissions +
            electricity_emissions + gas_emissions + oil_emissions +
            diet_emissions
        )

        # Display results
        st.success(f"🌍 Your estimated annual carbon footprint is **{total_emissions:,.2f} kg CO2e**.")

        # --- Suggestions Section ---
        st.write("---")
        st.subheader("💡 Suggestions to Reduce Your Carbon Footprint")
        suggestions = [
            "🚲 Use bicycles or walk for short trips instead of driving.",
            "🚆 Opt for public transportation or carpooling.",
            "💡 Switch to energy-efficient appliances and LED bulbs.",
            "🌱 Consider adopting a plant-based diet or reducing meat consumption.",
            "🔌 Unplug devices when not in use to save electricity.",
            "🌍 Purchase carbon offsets to neutralize unavoidable emissions."
        ]
        for suggestion in suggestions:
            st.write(suggestion)

    else:
        st.info("Enter your details and press **Calculate Carbon Footprint** to see your results.")

    # --- Footer ---
    st.write("---")
    st.write("🌱 **Every small action counts. Start your journey to sustainability today!**")
