import streamlit as st

# Title and Description
st.title("Waste Management Tracker")
st.write("Track your waste and get suggestions for recycling or composting.")

# Input Waste Data
waste_type = st.selectbox("Select Waste Type", ["Organic", "Plastic", "Paper", "Metal", "Glass", "Other"])
waste_amount = st.number_input("Enter amount of waste (in quantity)", min_value=0.0)

# Initialize session state for storing waste data
if 'waste_data' not in st.session_state:
    st.session_state['waste_data'] = []

# Add Waste Data
if st.button("Add Waste"):
    st.session_state['waste_data'].append({'type': waste_type, 'amount': waste_amount})
    st.success(f"Added {waste_amount} kg of {waste_type} waste.")

# Display Waste Data
st.write("Waste Data:")
st.write(st.session_state['waste_data'])

# Suggestions for Recycling or Composting
def get_suggestions(waste_type):
    suggestions = {
        "Organic": "Consider composting organic waste to create nutrient-rich soil.",
        "Plastic": "Recycle plastic waste at your nearest recycling center.",
        "Paper": "Recycle paper waste or use it for crafts and projects.",
        "Metal": "Recycle metal waste to reduce environmental impact.",
        "Glass": "Recycle glass waste at designated facilities.",
        "Other": "Check guidelines online for proper disposal of other types of waste."
    }
    return suggestions.get(waste_type, "No suggestion available for this type of waste.")

# Display Suggestion for the Last Added Waste Type
if st.session_state['waste_data']:
    last_entry = st.session_state['waste_data'][-1]
    suggestion = get_suggestions(last_entry['type'])
    st.write(f"Suggestion for {last_entry['type']} waste: {suggestion}")
