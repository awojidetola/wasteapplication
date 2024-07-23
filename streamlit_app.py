import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and Description
st.title("Waste Management Tracker")
st.write("Track your waste and get suggestions for recycling or composting.")

# Input Waste Data
waste_type = st.selectbox("Select Waste Type", ["Organic", "Plastic", "Paper", "Metal", "Glass", "Other"])
waste_amount = st.number_input("Enter the quantity of waste", min_value=0)

# Initialize session state for storing waste data
if 'waste_data' not in st.session_state:
    st.session_state['waste_data'] = pd.DataFrame(columns=['Type', 'Amount'])

# Add Waste Data
if st.button("Add Waste"):
    new_data = pd.DataFrame({'Type': [waste_type], 'Amount': [waste_amount]})
    st.session_state['waste_data'] = pd.concat([st.session_state['waste_data'], new_data], ignore_index=True)
    st.success(f"Added {waste_amount} quantity of {waste_type} waste.")

# Display Waste Data
st.write("Waste Data:")
st.table(st.session_state['waste_data'])

# Suggestions for Recycling or Composting
def get_suggestions(waste_type):
    suggestions = {
        "Organic": "Consider composting organic waste to create nutrient-rich soil.",
        "Plastic": "Recycle plastic waste to store other items.",
        "Paper": "Recycle paper waste or use it for crafts and projects.",
        "Metal": "Recycle metal waste to reduce environmental impact.",
        "Glass": "Recycle glass waste at designated facilities.",
        "Other": "Check guidelines for proper disposal of other types of waste."
    }
    return suggestions.get(waste_type, "No suggestion available for this type of waste.")

# Display Suggestion for the Last Added Waste Type
if not st.session_state['waste_data'].empty:
    last_entry = st.session_state['waste_data'].iloc[-1]
    suggestion = get_suggestions(last_entry['Type'])
    st.write(f"Suggestion for {last_entry['Type']} waste: {suggestion}")

data = st.session_state['waste_data'].sort_values()

# Visualize Data
if st.button("Visualise"):
    st.write("Waste Data Visualization:")
    st.bar_chart(data.groupby('Type').sum())
    #fig, ax = plt.subplots()
    #st.session_state['waste_data'].groupby('Type').sum().plot(kind='bar', ax=ax)
    #st.pyplot(fig)
