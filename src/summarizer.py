from textblob import TextBlob
import matplotlib.pyplot as plt
from wordcloud import WordCloud

from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.tokenize.treebank import TreebankWordDetokenizer
from nltk.probability import FreqDist

import os


def text_summarize(text, num_sentences=3):
    sentences = sent_tokenize(text)

    words = word_tokenize(text.lower())
    stop_words = set(stopwords.words("english"))

    words = [word for word in words if word.isalnum() and word not in stop_words]

    frequency_dist = FreqDist(words)
    max_freq = max(frequency_dist.values())

    sentence_scores = {}

    for sentence in sentences:
        for word in word_tokenize(sentence.lower()):
            if word in frequency_dist:
                if sentence in sentence_scores:
                    sentence_scores[sentence] += frequency_dist[word] / max_freq
                else:
                    sentence_scores[sentence] = frequency_dist[word] / max_freq

    summary_sentences = sorted(
        sentence_scores, key=sentence_scores.get, reverse=True
    )[:num_sentences]

    summary = TreebankWordDetokenizer().detokenize(summary_sentences)

    return summary


def sentiment_analysis(text):
    analysis = TextBlob(text)
    sentiment = SentimentIntensityAnalyzer()

    vader_scores = sentiment.polarity_scores(text)

    if analysis.sentiment.polarity > 0:
        result = "Positive"
    elif analysis.sentiment.polarity < 0:
        result = "Negative"
    else:
        result = "Neutral"

    return f"{result} : {vader_scores}"


def word_cloud(text, filename):

    os.makedirs("static/images", exist_ok=True)

    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color="white"
    ).generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.title("Word Cloud")

    file_path = f"static/images/{filename}"

    plt.savefig(file_path)
    plt.close()

    return file_path