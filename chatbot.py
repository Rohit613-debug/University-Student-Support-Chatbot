
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Example student questions and corresponding responses.
knowledge_base = [
    {
        "questions": [
            "hello",
            "hi",
            "hey",
            "good morning",
            "can you help me"
        ],
        "answer": (
            "Hello! I can assist with academic deadlines, "
            "course registration, financial aid, academic "
            "advising, library services, and IT support."
        )
    },
    {
        "questions": [
            "how do I check assignment deadlines",
            "when is my assignment due",
            "where can I find my course deadlines",
            "how do I see my academic calendar",
            "when should I submit my homework"
        ],
        "answer": (
            "Check your course assignments page or calendar "
            "in your learning management system (LMS). "
            "For official dates, consult your university's "
            "academic calendar."
        )
    },
    {
        "questions": [
            "how do I contact my academic advisor",
            "where can I find academic advising",
            "how can I get course planning help",
            "I need help choosing classes",
            "how do I schedule an advising appointment"
        ],
        "answer": (
            "Contact your assigned academic advisor or "
            "the university academic advising office. "
            "You can usually find advising information "
            "through your official student portal."
        )
    },
    {
        "questions": [
            "how do I apply for financial aid",
            "where can I find scholarships",
            "how do I pay my tuition",
            "I need help with university fees",
            "where can I get student financial assistance"
        ],
        "answer": (
            "For financial aid, tuition, and scholarships, "
            "visit your university's financial aid office "
            "or student portal. Check the official website "
            "for application requirements and deadlines."
        )
    },
    {
        "questions": [
            "how do I register for classes",
            "where can I enroll in courses",
            "how can I complete course registration",
            "how do I add a course",
            "how do I sign up for classes"
        ],
        "answer": (
            "Sign in to your student portal and open the "
            "course registration section. Confirm course "
            "requirements and availability with your "
            "academic advisor when necessary."
        )
    },
    {
        "questions": [
            "how do I reset my password",
            "I cannot log into my student account",
            "I forgot my student portal password",
            "where can I get technical support",
            "my university login is not working"
        ],
        "answer": (
            "For password, login, and technical issues, "
            "contact your university's IT help desk. "
            "Use the official password reset service "
            "provided by your institution."
        )
    },
    {
        "questions": [
            "where is the university library",
            "how do I access library resources",
            "where can I find research articles",
            "how do I borrow library books",
            "how can I access academic journals"
        ],
        "answer": (
            "Visit your university library website for "
            "academic databases, research articles, "
            "books, and citation support. Contact "
            "library staff for additional assistance."
        )
    },
    {
        "questions": [
            "where can I get student support",
            "how do I contact student services",
            "what support services are available",
            "where can I find university assistance",
            "how do I get help as a student"
        ],
        "answer": (
            "University support services may include "
            "academic advising, counseling, financial "
            "aid, library assistance, and IT support. "
            "Visit the official university website "
            "for contact information."
        )
    }
]


# Prepare example questions for machine learning.
example_questions = []
answers = []

for item in knowledge_base:
    for question in item["questions"]:
        example_questions.append(question)
        answers.append(item["answer"])


# Convert example questions into numerical representations.
vectorizer = TfidfVectorizer(
    lowercase=True,
    stop_words="english",
    ngram_range=(1, 2)
)

question_vectors = vectorizer.fit_transform(example_questions)


def get_response(message):
    """Find the closest matching university support answer."""

    if not isinstance(message, str) or not message.strip():
        return "Please enter a question so I can help you."

    # Convert the student's question into a TF-IDF vector.
    user_vector = vectorizer.transform([message])

    # Compare it against the example questions.
    similarities = cosine_similarity(
        user_vector,
        question_vectors
    )[0]

    best_match_index = similarities.argmax()
    best_score = similarities[best_match_index]

    # Avoid guessing when the question is not recognized.
    if best_score < 0.25:
        return (
            "I'm sorry, I couldn't confidently identify "
            "your question. Please ask about deadlines, "
            "registration, advising, financial aid, "
            "technical support, or library services. "
            "For other questions, contact your university's "
            "student support office."
        )

    return answers[best_match_index]
