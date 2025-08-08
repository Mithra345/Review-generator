# Product Review Generator

## Overview
The **Product Review Generator** is a Streamlit-based application that uses GPT to automatically generate product reviews for e-commerce products based on user input. It allows users to customize tone, length, and style of reviews.

## Features
- Generate AI-based product reviews.
- Choose tone: Positive, Neutral, Negative.
- Choose review length: Short, Medium, Long.
- Supports text preprocessing (NLTK).
- Interactive web interface via Streamlit.

## Installation
1. Clone the repository:
   ```bash
   git clone <your-repo-url>
   ```
2. Navigate to the project folder:
   ```bash
   cd <project-folder>
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the app:
   ```bash
   streamlit run app.py
   ```
2. Open the URL displayed in the terminal (usually http://localhost:8501).

## Project Structure
```
├── app.py               # Main Streamlit application
├── requirements.txt     # Python dependencies
└── README.md            # Project documentation
```

## Dependencies
- Python 3.10+
- Streamlit
- OpenAI API
- NLTK

## License
This project is licensed under the MIT License.
