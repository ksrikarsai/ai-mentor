import random
import nltk
from nltk.tokenize import sent_tokenize

# Sample questions for Socratic questioning
follow_up_questions = [
    "Why do you think that?",
    "Can you explain your reasoning further?",
    "What if we changed a condition in this problem?",
    "How would you approach it differently?",
    "Can you give a real-world example?",
    "What are the possible limitations of your answer?"
]

def ai_mentor_response(student_answer):
    """Simulates an AI mentor asking follow-up questions."""
    sentences = sent_tokenize(student_answer)
    if sentences:
        return random.choice(follow_up_questions)
    return "Can you elaborate on your thought process?"

# Simulating interaction
print("AI Mentor: What is your answer to the question?")
student_input = input("You: ")
ai_response = ai_mentor_response(student_input)
print(f"AI Mentor: {ai_response}")
