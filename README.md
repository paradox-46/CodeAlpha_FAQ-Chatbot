# FAQ Chatbot - CodeAlpha

A sophisticated FAQ chatbot built with Python, Flask, and NLP techniques. This chatbot uses cosine similarity and TF-IDF vectorization to match user questions with the most relevant FAQ answers.

## 🚀 Features

- **NLP-Powered Matching**: Uses TF-IDF vectorization and cosine similarity for intelligent question matching
- **Beautiful Chat UI**: Modern, responsive web interface with real-time chat functionality
- **FAQ Management**: Comprehensive FAQ database covering programming, technology, and more
- **Search Functionality**: Search through FAQs with instant results
- **Confidence Scoring**: Shows confidence levels for each response
- **Adjustable Threshold**: Fine-tune matching sensitivity with a slider
- **Real-time Statistics**: View chatbot statistics and performance metrics

## 🛠️ Technologies Used

- **Backend**: Python, Flask
- **NLP Libraries**: NLTK, scikit-learn, TextBlob
- **Frontend**: HTML5, CSS3, JavaScript (Vanilla)
- **Vectorization**: TF-IDF with cosine similarity
- **Text Processing**: Tokenization, stopword removal, preprocessing

## 📋 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## 🚀 Installation

1. **Clone or download the project files**

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Open your browser** and navigate to:
   ```
   http://localhost:5000
   ```

## 📁 Project Structure

```
CodeAlpha_FAQ Chatbot/
├── app.py                 # Flask web application
├── chatbot.py            # Main chatbot logic
├── nlp_processor.py      # NLP processing and similarity matching
├── faq_data.py          # FAQ database and data management
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html       # Web interface template
└── README.md            # This file
```

## 🎯 How It Works

### 1. **Text Preprocessing**
- Converts text to lowercase
- Removes punctuation and special characters
- Tokenizes text into words
- Removes stopwords (common words like "the", "is", "at")
- Filters out short words (less than 3 characters)

### 2. **Vectorization**
- Uses TF-IDF (Term Frequency-Inverse Document Frequency) vectorization
- Converts FAQ questions into numerical vectors
- Captures word importance and frequency patterns

### 3. **Similarity Matching**
- Calculates cosine similarity between user question and FAQ questions
- Returns the best matching FAQ based on similarity score
- Uses adjustable threshold for match confidence

### 4. **Response Generation**
- Returns the answer to the best matching question
- Provides confidence score and matched question details
- Handles cases where no good match is found

## 🎮 Usage

### **Chat Interface**
1. Type your question in the chat input
2. Press Enter or click the send button
3. View the bot's response with confidence score
4. See which FAQ question was matched

### **FAQ Sidebar**
- **Browse FAQs**: Click on any FAQ to automatically fill it in the chat input
- **Search FAQs**: Use the search box to find specific questions
- **Adjust Threshold**: Use the slider to change matching sensitivity
- **View Statistics**: See total FAQs and current threshold

### **Example Questions to Try**
- "What is Python?"
- "How do I install Python?"
- "What is machine learning?"
- "How do I create a virtual environment?"
- "What is Git?"
- "What is an API?"
- "How do I handle errors in Python?"

## ⚙️ Configuration

### **Similarity Threshold**
- **Lower threshold (0.05-0.15)**: More lenient matching, more responses
- **Higher threshold (0.15-0.30)**: Stricter matching, higher quality responses
- **Default**: 0.15 (balanced approach)

### **Adding New FAQs**
Edit `faq_data.py` and add new FAQ entries to the `FAQS` list:

```python
{
    "question": "Your question here?",
    "answer": "Your detailed answer here."
}
```

## 🔧 Customization

### **Modifying NLP Processing**
Edit `nlp_processor.py` to:
- Change preprocessing steps
- Adjust vectorization parameters
- Modify similarity calculation methods

### **Styling the Interface**
Edit `templates/index.html` to:
- Change colors and themes
- Modify layout and components
- Add new features to the UI

### **Adding New Features**
- Implement user authentication
- Add conversation history
- Integrate with external APIs
- Add support for multiple languages

## 📊 Performance

- **Response Time**: Typically < 500ms for question matching
- **Accuracy**: High accuracy for programming and technology questions
- **Scalability**: Can handle thousands of FAQs efficiently
- **Memory Usage**: Low memory footprint with TF-IDF vectors

## 🐛 Troubleshooting

### **Common Issues**

1. **Import Errors**:
   ```bash
   pip install -r requirements.txt
   ```

2. **NLTK Data Missing**:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

3. **Port Already in Use**:
   ```bash
   # Change port in app.py
   app.run(debug=True, host='0.0.0.0', port=5001)
   ```

### **Debug Mode**
The application runs in debug mode by default. Check the console for detailed error messages and logs.

## 🤝 Contributing

1. Fork the project
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is created for educational purposes as part of the CodeAlpha FAQ Chatbot task.

## 🎓 Learning Outcomes

This project demonstrates:
- **NLP Techniques**: Text preprocessing, vectorization, similarity matching
- **Web Development**: Flask backend, responsive frontend
- **AI/ML Concepts**: TF-IDF, cosine similarity, confidence scoring
- **Software Architecture**: Modular design, separation of concerns
- **User Experience**: Intuitive interface, real-time interactions

---

**Happy Chatting! 🤖💬** 