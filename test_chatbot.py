"""
Test script for FAQ Chatbot
Verifies that all components work correctly
"""

from chatbot import FAQChatbot
from nlp_processor import NLPProcessor
from faq_data import get_faqs, get_questions, get_answers

def test_faq_data():
    """Test FAQ data loading"""
    print("Testing FAQ data...")
    
    faqs = get_faqs()
    questions = get_questions()
    answers = get_answers()
    
    print(f"✓ Loaded {len(faqs)} FAQs")
    print(f"✓ Loaded {len(questions)} questions")
    print(f"✓ Loaded {len(answers)} answers")
    
    # Test a sample FAQ
    if faqs:
        sample_faq = faqs[0]
        print(f"✓ Sample FAQ: {sample_faq['question'][:50]}...")
    
    return True

def test_nlp_processor():
    """Test NLP processor functionality"""
    print("\nTesting NLP processor...")
    
    try:
        nlp = NLPProcessor()
        print("✓ NLP processor initialized")
        
        # Test text preprocessing
        test_text = "What is Python programming language?"
        processed = nlp.preprocess_text(test_text)
        print(f"✓ Text preprocessing: '{test_text}' -> '{processed}'")
        
        # Test keyword extraction
        keywords = nlp.extract_keywords(test_text)
        print(f"✓ Keywords extracted: {keywords}")
        
        # Test vectorizer training
        questions = get_questions()
        vectors = nlp.train_vectorizer(questions)
        print(f"✓ Vectorizer trained on {len(questions)} questions")
        
        # Test similarity matching
        match_result = nlp.find_best_match("What is Python?", threshold=0.1)
        print(f"✓ Similarity matching: {match_result['similarity']:.3f} confidence")
        
        return True
        
    except Exception as e:
        print(f"✗ NLP processor error: {e}")
        return False

def test_chatbot():
    """Test chatbot functionality"""
    print("\nTesting chatbot...")
    
    try:
        chatbot = FAQChatbot()
        print("✓ Chatbot initialized")
        
        # Test response generation
        test_questions = [
            "What is Python?",
            "How do I install Python?",
            "What is machine learning?",
            "How do I create a virtual environment?",
            "What is Git?",
            "Random question that shouldn't match"
        ]
        
        for question in test_questions:
            response = chatbot.get_response(question)
            print(f"✓ Q: '{question}'")
            print(f"  A: {response['answer'][:100]}...")
            print(f"  Confidence: {response['confidence']:.3f}")
            print(f"  Match: {response['is_match']}")
            print()
        
        # Test statistics
        stats = chatbot.get_statistics()
        print(f"✓ Statistics: {stats}")
        
        return True
        
    except Exception as e:
        print(f"✗ Chatbot error: {e}")
        return False

def test_search():
    """Test search functionality"""
    print("\nTesting search functionality...")
    
    try:
        chatbot = FAQChatbot()
        
        search_queries = ["python", "install", "machine learning", "git"]
        
        for query in search_queries:
            results = chatbot.search_faqs(query)
            print(f"✓ Search '{query}': {len(results)} results")
            for result in results[:2]:  # Show first 2 results
                print(f"  - {result['question'][:50]}... (similarity: {result['similarity']:.3f})")
            print()
        
        return True
        
    except Exception as e:
        print(f"✗ Search error: {e}")
        return False

def main():
    """Run all tests"""
    print("🧪 FAQ Chatbot Test Suite")
    print("=" * 40)
    
    tests = [
        ("FAQ Data", test_faq_data),
        ("NLP Processor", test_nlp_processor),
        ("Chatbot", test_chatbot),
        ("Search", test_search)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        try:
            if test_func():
                passed += 1
                print(f"✅ {test_name} test passed\n")
            else:
                print(f"❌ {test_name} test failed\n")
        except Exception as e:
            print(f"❌ {test_name} test error: {e}\n")
    
    print("=" * 40)
    print(f"📊 Test Results: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 All tests passed! The chatbot is ready to run.")
        print("\nTo start the web application, run:")
        print("python app.py")
        print("\nThen open http://localhost:5000 in your browser.")
    else:
        print("⚠️  Some tests failed. Please check the errors above.")
    
    return passed == total

if __name__ == "__main__":
    main() 