# GTTC BELAGAVI COLLEGE FAQ CHATBOT
## IP / NLP Lab – 3rd Project

### 1. Definition
A text-based College FAQ Chatbot that answers frequently asked questions about GTTC Belagavi using basic Natural Language Processing, a small FAQ knowledge base and predefined responses.

### 2. Problem Statement
Develop a College FAQ Chatbot that accepts a student's question and provides an appropriate answer for common questions such as college timings, departments/courses, admission information, contact details and website. The system uses tokenization, stopword handling and simple keyword/pattern matching to recognize common questions.

### 3. Objectives
- Create a small FAQ knowledge base.
- Preprocess user questions.
- Recognize keywords/patterns in user input.
- Return an appropriate predefined answer.
- Detect simple positive/negative/neutral sentiment.
- Display basic NLP analysis for demonstration.

### 4. Input / Data Required
Questions typed by a student in a simple GUI/web interface. A CSV sample dataset is included.

### 5. Expected Output
- Chatbot response for recognized questions.
- Fallback message for unknown questions.
- Sentiment result.
- Intent and confidence.
- Tokenized and stopword-filtered text in the NLP analysis panel.

### 6. Sample Input
What are the college working hours?

### 7. Sample Expected Result
Chatbot: The college/office working time should be confirmed from the latest GTTC Belagavi timetable or office notice.

### 8. Project Flow
Input Text/Data
→ Preprocessing
→ Tokenization
→ Stopword Handling
→ NLP Technique / Regex & Pattern Matching
→ Intent Analysis
→ Predefined FAQ Response
→ Sentiment
→ Result
→ Display / Report

### 9. NLP Techniques Used
**Tokenization:** Splits the question into words using regular expressions.

**Stopword Handling:** Removes common words such as "the", "is", "what", "about", "to" and "for" so that important words receive more attention.

**Pattern Matching:** Uses keyword/regular-expression style rules to identify intents such as courses, admission, fees, contact and timings.

**Sentiment:** Counts simple positive and negative words and reports Positive, Negative or Neutral.

**Fallback:** If no known pattern matches, the chatbot gives a helpful fallback message.

### 10. System Modules
1. User Input Module
2. Preprocessing Module
3. Tokenization Module
4. Stopword Module
5. Intent / Pattern Matching Module
6. FAQ Knowledge Base
7. Response Module
8. Sentiment Module
9. GUI / Web Display Module
10. Source Verification Module

### 11. Testing
Test recognized questions, differently worded questions, unknown questions, positive feedback and negative feedback.

### 12. Result
The chatbot accepts student questions, preprocesses them, identifies common FAQ intents and displays predefined answers. The NLP analysis panel demonstrates tokenization, stopword handling, intent, confidence and sentiment.

### 13. Conclusion
The project demonstrates how basic NLP can be used to build a practical FAQ chatbot without requiring a large machine-learning model.

### 14. Future Scope
- Voice input and text-to-speech.
- Kannada/Hindi/English multilingual support.
- Larger database.
- Machine-learning intent classifier.
- Retrieval from live college notices.
- Secure LLM/API integration for more natural free-form answers.

### 15. Student Deliverables
- Python NLP program: `chatbot.py`
- Advanced GUI/web interface: `index.html`, `styles.css`, `app.js`
- Sample dataset: `faq_dataset.csv`
- Project report
- 8-slide presentation
- README and demonstration instructions

### Source
Official GTTC Belagavi centre page:
https://gttc.karnataka.gov.in/9/belgaum/en

Verify current admissions, fees, timetables and contact details before final submission.


## Added FAQ Coverage
The chatbot also includes direct responses for the Principal, college working hours, and placement information. The placement knowledge base uses the official GTTC “Placement and Entrepreneurs” page and includes the companies listed there, plus companies started by alumni. The chatbot answers these questions directly instead of forcing the student to open a website.
