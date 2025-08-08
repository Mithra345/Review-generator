import nltk

# Auto-download NLTK resources if missing
nltk.download('punkt')
nltk.download('punkt_tab')

# Your other imports
import streamlit as st
import openai
import os
import pyttsx3
import sqlite3
from dotenv import load_dotenv
from textblob import TextBlob
from rake_nltk import Rake


# Load API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_base = "https://openrouter.ai/api/v1"

# Connect to SQLite
conn = sqlite3.connect("reviews.db")
cursor = conn.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT,
        category TEXT,
        rating INTEGER,
        tone TEXT,
        review TEXT,
        sentiment TEXT,
        keywords TEXT
    )
""")
conn.commit()

# App Title
st.title("🛍️ Product Review Generator using GPT")

# Inputs
product_name = st.text_input("📌 Enter Product Name:")
category = st.selectbox("📂 Select Category:", ["Electronics", "Fashion", "Home", "Beauty", "Books", "Other"])
rating = st.slider("⭐ Select Rating (1–5 stars):", 1, 5, 4)
tone = st.selectbox("🎨 Select Tone:", ["Professional", "Casual", "Funny", "Excited", "Honest"])
model = st.selectbox("🧠 Select GPT Model:", ["gpt-3.5-turbo", "gpt-4"])
image = st.file_uploader("🖼️ Upload Product Image (optional):", type=["png", "jpg", "jpeg"])
count_toggle = st.radio("🔢 Show:", ["Word Count", "Character Count"])

# Generate Review
if st.button("🎯 Generate Review"):
    if product_name:
        with st.spinner("Generating review..."):
            prompt = (
                f"Write a {tone.lower()} product review for a {category.lower()} product named "
                f"'{product_name}' with a {rating}-star rating."
            )
            try:
                response = openai.ChatCompletion.create(
                    model=model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.7,
                    max_tokens=250
                )
                review = response['choices'][0]['message']['content']
                st.session_state['review'] = review

                # Display Review
                st.success("✅ Review Generated:")
                st.write(review)

                # Image Display
                if image:
                    st.image(image, caption="Uploaded Product Image", use_column_width=True)

                # Count
                if count_toggle == "Word Count":
                    st.info(f"🧮 Word Count: {len(review.split())}")
                else:
                    st.info(f"✍️ Character Count: {len(review)}")

                # Sentiment
                sentiment = TextBlob(review).sentiment.polarity
                if sentiment > 0.1:
                    sentiment_label = "Positive"
                elif sentiment < -0.1:
                    sentiment_label = "Negative"
                else:
                    sentiment_label = "Neutral"
                st.markdown(f"📊 Sentiment: **{sentiment_label}**")

                # Keywords
                r = Rake()
                r.extract_keywords_from_text(review)
                keywords = ", ".join(r.get_ranked_phrases()[:5])
                st.markdown(f"🔑 Top Keywords: `{keywords}`")

                # Save to DB
                cursor.execute("""
                    INSERT INTO reviews (product_name, category, rating, tone, review, sentiment, keywords)
                    VALUES (?, ?, ?, ?, ?, ?, ?)
                """, (product_name, category, rating, tone, review, sentiment_label, keywords))
                conn.commit()

            except Exception as e:
                st.error(f"❌ Error generating review: {e}")
    else:
        st.warning("⚠️ Please enter a product name.")

# Text-to-Speech
if st.button("🔊 Speak Review"):
    if 'review' in st.session_state:
        try:
            engine = pyttsx3.init()
            engine.say(st.session_state['review'])
            engine.runAndWait()
        except Exception as e:
            st.error(f"🔊 TTS Error: {e}")
    else:
        st.warning("⚠️ Generate review first.")

# Save Review to File
if 'review' in st.session_state:
    if st.button("💾 Save Review to File"):
        filename = f"{product_name.replace(' ', '_')}_review.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(st.session_state['review'])
            st.success(f"📁 Saved as {filename}")
        except Exception as e:
            st.error(f"❌ Error saving file: {e}")
