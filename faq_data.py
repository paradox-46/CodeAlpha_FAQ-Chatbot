"""
FAQ Data Collection and Management
Contains sample FAQs for the chatbot demonstration
"""

FAQS = [
    {
        "question": "What is Python?",
        "answer": "Python is a high-level, interpreted programming language known for its simplicity and readability. It was created by Guido van Rossum and first released in 1991. Python supports multiple programming paradigms including procedural, object-oriented, and functional programming."
    },
    {
        "question": "How do I install Python?",
        "answer": "To install Python, visit python.org and download the latest version for your operating system. For Windows, run the installer and check 'Add Python to PATH'. For macOS, you can use Homebrew: 'brew install python'. For Linux, use your package manager: 'sudo apt install python3' (Ubuntu/Debian) or 'sudo yum install python3' (CentOS/RHEL)."
    },
    {
        "question": "What is a variable in programming?",
        "answer": "A variable is a named storage location in computer memory that can hold data. Variables have a name, a type, and a value. They allow programmers to store and manipulate data during program execution. In Python, variables are dynamically typed, meaning you don't need to declare their type explicitly."
    },
    {
        "question": "What is machine learning?",
        "answer": "Machine learning is a subset of artificial intelligence that enables computers to learn and improve from experience without being explicitly programmed. It uses algorithms to identify patterns in data and make predictions or decisions. Common types include supervised learning, unsupervised learning, and reinforcement learning."
    },
    {
        "question": "How do I create a virtual environment in Python?",
        "answer": "To create a virtual environment in Python, use the command: 'python -m venv myenv' (replace 'myenv' with your desired environment name). To activate it: On Windows use 'myenv\\Scripts\\activate', on macOS/Linux use 'source myenv/bin/activate'. To deactivate, simply type 'deactivate'."
    },
    {
        "question": "What is Git?",
        "answer": "Git is a distributed version control system that tracks changes in source code during software development. It was created by Linus Torvalds in 2005. Git allows multiple developers to work on the same project simultaneously, maintains a complete history of changes, and enables branching and merging of code."
    },
    {
        "question": "How do I commit changes in Git?",
        "answer": "To commit changes in Git, first add your files with 'git add <filename>' or 'git add .' for all files. Then commit with a message using 'git commit -m \"Your commit message\"'. You can also use 'git status' to see which files have been modified."
    },
    {
        "question": "What is an API?",
        "answer": "An API (Application Programming Interface) is a set of rules and protocols that allows different software applications to communicate with each other. APIs define the methods and data formats that applications can use to request and exchange information. They act as intermediaries between different software systems."
    },
    {
        "question": "What is the difference between HTTP and HTTPS?",
        "answer": "HTTP (Hypertext Transfer Protocol) is the standard protocol for transmitting data over the web. HTTPS is the secure version of HTTP that uses SSL/TLS encryption to protect data transmission. HTTPS encrypts all data between the client and server, making it much more secure for sensitive information like passwords and credit card details."
    },
    {
        "question": "What is a database?",
        "answer": "A database is an organized collection of structured information or data, typically stored electronically in a computer system. Databases are designed to efficiently store, retrieve, and manage data. Common types include relational databases (like MySQL, PostgreSQL) and NoSQL databases (like MongoDB, Cassandra)."
    },
    {
        "question": "What is object-oriented programming?",
        "answer": "Object-oriented programming (OOP) is a programming paradigm based on the concept of 'objects' that contain data and code. The four main principles are: Encapsulation (bundling data and methods), Inheritance (creating new classes from existing ones), Polymorphism (same interface, different implementations), and Abstraction (hiding complex implementation details)."
    },
    {
        "question": "How do I handle errors in Python?",
        "answer": "In Python, you can handle errors using try-except blocks. The basic syntax is: 'try: code_that_might_raise_error except ExceptionType: handle_error'. You can also use 'finally' for cleanup code that always runs, and 'else' for code that runs only if no exception occurs."
    },
    {
        "question": "What is a function?",
        "answer": "A function is a reusable block of code that performs a specific task. Functions help organize code, reduce duplication, and make programs more modular. They can accept parameters (inputs) and return values (outputs). Functions are defined using the 'def' keyword in Python."
    },
    {
        "question": "What is the difference between a list and a tuple in Python?",
        "answer": "Lists and tuples are both sequence types in Python, but lists are mutable (can be changed after creation) while tuples are immutable (cannot be changed). Lists use square brackets [1, 2, 3] and tuples use parentheses (1, 2, 3). Tuples are generally faster and use less memory than lists."
    },
    {
        "question": "What is a loop in programming?",
        "answer": "A loop is a programming construct that repeats a block of code multiple times. Common types include: for loops (iterate over a sequence), while loops (repeat while a condition is true), and do-while loops (execute at least once, then check condition). Loops are essential for processing data and automating repetitive tasks."
    },
    {
        "question": "What is debugging?",
        "answer": "Debugging is the process of finding and fixing errors (bugs) in computer programs. It involves identifying the cause of unexpected behavior, understanding how the program flows, and correcting the issues. Common debugging techniques include using print statements, debuggers, logging, and systematic problem-solving approaches."
    }
]

def get_faqs():
    """Return the list of FAQs"""
    return FAQS

def get_questions():
    """Return just the questions from FAQs"""
    return [faq["question"] for faq in FAQS]

def get_answers():
    """Return just the answers from FAQs"""
    return [faq["answer"] for faq in FAQS] 