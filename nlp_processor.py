"""
NLP Processor for FAQ Chatbot
Handles text preprocessing, tokenization, and similarity matching
"""

import re
import nltk
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from textblob import TextBlob
import string

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class NLPProcessor:
    def __init__(self):
        """Initialize the NLP processor with stopwords and punctuation"""
        self.stop_words = set(stopwords.words('english'))
        self.punctuation = string.punctuation
        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            stop_words='english',
            ngram_range=(1, 2),
            max_features=1000
        )
        self.faq_vectors = None
        self.faq_questions = None
        
    def preprocess_text(self, text):
        """
        Preprocess text by:
        1. Converting to lowercase
        2. Removing punctuation
        3. Tokenizing
        4. Removing stopwords
        5. Lemmatizing
        """
        # Convert to lowercase
        text = text.lower()
        
        # Remove punctuation
        text = re.sub(r'[^\w\s]', '', text)
        
        # Tokenize
        tokens = word_tokenize(text)
        
        # Remove stopwords and short words
        tokens = [token for token in tokens if token not in self.stop_words and len(token) > 2]
        
        # Join tokens back into text
        processed_text = ' '.join(tokens)
        
        return processed_text
    
    def extract_keywords(self, text):
        """Extract important keywords from text using TextBlob"""
        blob = TextBlob(text)
        # Get noun phrases and important words
        keywords = []
        
        # Add noun phrases
        keywords.extend(blob.noun_phrases)
        
        # Add important words (nouns, adjectives, verbs)
        for word, tag in blob.tags:
            if tag.startswith(('NN', 'JJ', 'VB')) and len(word) > 2:
                keywords.append(word.lower())
        
        return list(set(keywords))
    
    def train_vectorizer(self, faq_questions):
        """
        Train the TF-IDF vectorizer on FAQ questions
        """
        self.faq_questions = faq_questions
        
        # Preprocess all questions
        processed_questions = [self.preprocess_text(q) for q in faq_questions]
        
        # Fit and transform the vectorizer
        self.faq_vectors = self.vectorizer.fit_transform(processed_questions)
        
        return self.faq_vectors
    
    def find_best_match(self, user_question, threshold=0.1):
        """
        Find the best matching FAQ question using cosine similarity
        Returns (best_match_index, similarity_score, processed_question)
        """
        if self.faq_vectors is None:
            raise ValueError("Vectorizer must be trained first. Call train_vectorizer()")
        
        # Preprocess user question
        processed_question = self.preprocess_text(user_question)
        
        # Transform user question
        user_vector = self.vectorizer.transform([processed_question])
        
        # Calculate cosine similarity
        similarities = cosine_similarity(user_vector, self.faq_vectors).flatten()
        
        # Find the best match
        best_match_index = np.argmax(similarities)
        best_similarity = similarities[best_match_index]
        
        # Return results
        return {
            'index': best_match_index,
            'similarity': best_similarity,
            'question': self.faq_questions[best_match_index],
            'processed_question': processed_question,
            'threshold': threshold,
            'is_match': best_similarity >= threshold
        }
    
    def get_similarity_analysis(self, user_question):
        """
        Get detailed similarity analysis for debugging
        """
        if self.faq_vectors is None:
            return None
        
        processed_question = self.preprocess_text(user_question)
        user_vector = self.vectorizer.transform([processed_question])
        similarities = cosine_similarity(user_vector, self.faq_vectors).flatten()
        
        # Get top 5 matches
        top_indices = np.argsort(similarities)[::-1][:5]
        
        analysis = {
            'user_question': user_question,
            'processed_question': processed_question,
            'top_matches': []
        }
        
        for idx in top_indices:
            analysis['top_matches'].append({
                'index': idx,
                'question': self.faq_questions[idx],
                'similarity': similarities[idx]
            })
        
        return analysis 