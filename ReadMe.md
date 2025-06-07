# AI Hiring Assistant

An AI-powered hiring assistant built with Streamlit, Cohere (LLM), and LangChain, designed to conduct technical screening interviews.

The app:

   - Collects candidate details  
   - Generates technical questions based on the candidate's tech stack  
   - Displays questions one by one with a countdown timer  
   - Collects candidate answers  
   - Automatically evaluates answers using an LLM  
   - Saves the full report to a JSON file  
   - Provides a friendly, conversational experience for the candidate  

---

## Live Demo

[Deployed App on Streamlit Cloud](https://ai-hiring-assistantt.streamlit.app/)

---

## Screenshots

### Home / Candidate Form

<!-- Place a screenshot of the initial form here -->
![Candidate Form Screenshot](screenshots\candidate_form.png)


---

### Question Screen with Timer

<!-- Place a screenshot of a question being shown with the timer -->
![Question Screen Screenshot](screenshots\question_screen.png)

---

### Evaluation Screen

<!-- Place a screenshot of the final evaluation / results -->
![Evaluation Screen Screenshot](screenshots\answer_eval_1.png)

---

## Architecture

Streamlit App
|
|--> Collect Candidate Info
|
|--> Generate Questions (via Cohere LLM + LangChain)
|
|--> Display Questions one by one + Timer
|
|--> Collect Answers
|
|--> Evaluate Answers (via Cohere LLM + LangChain)
|
|--> Save results as JSON
|
|--> Display Final Evaluation


Features:

   - Candidate profile form
   - Dynamic technical questions
   - Per-question timer
   - Answer collection
   - Automated evaluation
   - Save answers and evaluations as JSON
   - Friendly conversational flow
   - Ready for deployment on Streamlit Cloud

Future Improvements:

   - Add more question types (MCQ, coding, etc.)
   - Store results to a database (SQLite, Supabase, Firebase)
   - Add recruiter login panel
   - Support for multi-round interviews
   - Email the candidate a report after interview

Acknowledgments:
   
   - OpenAI / Google Gemini API / Cohere LLM APIs
   - Streamlit team
   - LangChain team
   - Inspiration from various AI HR tools



Author
Karan Tomar
GitHub → https://github.com/karantomar-26