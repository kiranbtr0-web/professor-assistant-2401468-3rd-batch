import random

print("Welcome to professor assistant version 1.0.")
name = input("Please Enter Your Name: ")
print(f"Hello Professor. {name}, I am here to help you create exams from a question bank.")

QUESTION_BANK_FILE = "queation_bank.txt"   # fixed file

while True:
    choice = input("Do you want me to help you create an exam (Yes to proceed | No to quit the program)? ").strip().lower()
    if choice != "yes":
        print(f"Thank you professor {name}. Have a good day!")
        break

    # Always load the fixed question bank
    try:
        with open(QUESTION_BANK_FILE, "r") as f:
            lines = f.read().strip().splitlines()
    except:
        print("Error: Could not open the question bank file.")
        break

    print("Question bank loaded successfully.")

    num = int(input("How many question-answer pairs do you want to include in your exam? ").strip())
    out_file = input("Where do you want to save your exam? ").strip()

    # Prepare question–answer pairs
    qa_pairs = []
    for i in range(0, len(lines), 2):
        if i + 1 < len(lines):
            qa_pairs.append((lines[i], lines[i + 1]))

    if num > len(qa_pairs):
        print("Not enough questions in the question bank. Try again.")
        continue

    selected = random.sample(qa_pairs, num)

    with open(out_file, "w") as f:
        for q, a in selected:
            f.write(q + "\n")
            f.write(a + "\n")

    print(f"Congratulations Professor {name}. Your exam is created and saved in {out_file}.")

    again = input("Do you want me to help you create another exam (Yes to proceed | No to quit the program)? ").strip().lower()
    if again != "yes":
        print(f"Thank you professor {name}. Have a good day!")
        break