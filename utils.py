import os
from dotenv import load_dotenv
import streamlit as st
# LangChain
from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()



# Load API key safely (works both local and Streamlit Cloud)
cohere_api_key = os.getenv("COHERE_API_KEY") or st.secrets["COHERE_API_KEY"]


# Initialize LangChain ChatCohere model
class CohereClient:
    def __init__(self, api_key):
        self.model = ChatCohere(cohere_api_key=api_key, model_name="command-r-plus")  # or "command-r"

    def generate_content(self, prompt):
        chat_prompt = ChatPromptTemplate.from_template("{prompt}")
        messages = chat_prompt.format_messages(prompt=prompt)
        response = self.model.invoke(messages)
        return response.content

model = CohereClient(cohere_api_key)

# Helper function
def generate_questions(tech_stack):
    prompt = f"""
    You are a technical interviewer. Generate 3-5 technical questions for each technology listed:
    {tech_stack}

    Keep questions clear and suitable for candidates with 1-3 years experience.
    """

    return model.generate_content(prompt)


def evaluate_answer(question, answer):
    prompt = f"""
    You are a technical interviewer.

    Evaluate the following candidate answer to the question provided.

    Question: {question}

    Candidate Answer: {answer}

    Please provide:
    - A score out of 10
    - A short feedback (1-2 sentences)

    Format your response like this:

    Score: X/10
    Feedback: <your feedback here>
    """

    return model.generate_content(prompt)
