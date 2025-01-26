# Import required libraries
from textblob import TextBlob
from wordcloud import WordCloud, STOPWORDS
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import streamlit as st
import pandas as pd

# Initialize VADER Sentiment Analyzer
analyzer = SentimentIntensityAnalyzer()

# Streamlit App Title
st.title('Enhanced Sentiment Analysis App')

# Text Input
user_input = st.text_area("Enter text for sentiment analysis:")

# "Send" Button
if st.button("Send"):
    if user_input.strip():  # Ensure input is not empty
        # Analyze with TextBlob
        blob = TextBlob(user_input)
        tb_polarity = blob.sentiment.polarity

        # Analyze with VADER
        vader_scores = analyzer.polarity_scores(user_input)
        vader_compound = vader_scores['compound']

        # Define Sentiment Categories
        if vader_compound > 0.75:
            sentiment_label = "Very Positive"
            label_color = "darkgreen"
        elif 0.05 < vader_compound <= 0.75:
            sentiment_label = "Positive"
            label_color = "green"
        elif -0.05 <= vader_compound <= 0.05:
            sentiment_label = "Neutral"
            label_color = "gray"
        elif -0.75 <= vader_compound < -0.05:
            sentiment_label = "Negative"
            label_color = "orange"
        else:
            sentiment_label = "Very Negative"
            label_color = "red"

        # Display Results
        st.write(f"### Sentiment Results")
        st.markdown(f"**TextBlob Polarity:** `{tb_polarity:.2f}` (Range: -1 to 1)")
        st.markdown(f"**VADER Compound Score:** `{vader_compound:.2f}` (Range: -1 to 1)")
        st.markdown(f"<span style='color:{label_color};font-weight:bold'>Overall Sentiment (VADER): {sentiment_label}</span>", unsafe_allow_html=True)

        # Visualization of VADER Scores
        st.write("#### VADER Sentiment Breakdown")
        vader_df = pd.DataFrame({
            'Sentiment': ['Positive', 'Neutral', 'Negative'],
            'Score': [vader_scores['pos'], vader_scores['neu'], vader_scores['neg']]
        })
        st.bar_chart(vader_df.set_index('Sentiment'))

        # Generate Word Cloud
        st.write("#### Word Cloud")
        stopwords = set(STOPWORDS)
        wordcloud = WordCloud(stopwords=stopwords, background_color='white').generate(user_input)
        st.image(wordcloud.to_array(), caption='Word Cloud')
    else:
        st.write("Please enter some text for analysis.")
