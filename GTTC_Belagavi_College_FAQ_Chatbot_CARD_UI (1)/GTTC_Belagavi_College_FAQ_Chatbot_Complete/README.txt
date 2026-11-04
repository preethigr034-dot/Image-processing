GTTC BELAGAVI COLLEGE FAQ CHATBOT — COMPLETE LAB PROJECT

FILES
- chatbot.py              -> Python NLP program required for the lab
- index.html              -> Advanced ChatGPT-style interface
- styles.css              -> UI styling
- app.js                  -> Browser NLP logic + FAQ knowledge base
- faq_dataset.csv         -> Sample dataset
- PROJECT_REPORT.md       -> Report content
- PRESENTATION_8_SLIDES.md -> 8-slide presentation
- README.txt              -> This guide

RUN THE ADVANCED GUI
1. Extract the ZIP.
2. Open the project folder.
3. Double-click index.html.
OR:
   python -m http.server 8000
   Then open http://localhost:8000

RUN THE PYTHON NLP PROGRAM
Open PowerShell in the project folder:
   python chatbot.py

Then type:
   What courses are available at GTTC Belagavi?
   Tell me about AIML.
   How can I get admission?
   What is the fee structure?
   What are the college working hours?
   exit

The Python program prints:
- original tokens
- tokens after stopword removal
- detected intent
- confidence
- sentiment
- predefined answer

PROJECT REQUIREMENTS COVERED
✓ Definition
✓ Problem statement
✓ Objectives
✓ Input/data
✓ Expected output
✓ Sample input/output
✓ Project flow
✓ Tokenization
✓ Stopword handling
✓ Pattern matching
✓ Predefined responses
✓ Unknown-question fallback
✓ Sentiment
✓ Python program
✓ Dataset
✓ GUI
✓ Report
✓ 8-slide presentation
✓ Demonstration-ready interface

IMPORTANT
The chatbot is a student NLP/rule-based system, not a real ChatGPT model.
The official GTTC page is linked inside the project. Verify current live
information before final submission.

Placement questions are answered directly using the GTTC placement knowledge base.

UPDATED CARD-STYLE FAQ UI
-------------------------
The chatbot now displays rich option cards instead of short one-line answers for major FAQ categories.
- Courses: 4 diploma cards with duration, semester fee and intake.
- Fees: course-wise fee cards.
- Short-term training: CNC, CMM, AutoCAD, SolidWorks, CATIA and CAD-CAM cards.
- Timings: Monday-Friday, Saturday and Sunday schedule cards.
- AIML: dedicated AI & ML diploma card.
- Principal: principal profile card.
- Placements: company cards plus GTTC alumni entrepreneur cards.

Run:
1. Open PowerShell in this folder.
2. Run: python -m http.server 8000
3. Open: http://localhost:8000
