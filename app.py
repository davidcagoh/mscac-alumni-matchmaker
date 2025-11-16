import streamlit as st
from matcher import match_student   # your retrieval code

st.set_page_config(page_title="MScAC Alumni Matchmaker", layout="centered")

st.title("MScAC Alumni Matchmaker")
st.write("Ask a question. We'll match you with a relevant alum based on past MScAC projects.")

# --- Form ---
with st.form("student_form"):

    student_name = st.text_input("Your name *", max_chars=100)
    student_type = st.text_input("Your status *", value="1st Year MScAC Student", max_chars=100)

    headline = st.text_input("Short headline *", max_chars=100)

    background = st.text_area(
        "Briefly introduce yourself *",
        max_chars=500,
        height=80,
        help="Share your background or interests."
    )

    request = st.text_area(
        "What do you need help with? *",
        max_chars=2000,
        height=150,
        help="Describe what advice, perspective, or help you're seeking."
    )

    closing = st.text_area(
        "Close nicely *",
        max_chars=250,
        height=60,
        help="e.g., 'Looking forward to hearing from you!'"
    )

    commit = st.checkbox("I commit to thanking each alum who responds to my question. *")

    submitted = st.form_submit_button("Submit")

# --- On submit ---
if submitted:
    if not (student_name and student_type and headline and background and request and closing and commit):
        st.error("Please fill in all required fields and check the commitment box.")
    else:
        student_input = {
            "student_name": student_name,
            "student_type": student_type,
            "headline": headline,
            "background": background,
            "request": request,
            "closing": closing
        }

        st.subheader("🔎 Best Matches")
        matches, email = match_student(student_input)

        for m in matches:
            meta = m["meta"]
            st.write(
                f"**{meta.get('student', 'Unknown')}** "
                f"(Cohort {meta.get('cohort', '?')}) — "
                f"{m['title']} at *{meta.get('partner', 'Unknown')}*"
            )

        st.subheader("📧 Email to Alumni")
        st.code(email, language="text")