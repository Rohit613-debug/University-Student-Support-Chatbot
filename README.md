
# University Student Support Chatbot

## Project Description

The University Student Support Chatbot is a web-based
application designed to help university students access
common academic and administrative information.

It provides guidance on assignment deadlines, academic
advising, course registration, financial aid, library
services, and technical support.

## Technologies Used

- Python
- Flask
- HTML
- CSS
- JavaScript
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity

## System Requirements

- Windows, macOS, or Linux
- Python 3.14 (tested with Python 3.14.2)
- Internet connection for the initial dependency installation
- A modern web browser

## Installation Instructions

1. Download or clone this project.
2. Open the project folder in Visual Studio Code.
3. Open a terminal in the main project folder.

4. Create a Python virtual environment:

   python -m venv .venv

5. Activate the environment on Windows CMD:

   .venv\Scripts\activate.bat

   On macOS or Linux:

   source .venv/bin/activate

6. Install the dependencies:

   python -m pip install -r requirements.txt

7. Start the application:

   python app.py

8. Open the browser and visit:

   http://127.0.0.1:5000

## How to Use the Chatbot

1. Open the chatbot webpage.
2. Enter a question into the text field.
3. Click Send or press Enter.
4. Read the chatbot's response.
5. Continue asking questions as needed.

## Example Questions

- How do I register for classes?
- How do I reset my password?
- Where can I find scholarships?
- How do I contact my academic advisor?
- When is my assignment due?
- How do I access library resources?

## How the Chatbot Works

The chatbot uses TF-IDF vectorization and cosine
similarity to compare a student's question with
predefined example questions.

The system selects the closest matching question
and returns its associated answer when the
similarity score reaches the configured threshold.

When no suitable match is identified, the chatbot
returns a fallback response.

## Project Structure

app.py - Flask application and API routes

chatbot.py - Question matching and response logic

requirements.txt - Python dependencies

templates/index.html - Chatbot webpage

static/style.css - User interface styling

static/script.js - Browser interaction logic

## Limitations

- The chatbot uses a predefined knowledge base.
- It does not generate new answers using a large language model.
- It cannot access private student information.
- It does not retrieve live university deadlines.
- Its answers should be verified using official university resources.
- Some differently worded questions may produce incorrect matches.

## Testing

The application was tested locally using questions
about deadlines, registration, financial aid,
technical support, and library services.

Testing also included unrelated questions to
evaluate the fallback response.

## Security

This application is a local academic prototype.
It does not require API keys or student credentials.

The Flask development server is not intended
for production deployment.

## Academic Use and Credits

This project was developed for the
University of the Cumberlands
Artificial Intelligence for Human-Computer Interaction
course (MSAI-631).

ChatGPT was used to assist with code development,
debugging, explanations, and documentation.

The team reviewed, adapted, and tested the code.
Further information about software libraries
and reused-code credits is provided separately.
