import random

def generate_algebra_question():
    a = random.randint(1, 10)
    b = random.randint(1, 10)

    question = f"Solve for x: {a}x + {b} = 0"
    answer = -b / a

    explanation = f"Subtract {b} from both sides and divide by {a}."

    return question, answer, explanation
  
def generate_questions(n=5):
    questions = []
    for _ in range(n):
        q, a, e = generate_algebra_question()
        questions.append((q, a, e))
    return questions

if __name__ == "__main__":
    qs = generate_questions()

    for i, (q, a, e) in enumerate(qs, 1):
        print(f"{i}. {q}")
        print(f"Answer: {a}")
        print(f"Explanation: {e}\n")
