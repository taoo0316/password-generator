
QUESTIONS = [
    ("Where does Wentao go to school", "Yale-NUS College"),
    ("How old is Wentao", "22"),
    ("What is Wentao's major in college", " Computer Science"),
]

for question, correct_answer in QUESTIONS:
    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Correct!")
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")
