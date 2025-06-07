from utils import model

def generate_greeting():
    return "Hello! 👋 Welcome to TalentScout Hiring Assistant. I will help you with your interview screening."

def farewell_message():
    return "Thank you for your time! We will get back to you soon with the next steps. Good luck!"

def generate_technical_questions(tech_stack):
    prompt = f"""
    You are a technical interviewer. Generate 3 good technical questions for each of these technologies:
    {tech_stack}

    Keep questions clear and suitable for 1-3 years of experience.
    """

    response = model.generate_content(prompt)
    return response
