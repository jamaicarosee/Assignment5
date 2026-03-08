import streamlit as st
import pandas as pd
import datetime

st.set_page_config(
    page_title="Make-App",
    page_icon="app_icon.png",
    layout="wide"
)

# SIDEBAR
st.sidebar.image("app_icon.png", width=100) 

# Dropdown menu with new order
page = st.sidebar.selectbox(
    "Menu",
    ["Home", "User Information", "Make-App Recommender", "Beauty Quiz", "About"]
)

# HOME PAGE
if page == "Home":

    st.title("💄 Make-App – Beauty Routine Recommender")
    st.header("Welcome to the Make-App!")

    st.image("home_icon.jpg", width=500)

    st.write("""
    Hi! I'm a Jamaica Madriaga, a college student who loves makeup and beauty products.  
    I created this simple Streamlit app to help people choose makeup styles depending
    on their skin type and occasion.
    """)

    st.success("Go to the User Information page first before using the recommender!")

    st.info("Tip: Makeup should enhance your natural beauty.")

    st.warning("Always check if the product is safe for your skin.")

# USER INFORMATION PAGE (2nd page now)
elif page == "User Information":

    st.header("👤 User Profile")

    name = st.text_input("Enter your name")
    age = st.number_input("Age", 15, 50, 20)

    experience = st.selectbox(
        "Makeup Experience",
        ["Beginner", "Intermediate", "Advanced"]
    )

    skin_type = st.selectbox(
        "Skin Type",
        ["Oily", "Dry", "Combination", "Sensitive"]
    )

    skin_tone = st.selectbox(
        "Skin Tone",
        ["Fair", "Light", "Medium", "Morena", "Deep"]
    )

    favorite_product = st.multiselect(
        "Favorite Makeup Products",
        ["Lipstick", "Foundation", "Blush", "Mascara", "Highlighter"]
    )

    st.write("Today's date:", datetime.date.today())

    if st.button("Save Profile"):
        st.success(f"Profile saved! Welcome, {name}!")

# RECOMMENDER PAGE
elif page == "Make-App Recommender":

    st.header("💄 Find Your Makeup Look")

    col1, col2 = st.columns(2)

    with col1:
        skin_type = st.selectbox(
            "Skin Type",
            ["Oily", "Dry", "Combination", "Sensitive"]
        )

        skin_tone = st.selectbox(
            "Skin Tone",
            ["Fair", "Light", "Medium", "Morena", "Deep"]
        )

        occasion = st.radio(
            "Occasion",
            ["School", "Date", "Party", "Casual Hangout"]
        )

    with col2:
        coverage = st.slider("Foundation Coverage", 0, 100, 50)

        favorite_color = st.color_picker("Pick your favorite lipstick color")

        glitter = st.checkbox("Do you like glitter eyeshadow?")

        makeup_time = st.time_input("What time do you usually do makeup?")

    st.subheader("Makeup Preferences")

    products = st.multiselect(
        "Choose products you usually use",
        ["Foundation", "Concealer", "Blush", "Bronzer", "Highlighter", "Lipstick", "Mascara"]
    )

    mood = st.select_slider(
        "Your makeup mood today",
        options=["Natural", "Soft Glam", "Full Glam"]
    )

    rating = st.slider("How much do you love makeup?", 1, 10)

    if st.button("Generate Make-App Recommendation 💄"):

        st.subheader("Your Suggested Look")

        if occasion == "School":
            st.write("✨ Natural everyday makeup")
            st.write("- Light foundation")
            st.write("- Soft blush")
            st.write("- Mascara")

        elif occasion == "Date":
            st.write("💕 Romantic makeup")
            st.write("- Pink blush")
            st.write("- Shimmer eyeshadow")
            st.write("- Glossy lips")

        elif occasion == "Party":
            st.write("🎉 Glam makeup")
            st.write("- Full coverage foundation")
            st.write("- Glitter eyeshadow")
            st.write("- Bold lipstick")

        else:
            st.write("🌸 Soft casual look")

        st.write("Your chosen lipstick color:", favorite_color)

        st.balloons()

# QUIZ PAGE
elif page == "Beauty Quiz":

    st.header("💋 Quick Beauty Quiz")

    q1 = st.radio("What is the most important makeup product?", 
                  ["Foundation", "Mascara", "Lipstick"])

    q2 = st.radio("How often do you wear makeup?", 
                  ["Daily", "Sometimes", "Rarely"])

    q3 = st.radio("Favorite makeup style?", 
                  ["Natural", "Soft Glam", "Full Glam"])

    if st.button("Submit Quiz"):

        data = {
            "Question": [
                "Important Product",
                "Makeup Frequency",
                "Favorite Style"
            ],
            "Answer": [q1, q2, q3]
        }

        df = pd.DataFrame(data)

        st.write("Your Answers:")
        st.table(df)

        st.success("Thanks for answering the beauty quiz!")

# ABOUT PAGE
elif page == "About":

    st.header("ℹ️ About This App")
    
    st.write("**App Name:** Make-App – Beauty Routine Recommender")

    st.subheader("What the app does")
    st.write("""
    This app helps users choose a makeup look based on their skin type,
    skin tone, occasion, and makeup preferences.
    """)

    st.subheader("Target Users")
    st.write("""
    Students, beginners, and people interested in simple makeup routines.
    """)

    st.subheader("Inputs Collected")
    st.write("""
    - User profile information
    - Skin type and skin tone
    - Occasion and makeup preferences
    """)

    st.subheader("Outputs Shown")
    st.write("""
    - Suggested makeup looks
    - Beauty quiz results
    """)

    st.caption("Created as a project in ITP222")