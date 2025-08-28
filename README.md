  Translation Tool 
Overview
A modern, responsive web-based translation tool that allows users to translate text between multiple languages. The application features a clean, intuitive interface with language detection, text-to-speech functionality, and copy-to-clipboard capabilities.

Features
Multi-language Support: Translate between 11 languages including English, Spanish, French, German, and more

Language Detection: Automatically detect the source language

Language Swapping: Quickly swap between source and target languages

Text-to-Speech: Listen to your translations

Copy to Clipboard: Easily copy translated text

Character Counter: Track input length with a 5000-character limit

Responsive Design: Works well on desktop and mobile devices

Status Notifications: Get feedback on translation progress and errors

Supported Languages
English (en)

Spanish (es)

French (fr)

German (de)

Italian (it)

Portuguese (pt)

Russian (ru)

Chinese (zh)

Japanese (ja)

Arabic (ar)

Hindi (hi)

Setup Instructions
Prerequisites
A modern web browser (Chrome, Firefox, Safari, Edge)

Internet connection for Google Translate API calls

A Google Cloud account with Translation API enabled (for production use)

Installation
Download or clone the project files

Open index.html in a web browser

For full functionality, add your Google Translate API key to the script.js file:

Replace 'YOUR_GOOGLE_TRANSLATE_API_KEY' with your actual API key

Alternatively, the app will use a simulated translation for demonstration purposes

Getting a Google Translate API Key
Go to the Google Cloud Console

Create a new project or select an existing one

Enable the Translation API

Create credentials (API key)

Copy the API key and paste it into the script.js file

Usage
Select the source language or choose "Detect Language"

Select the target language

Type or paste text into the source text area

Click the "Translate" button

View the translation in the target text area

Use additional features:

Click the swap button to exchange languages

Click the copy button to copy the translation

Click the speak button to hear the translation

File Structure
text
translation-tool/
│
├── index.html          # Main HTML file
├── styles.css          # CSS styling
├── script.js           # JavaScript functionality
└── README.md           # This file
Browser Compatibility
Chrome (recommended)

Firefox

Safari

Edge

Limitations
The demo version uses simulated translations without an API key

Text-to-speech functionality depends on browser support

Maximum character limit of 5000 per translation

Requires an internet connection for actual translations

Future Enhancements
Support for additional languages

Translation history

Favorite translations

File upload for translation

Dark mode theme

Offline translation capability

Troubleshooting
If translations fail, check your API key and internet connection

Ensure your browser supports Web Speech API for text-to-speech

Clear browser cache if experiencing display issues
