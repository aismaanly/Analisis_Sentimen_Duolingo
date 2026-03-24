# Duolingo Sentiment Analysis 🦉

This project focuses on performing sentiment analysis on user reviews of the Duolingo application on the Google Play Store (specifically targeting Indonesian reviews). The project is divided into two primary phases: **Data Scraping** (collecting reviews) and **Sentiment Analysis** (data cleaning, lexicon-based labeling, and Machine Learning/Deep Learning modeling).

## 🗂️ Project Structure

- `Scraping_Duolingo.ipynb`: A Jupyter Notebook used to scrape user reviews from the Google Play Store using the `google-play-scraper` library.
- `Analisis_Sentimen_Duolingo.ipynb`: The main Jupyter Notebook containing the end-to-end NLP pipeline. This includes text preprocessing, lexicon-based sentiment labeling, and the implementation/evaluation of multiple machine learning and deep learning models.
- `duolingo_review.csv`: The raw dataset containing the scraped reviews.
- `processed_review.csv`: The cleaned and preprocessed dataset, ready for model training (contains tokenized and lemmatized texts).
- `requirements.txt`: A list of required Python dependencies to run this project.

## 🚀 Workflow

### 1. Data Scraping
We use `google-play-scraper` to extract thousands of reviews from the Google Play Store (`com.duolingo`). Key metrics, such as the review text (*content*) and rating score, are scraped and saved into `duolingo_review.csv`.

### 2. Data Preprocessing & Text Pre-Processing
We clean the data and process the Indonesian text so that it can be optimally understood by our machine learning models:
- **Data Cleaning**: Removing unneeded columns, missing values (NaN), and duplicate entries.
- **Lowercasing & Cleansing**: Converting text to lowercase and removing punctuation and numerical noise.
- **Slang Replacement**: Mapping informal language and Indonesian slang into standardized words.
- **Tokenization & Stopwords Removal**: Splitting sentences into tokens (words) and removing meaningless words (stopwords).
- **Stemming / Lemmatization**: Utilizing the `MPStemmer` library (developed specifically for the Indonesian language) to convert words into their base forms.

### 3. Data Labeling (Lexicon-Based)
To assign a sentiment target (Positive, Negative, or Neutral) to the unlabeled reviews, this project leverages an **Indonesian Sentiment Lexicon Dictionary**. The sentiment score for each document is calculated by summing the positive and negative lexicon values of the constituent words. Visualizations of the final sentiment distributions and Word Clouds for each sentiment category are also included.

### 4. Feature Extraction and Modeling
We built and compared several combinations of text feature extraction techniques and sequence models:
1. **Multilayer Perceptron (MLP) + TF-IDF Vectorizer**: A standard feed-forward Artificial Neural Network baseline.
2. **Long Short-Term Memory (LSTM) + TF-IDF Vectorizer**: A Deep Learning RNN variant adapted to retain long-term dependencies over extended review sequences. It also leverages custom callbacks to halt training when hitting specific validation thresholds.
3. **Simple Recurrent Neural Network (RNN) + Bag of Words (BoW)**: A fundamental sequence model architecture relying on sequential Bag-of-Words features.

Model performances are evaluated based on their **Validation Accuracy** and **Test Accuracy** to measure generalization robustness.

## 🛠️ Dependencies

You need to install the project dependencies, ideally within a virtual environment. Use `requirements.txt` to install all necessary packages:

```bash
pip install -r requirements.txt
```

Key NLP and Machine Learning libraries used in this project include `Sastrawi/MPStemmer`, `nltk`, `wordcloud`, `scikit-learn`, and `TensorFlow`.

## ▶️ How to Run

1. Install all required dependencies using the command above.
2. *(Optional)* Run all cells in `Scraping_Duolingo.ipynb` if you wish to scrape recent data and overwrite `duolingo_review.csv`.
3. Open `Analisis_Sentimen_Duolingo.ipynb`. Run all cells from top to bottom. The notebook will automatically process the raw `.csv` file, perform text preprocessing and sentiment labeling, and ultimately train and evaluate the MLP, LSTM, and RNN models.
