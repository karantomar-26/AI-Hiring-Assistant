import streamlit as st
from prompts import generate_greeting, farewell_message
from utils import generate_questions, evaluate_answer
import json
import time

# Initialize session state
if "conversation_active" not in st.session_state:
    st.session_state.conversation_active = True
if "submitted_data" not in st.session_state:
    st.session_state.submitted_data = {}
if "questions" not in st.session_state:
    st.session_state.questions = []
if "current_question_index" not in st.session_state:
    st.session_state.current_question_index = 0
if "answers" not in st.session_state:
    st.session_state.answers = {}
if "current_answer" not in st.session_state:
    st.session_state.current_answer = ""

st.title("💼 TalentScout Hiring Assistant")

# Stage 1: Profile Form
if st.session_state.conversation_active and not st.session_state.questions:
    st.markdown(generate_greeting())

    with st.form("candidate_form"):
        full_name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.slider("Years of Experience", 0, 30, 1)
        position = st.text_input("Desired Position(s)")
        location = st.text_input("Current Location")
        tech_stack = st.text_area("Tech Stack (e.g., Python, Django, React, MySQL)")

        submitted = st.form_submit_button("Submit")

        if submitted:
            # Save profile data
            st.session_state.submitted_data = {
                "name": full_name,
                "email": email,
                "phone": phone,
                "experience": experience,
                "position": position,
                "location": location,
                "tech_stack": tech_stack
            }

            # Generate technical questions
            questions_text = generate_questions(tech_stack)

            # Extract only actual questions (lines starting with 1. 2. etc.)
            questions = []
            for line in questions_text.split("\n"):
                line = line.strip()
                if line.startswith("1.") or line.startswith("2.") or line.startswith("3.") or line.startswith("4.") or line.startswith("5."):
                    # Clean up leading "1. ", "2. " etc.
                    question_text = line[line.find(".")+1:].strip()
                    questions.append(question_text)

            # Save questions to session state
            st.session_state.questions = questions
            st.session_state.current_question_index = 0
            st.session_state.answers = {}
            st.session_state.current_answer = ""

# Stage 2: Question/Answer Loop
if st.session_state.questions:
    total_questions = len(st.session_state.questions)
    current_index = st.session_state.current_question_index

    if current_index < total_questions:
        question = st.session_state.questions[current_index]

        st.markdown(f"### Question {current_index + 1} of {total_questions}")
        st.write(question)

        # Show timer first
        timer_placeholder = st.empty()
        for seconds_left in range(10, 0, -1):  
            timer_placeholder.info(f"⏳ Time remaining: {seconds_left} seconds")
            time.sleep(1)
        timer_placeholder.empty()

        # Answer form
        with st.form("answer_form"):
            user_answer = st.text_area(
                "Your Answer", 
                value=st.session_state.current_answer, 
                key=f"answer_{current_index}"
            )
            submitted_answer = st.form_submit_button("Submit Answer")

            if submitted_answer:
                # Save answer
                st.session_state.answers[f"Question {current_index + 1}"] = {
                    "question": question,
                    "answer": user_answer
                }
                # Reset for next
                st.session_state.current_answer = ""
                st.session_state.current_question_index += 1

    else:
        # All questions answered → Save to JSON
        filename = f"{st.session_state.submitted_data['name']}_answers.json"
        evaluations = {}

        st.markdown("### 📝 Evaluating your answers...")

        # Evaluate each answer
        for q_key, q_data in st.session_state.answers.items():
            question = q_data["question"]
            answer = q_data["answer"]
            
            evaluation_text = evaluate_answer(question, answer)
            
            # Save evaluation
            evaluations[q_key] = {
                "question": question,
                "answer": answer,
                "evaluation": evaluation_text
            }
            
            # Also display on screen
            st.markdown(f"#### {q_key}")
            st.write(f"**Question:** {question}")
            st.write(f"**Your Answer:** {answer}")
            st.write("**Evaluation:**")
            st.write(evaluation_text)
            st.markdown("---")

        # Save everything to JSON
        data_to_save = {
            "candidate_info": st.session_state.submitted_data,
            "answers": st.session_state.answers,
            "evaluations": evaluations
        }

        with open(filename, "w") as f:
            json.dump(data_to_save, f, indent=4)

        st.success("✅ All questions completed and evaluated! Results saved.")
        st.write(f"Saved to `{filename}`.")

        st.markdown("---")
        st.success(farewell_message())

        # Reset session for next run
        st.session_state.conversation_active = False
