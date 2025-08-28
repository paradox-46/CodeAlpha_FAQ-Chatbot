"""
FAQ Chatbot Implementation
Main chatbot class that handles question matching and response generation
"""

from faq_data import get_faqs, get_questions, get_answers
from nlp_processor import NLPProcessor
import json

class FAQChatbot:
    def __init__(self):
        """Initialize the FAQ chatbot with data and NLP processor"""
        self.faqs = get_faqs()
        self.questions = get_questions()
        self.answers = get_answers()
        
        # Initialize NLP processor
        self.nlp_processor = NLPProcessor()
        
        # Train the vectorizer on FAQ questions
        self.nlp_processor.train_vectorizer(self.questions)
        
        # Set default threshold for matching
        self.similarity_threshold = 0.15
        
    def get_response(self, user_question):
        """
        Get the best matching response for a user question
        Returns a dictionary with response details
        """
        if not user_question.strip():
            return {
                'answer': "Please ask a question!",
                'confidence': 0.0,
                'matched_question': None,
                'is_match': False,
                'debug_info': None
            }
        
        # Find best match
        match_result = self.nlp_processor.find_best_match(
            user_question, 
            threshold=self.similarity_threshold
        )
        
        # Prepare response
        if match_result['is_match']:
            answer = self.answers[match_result['index']]
            confidence = match_result['similarity']
            matched_question = match_result['question']
        else:
            answer = "I'm sorry, I couldn't find a good match for your question. Could you try rephrasing it or ask something else?"
            confidence = match_result['similarity']
            matched_question = None
        
        # Get similarity analysis and ensure proper format
        top_matches = self.nlp_processor.get_similarity_analysis(user_question)
        processed_matches = []
        
        if top_matches and isinstance(top_matches, list):
            for match in top_matches:
                if isinstance(match, dict):
                    processed_matches.append({
                        'question': str(match.get('question', '')),
                        'similarity': float(match.get('similarity', 0.0)),
                        'index': int(match.get('index', 0))
                    })
        
        return {
            'answer': answer,
            'confidence': confidence,
            'matched_question': matched_question,
            'is_match': match_result['is_match'],
            'debug_info': {
                'processed_question': match_result['processed_question'],
                'similarity_threshold': self.similarity_threshold,
                'top_matches': processed_matches
            }
        }
    
    # ... [rest of your methods remain unchanged] ...