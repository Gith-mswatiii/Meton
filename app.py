import streamlit as st

st.set_page_config(page_title="Meton - Carbon Tracker", page_icon="🌿")

st.title("🌍 EcoMeter - Your Personal Carbon Footprint Tracker")
st.write("Estimate your monthly carbon emissions and get tips to reduce them!")

# Questions
distance = st.number_input("🚗 How many km do you drive per week?", 0, 2000, 50)
electricity = st.number_input("💡 How many kWh of electricity do you use per month?", 0, 2000, 100)
meat_meals = st.slider("🍖 How many meat-based meals do you eat per week?", 0, 21, 7)
flights = st.number_input("✈️ How many short flights (under 3h) do you take per year?", 0, 50, 0)
recycle = st.selectbox("♻️ Do you recycle regularly?", ["Yes", "No"])

# Simple emission factors (approx kg CO2)
EF_DRIVE = 0.2  # per km
EF_ELECTRICITY = 0.5  # per kWh
EF_MEAT = 7.0  # per meal
EF_FLIGHT = 250  # per short flight

# Calculate footprint
monthly_footprint = (
    distance * 4 * EF_DRIVE +
    electricity * EF_ELECTRICITY +
    meat_meals * 4 * EF_MEAT +
    (flights / 12) * EF_FLIGHT
)

if recycle == "Yes":
    monthly_footprint *= 0.9  # 10% reduction for recycling

st.subheader(f"🌿 Estimated monthly footprint: {monthly_footprint:.1f} kg CO₂")

# Interpretation
if monthly_footprint < 200:
    st.success("Excellent! You're living a very eco-friendly lifestyle 🌱")
elif monthly_footprint < 400:
    st.info("Good job! You can improve further by reducing meat or electricity use.")
else:
    st.warning("Your footprint is high ⚠️ Try walking more or switching to renewables.")
