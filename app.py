import streamlit as st
import random

st.set_page_config(page_title="WAEC Math Generator", layout="centered")

st.title("📘 WAEC Math Question Generator")
st.write("Generate WAEC-style math questions with answers and explanations.")

# Select topic
topic = st.selectbox("Choose a topic:", ["Algebra", "Quadratic Equations"])

def generate_algebra():
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    question = f"Solve for x: {a}x + {b} = 0"
    answer = -b / a
    explanation = f"Subtract {b} from both sides and divide by {a}."
    return question, answer, explanation

def generate_quadratic():
    a = random.randint(1, 5)
    b = random.randint(1, 10)
    c = random.randint(1, 10)

    question = f"Solve: {a}x² + {b}x + {c} = 0"

    discriminant = b**2 - 4*a*c
    explanation = f"Use the quadratic formula. Discriminant = {discriminant}"

    return question, "Solve using quadratic formula", explanation

if st.button("Generate Question"):
    if topic == "Algebra":
        q, a, e = generate_algebra()
    else:
        q, a, e = generate_quadratic()

    st.subheader("📌 Question")
    st.write(q)

    st.subheader("✅ Answer")
    st.write(a)

    st.subheader("🧠 Explanation")
    st.write(e)
