import streamlit as st
import os

# Initialize page state
if "page" not in st.session_state:
    st.session_state.page = "Welcome"

def set_page(page_name):
    st.session_state.page = page_name

# ---------------- WELCOME PAGE ----------------
if st.session_state.page == "Welcome":
    st.title("🎓 SAT Study Companion")
    st.write("Welcome to your custom SAT prep platform! Choose an option below to get started.")
    st.write("")
    
    if st.button("📚 Math Test", use_container_width=True):
        set_page("Math Test")
        st.rerun()

    st.write("")

    if st.button("💬 Feedback", use_container_width=True):
        set_page("Feedback")
        st.rerun()

# ---------------- MATH TEST PAGE ----------------
elif st.session_state.page == "Math Test":
    st.title("📚 SAT Math Practice")
    
    questions = [
        {
            "id": "q1",
            "question": "1. If 3x + 7 = 22, what is the value of 6x - 4?",
            "options": ["15", "26", "30", "34"],
            "answer": "26",
            "explanation": "3x = 15 -> x = 5 -> 6(5) - 4 = 26"
        },
        {
            "id": "q2",
            "question": "2. What is the slope of the line given by the equation 4x - 2y = 8?",
            "options": ["-2", "2", "4", "8"],
            "answer": "2",
            "explanation": "Convert to slope-intercept form (y = mx + b): -2y = -4x + 8 -> y = 2x - 4. Slope = 2."
        },
        {
            "id": "q3",
            "question": "3. If a rectangle has a length of 12 and a perimeter of 34, what is its width?",
            "options": ["5", "10", "11", "22"],
            "answer": "5",
            "explanation": "Perimeter = 2(length + width) -> 34 = 2(12 + width) -> 17 = 12 + width -> width = 5."
        }
    ]

    with st.form("math_quiz_form"):
        user_answers = {}
        
        for q in questions:
            st.subheader(q["question"])
            user_answers[q["id"]] = st.radio("Select an answer:", q["options"], key=q["id"])
            st.write("---")
            
        submitted = st.form_submit_button("Submit Test")

    if submitted:
        score = 0
        for q in questions:
            user_ans = user_answers[q["id"]]
            if user_ans == q["answer"]:
                score += 1
                st.success(f"*{q['question']}*\n\nCorrect! 🎉 ({q['explanation']})")
            else:
                st.error(f"*{q['question']}\n\nIncorrect. Correct answer: *{q['answer']}** ({q['explanation']})")
        
        st.info(f"### Your Final Score: {score} / {len(questions)}")

    st.write("---")
    if st.button("⬅️ Back to Home"):
        set_page("Welcome")
        st.rerun()

# ---------------- FEEDBACK PAGE ----------------
elif st.session_state.page == "Feedback":
    st.title("💬 Feedback & Suggestions")
    st.write("We'd love to hear your thoughts to make this study app better!")
    
    user_feedback = st.text_area("Leave your feedback or feature requests here:")
    
    if st.button("Submit Feedback"):
        if user_feedback.strip():
            # Save feedback to a text file on your system
            with open("feedback.txt", "a", encoding="utf-8") as f:
                f.write(user_feedback.strip() + "\n---\n")
            st.success("Thank you for your feedback! 🙌")
        else:
            st.warning("Please type a message before submitting.")

    st.write("---")

    # View Submissions Section
    with st.expander("👀 View Submitted Feedback"):
        if os.path.exists("feedback.txt"):
            with open("feedback.txt", "r", encoding="utf-8") as f:
                feedback_data = f.read()
            if feedback_data.strip():
                st.text_area("All Received Feedback:", value=feedback_data, height=200, disabled=True)
            else:
                st.info("No feedback has been submitted yet.")
        else:
            st.info("No feedback has been submitted yet.")

    st.write("---")
    if st.button("⬅️ Back to Home"):
        set_page("Welcome")
        st.rerun()
