import streamlit as st
import langchain_helper  # Import the helper file

st.title("🍽️ Restaurant Name & Menu Generator")

cuisine = st.sidebar.selectbox("Pick a Cuisine", ("Indian", "Italian", "Mexican", "Arabic", "American"))

if cuisine:
    response = langchain_helper.generate_restaurant_name_and_items(cuisine)
    st.header(response['restaurant_name'].strip())  # Display restaurant name
    menu_items = response['menu_items'].strip().split(",")
    
    st.subheader("🍲 Suggested Menu Items")
    for item in menu_items:
        st.write("-", item.strip())  # Display each menu item
