# Text Summarizer Project
# A beginner-friendly text summarization using word frequency

import re
from collections import Counter

def preprocess_text(text):
    # Remove special characters and make everything lowercase
    text = re.sub(r'\s+', ' ', text)
    text = text.lower()
    return text

def get_word_frequencies(text):
    words = re.findall(r'\w+', text)
    stopwords = {'the', 'and', 'is', 'in', 'to', 'of', 'a', 'an'}
    filtered_words = [word for word in words if word not in stopwords]
    return Counter(filtered_words)

def score_sentences(sentences, word_freq):
    sentence_scores = {}
    for sentence in sentences:
        sentence_lower = sentence.lower()
        score = 0
        for word in word_freq:
            if word in sentence_lower:
                score += word_freq[word]
        sentence_scores[sentence] = score
    return sentence_scores

def summarize(text, max_sentences=2):
    sentences = re.split(r'(?<=[.!?]) +', text)
    preprocessed = preprocess_text(text)
    word_freq = get_word_frequencies(preprocessed)
    scores = score_sentences(sentences, word_freq)
    sorted_sentences = sorted(scores, key=scores.get, reverse=True)
    summary = ' '.join(sorted_sentences[:max_sentences])
    return summary

# Example
text = """Artificial Intelligence is changing the world. It is used in medicine, education, and finance. 
It helps machines learn from data. AI is also used in chatbots and translation tools. Many people are learning AI these days."""
print("Summary:")
print(summarize(text))
