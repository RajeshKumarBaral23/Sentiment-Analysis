# sentiment analysis with MachineLearning
# Sentiment Analysis of Customer Reviews

## Problem Statement
The goal of this project is to analyze customer reviews to determine their sentiment (positive, neutral, or negative). By leveraging natural language processing (NLP) and machine learning techniques, we aim to build a model that can accurately classify the sentiment of reviews. This can help businesses understand customer feedback and improve their products and services.

## Unique Features
1. **Contextual Sentiment Analysis**: Incorporates custom keywords to recognize specific contexts (e.g., detecting "disgusting" keywords) for more nuanced sentiment analysis.
2. **Multiple Sentiment Analysis Techniques**: Utilizes both VADER and TextBlob for sentiment analysis, providing a comparison of rule-based and machine learning-based approaches.
3. **Advanced Text Processing**: Employs advanced text preprocessing techniques, including lemmatization and custom stopwords handling, to improve model accuracy.
4. **Hyperparameter Tuning**: Uses GridSearchCV for hyperparameter tuning of machine learning models to achieve optimal performance.
5. **Interactive Web Application**: Deploys the sentiment analysis model using Streamlit, allowing users to interact with the model through a web interface.
6. **Comprehensive Model Evaluation**: Provides detailed model evaluation metrics, including accuracy, precision, recall, F1-score, and confusion matrix, for thorough performance assessment.
7. **Visualization**: Generates word clouds to visualize the most frequent words in the reviews, enhancing the interpretability of the data.

## End Users
1. **Businesses and Companies**: To analyze customer feedback and improve products or services based on sentiment trends.
2. **Marketing Teams**: To gauge customer sentiment towards marketing campaigns and brand perception.
3. **Product Managers**: To understand user satisfaction and identify areas for product improvement.
4. **Customer Support Teams**: To prioritize and address negative feedback more effectively.
5. **Researchers and Analysts**: To study sentiment trends and patterns in customer reviews.
6. **Developers and Data Scientists**: To use the project as a reference or starting point for similar sentiment analysis tasks.

## Installation
To run this project locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/sentiment-analysis.git
    cd sentiment-analysis
    ```

2. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

3. Download NLTK data:
    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')
    ```

## Usage
1. **Training the Model**:
    - Open the [sentimentanalysis.ipynb](http://_vscodecontentref_/1) notebook.
    - Run all cells to preprocess the data, train the models, and save the trained models and vectorizers.

2. **Running the Streamlit App**:
    - Navigate to the directory containing `APPP.py`.
    - Run the following command:
        ```sh
        streamlit run APPP.py
        ```
    - Open the provided URL in your browser to interact with the sentiment analysis web app.

## Conclusion
This project successfully addresses the problem of analyzing customer reviews to determine their sentiment. By implementing advanced NLP and machine learning techniques, we have developed a robust model that can accurately classify sentiments. The interactive web application further enhances the usability of the model, allowing businesses and other stakeholders to gain valuable insights from customer feedback. This can lead to improved products, services, and overall customer satisfaction.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
