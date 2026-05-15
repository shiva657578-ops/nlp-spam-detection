import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string

# Download required data (safe check)
nltk.download('punkt')
nltk.download('stopwords')

# Streamlit UI
st.title(" NLP Spam Detection App")

# Input box
text = st.text_area("Enter your message:")

if st.button("Analyze Text"):

    if text.strip() == "":
        st.warning("Please enter some text")
    else:

        # 1. Cleaning
        text_clean = text.lower()
        text_clean = text_clean.translate(str.maketrans('', '', string.punctuation))

        # 2. Tokenization
        tokens = word_tokenize(text_clean)

        # 3. Stopword removal
        stop_words = set(stopwords.words('english'))
        filtered_words = [word for word in tokens if word not in stop_words]

        # 4. Stemming
        ps = PorterStemmer()
        stemmed_words = [ps.stem(word) for word in filtered_words]

        # 5. Simple spam detection logic
        spam_keywords = ["free", "win", "prize", "click", "offer", "money"]
        is_spam = any(word in stemmed_words for word in spam_keywords)

        # OUTPUT UI
        st.subheader(" Original Text")
        st.write(text)

        st.subheader("1️ Cleaned Text")
        st.write(text_clean)

        st.subheader("2️ Tokens")
        st.write(tokens)

        st.subheader("3️ Stopword Removal")
        st.write(filtered_words)

        st.subheader("4️ Stemmed Words")
        st.write(stemmed_words)

        st.subheader("5️ Final Result")

        if is_spam:
            st.error(" SPAM MESSAGE DETECTED")
        else:
            st.success(" NOT SPAM")