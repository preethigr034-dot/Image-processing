"""
GTTC Belagavi College FAQ Chatbot
IP / NLP Lab - 3rd Project

Required techniques:
1. Tokenization
2. Stopword handling
3. Keyword / Regex pattern matching
4. Predefined FAQ responses
5. Optional positive / negative / neutral sentiment
"""

import re
from typing import Dict, List, Tuple

STOPWORDS = {
    "a","an","the","is","are","was","were","to","of","for","in","on","at",
    "do","does","did","can","could","would","what","when","where","how",
    "why","please","tell","me","about","my","our","your","i","we","you",
    "and","or","from","with","this","that"
}

POSITIVE = {"good","great","excellent","thanks","thank","happy","nice","helpful","awesome"}
NEGATIVE = {"bad","poor","wrong","confused","sad","problem","difficult","not"}

FAQS = [
    {
        "intent": "timings",
        "patterns": [r"\bworking hours?\b", r"\bcollege timings?\b", r"\bcollege time\b", r"\bcollage time\b", r"\bwhen.*college.*start\b", r"\bwhen.*college.*close\b",
                     r"\bwhen.*college.*open\b", r"\bwhen.*college.*close\b"],
        "answer": "GTTC Belagavi college working hours are generally 9:00 AM to 5:00 PM, Monday to Friday. Saturday may have a half-day or special schedule, and Sunday is usually a holiday."
    },
    {
        "intent": "departments",
        "patterns": [r"\bdepartments?\b", r"\bbranches?\b", r"\bstreams?\b", r"\bwhat.*courses?\b",
                     r"\bcourses?\b"],
        "answer": "GTTC Belagavi lists long-term diploma programmes in Tool & Die Making, Precision Manufacturing, Automation & Robotics, and Artificial Intelligence & Machine Learning."
    },
    {
        "intent": "aiml",
        "patterns": [r"\baiml\b", r"\bartificial intelligence\b", r"\bmachine learning\b"],
        "answer": "GTTC Belagavi lists a Diploma in Artificial Intelligence and Machine Learning as a long-term programme."
    },
    {
        "intent": "admission",
        "patterns": [r"\badmission\b", r"\bhow.*admission\b", r"\badmission.*process\b",
                     r"\bjoin.*college\b", r"\bapply\b", r"\beligib"],
        "answer": "For admission, students should check the current admission notification for eligibility, application dates and required documents."
    },
    {
        "intent": "fees",
        "patterns": [r"\bfees?\b", r"\bfee structure\b", r"\bcost\b", r"\bprice\b",
                     r"\bsemester fee\b", r"\btuition\b"],
        "answer": "The fee depends on the programme and admission year. The chatbot can provide the available fee information when it is added to the FAQ database."
    },
    {
        "intent": "contact",
        "patterns": [r"\bcontact\b", r"\bphone\b", r"\btelephone\b", r"\bcall\b",
                     r"\bmobile\b", r"\bemail\b"],
        "answer": "You can contact GTTC Belagavi through its college office for admission, course and student enquiries. Current contact details can be added to this chatbot database."
    },
    {
        "intent": "website",
        "patterns": [r"\bwebsite\b", r"\bofficial site\b", r"\bweb site\b", r"\blink\b"],
        "answer": "The official GTTC Belagavi website is available at gttc.karnataka.gov.in/9/belgaum/en."
    },
    {
        "intent": "library",
        "patterns": [r"\blibrary\b", r"\blibrary.*time\b"],
        "answer": "The GTTC Belagavi library is available for students for study and reference. Library timings may follow the college working schedule."
    },
    {
        "intent": "exam",
        "patterns": [r"\bexam\b", r"\bexamination\b", r"\btest\b", r"\binternal assessment\b"],
        "answer": "Exam and internal assessment dates are announced by the concerned department. The exact date is added to the chatbot when the department publishes the schedule."
    },
    {
        "intent": "short_term",
        "patterns": [r"\bshort[- ]term\b", r"\bshort term course\b", r"\bcnc\b", r"\bcmm\b",
                     r"\bautocad\b", r"\bsolid works\b", r"\bcatia\b", r"\bcad[- ]cam\b"],
        "answer": "GTTC Belagavi offers short-term training in areas such as CNC, CMM, AutoCAD, Solid Works, CATIA and CAD-CAM."
    },
    {
        "intent": "principal",
        "patterns": [r"\bprincipal\b", r"\bprinciple\b", r"\bhead of (the )?college\b", r"\bhead of (the )?institution\b", r"\bwho.*principal\b"],
        "answer": "The Principal of GTTC Belagavi, Belagavi is Shri Yallappa Savadatti Sir."
    },
    {
        "intent": "location",
        "patterns": [r"\baddress\b", r"\blocation\b", r"\bwhere.*college\b", r"\bwhere.*gttc\b",
                     r"\budyambag\b", r"\bbelagavi\b", r"\bbelgaum\b"],
        "answer": "GTTC Belagavi is located in the Udyambag industrial area of Belagavi, Karnataka."
    },
    {
        "intent": "placement",
        "patterns": [r"\bplacement\b", r"\bplacements\b", r"\bjob\b", r"\brecruit", r"\bcompany.*placement", r"\bplacement.*company", r"\bwhich.*companies", r"\bcompanies.*hire", r"\bcompanies.*recruit"],
        "answer": "GTTC provides placement opportunities for students after course completion. The official GTTC placement page lists companies/industries where students have been placed, including Dassult Systems, Goodrich Aerospace, Wipro, TCS, Infosys, IBM, Siemens, Allegro, Altair, QUEST, TATA Johnson Control, ITC InfoTech, Bosch, ASM, Cimatron, Volvo, Toyota Kirloskar, L&T, Schneider, Autoliv, Sansera, ABB, BEL, NAI, Black & Decker, Indo-MIN, PTC, Geometric Solutions, Mahindra, Emerson, RLE, TAFE, Rane Madras, Mastercraft, NASH Industries, Triveni Gears, Micro Plastics and Denso. The same official page also lists companies started by GTTC alumni, such as Spectrum Moulds, Incite Cam, Saras Mikrons, Camtech, Macro Precise, Accu Spark, 3D Precisions, Shashwathi, Precision Mould Tech, Techno Services, Shankar Tools, 3D Cad, Magna Tooling, Cadwin and Benaka Tooling."
    },
]

COURSE_OPTIONS = [
    ("Diploma in Tool and Die Making", "3+1 years • ₹13,750 per semester • Intake 60"),
    ("Diploma in Precision Manufacturing", "3+1 years • ₹13,750 per semester • Intake 30"),
    ("Diploma in Automation and Robotics", "3+1 years • ₹13,750 per semester • Intake 60"),
    ("Diploma in Artificial Intelligence and Machine Learning", "3+1 years • ₹13,750 per semester • Intake 60"),
]

SHORT_TERM_OPTIONS = [
    ("CNC Training", "Short-term skill training"),
    ("CMM Training", "Short-term skill training"),
    ("AutoCAD", "CAD design training"),
    ("SolidWorks", "3D CAD training"),
    ("CATIA", "CAD / product design training"),
    ("CAD-CAM", "Computer-aided design and manufacturing"),
]

PLACEMENT_COMPANIES = [
    "Dassult Systems", "Goodrich Aerospace", "Wipro", "TCS", "Infosys", "IBM",
    "Siemens", "Bosch", "Volvo", "Toyota Kirloskar", "L&T", "Schneider",
    "ABB", "Mahindra", "TAFE", "Denso"
]

ALUMNI_ENTREPRENEURS = [
    "Spectrum Moulds", "Incite Cam", "Saras Mikrons", "Camtech", "Macro Precise",
    "Accu Spark", "3D Precisions", "Shashwathi", "Precision Mould Tech",
    "Techno Services", "Shankar Tools", "3D Cad", "Magna Tooling", "Cadwin",
    "Benaka Tooling"
]

def tokenize(text: str) -> List[str]:
    return re.findall(r"[a-z0-9]+", text.lower())

def remove_stopwords(tokens: List[str]) -> List[str]:
    return [t for t in tokens if t not in STOPWORDS]

def preprocess(text: str) -> Tuple[List[str], List[str]]:
    tokens = tokenize(text)
    filtered = remove_stopwords(tokens)
    return tokens, filtered

def detect_sentiment(text: str) -> str:
    words = set(tokenize(text))
    pos = len(words & POSITIVE)
    neg = len(words & NEGATIVE)
    if pos > neg:
        return "Positive"
    if neg > pos:
        return "Negative"
    return "Neutral"

def classify(text: str) -> Tuple[str, float]:
    original = text.lower()
    _, filtered = preprocess(text)
    cleaned = " ".join(filtered)

    best_intent = "unknown"
    best_score = 0

    for item in FAQS:
        score = 0
        for pattern in item["patterns"]:
            if re.search(pattern, original) or re.search(pattern, cleaned):
                score += 1
        if score > best_score:
            best_score = score
            best_intent = item["intent"]

    confidence = min(0.98, 0.55 + best_score * 0.12) if best_score else 0.0
    return best_intent, confidence

def get_response(text: str) -> Dict:
    tokens, filtered = preprocess(text)
    intent, confidence = classify(text)

    answer = next((x["answer"] for x in FAQS if x["intent"] == intent), None)
    if not answer:
        answer = (
            "Sorry, I couldn't find an answer for that question. "
            "Try asking about timings, departments/courses, AIML, admission, "
            "fees, exams, library, short-term courses, contact, location, website, principal or placements."
        )

    return {
        "question": text,
        "tokens": tokens,
        "filtered_tokens": filtered,
        "intent": intent,
        "confidence": confidence,
        "sentiment": detect_sentiment(text),
        "answer": answer
    }

if __name__ == "__main__":
    print("=" * 60)
    print("GTTC BELAGAVI COLLEGE FAQ CHATBOT - NLP LAB")
    print("Type 'exit' to stop.")
    print("=" * 60)
    while True:
        q = input("\nStudent: ").strip()
        if q.lower() == "exit":
            break
        result = get_response(q)
        print("Bot:", result["answer"])

        if result["intent"] == "departments":
            print("\nDIPLOMA COURSES:")
            for title, meta in COURSE_OPTIONS:
                print(f"  • {title}\n    {meta}")
        elif result["intent"] == "short_term":
            print("\nSHORT-TERM TRAINING:")
            for title, meta in SHORT_TERM_OPTIONS:
                print(f"  • {title} — {meta}")
        elif result["intent"] == "placement":
            print("\nPLACEMENT COMPANIES:")
            print("  • " + ", ".join(PLACEMENT_COMPANIES))
            print("\nGTTC ALUMNI ENTREPRENEURS:")
            print("  • " + ", ".join(ALUMNI_ENTREPRENEURS))
        elif result["intent"] == "timings":
            print("\nCOLLEGE SCHEDULE:")
            print("  • Monday–Friday — 9:00 AM–5:00 PM")
            print("  • Saturday — Half-day / special schedule")
            print("  • Sunday — Usually a holiday")

        print(f"NLP -> intent={result['intent']} | confidence={result['confidence']:.0%} | sentiment={result['sentiment']}")
        print("Tokens:", result["tokens"])
        print("After stopword removal:", result["filtered_tokens"])
