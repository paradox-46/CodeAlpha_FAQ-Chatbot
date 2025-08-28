"""
Download NLTK data for FAQ Chatbot
This script downloads all required NLTK data packages
"""

import nltk  # type: ignore
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

def download_nltk_data():
    """Download all required NLTK data"""
    print("📥 Downloading NLTK data...")
    
    # List of required NLTK data packages
    required_packages = [
        'punkt',
        'stopwords',
        'punkt_tab',
        'averaged_perceptron_tagger',
        'maxent_ne_chunker',
        'words'
    ]
    
    for package in required_packages:
        try:
            print(f"Downloading {package}...")
            nltk.download(package, quiet=True)
            print(f"✓ {package} downloaded successfully")
        except Exception as e:
            print(f"⚠️  Warning: Could not download {package}: {e}")
    
    print("\n✅ NLTK data download completed!")
    print("You can now run the chatbot.")

if __name__ == "__main__":
    download_nltk_data() 