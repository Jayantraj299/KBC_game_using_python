import time
import json
import random

filename = 'qna_list.json'

# Read the file contents
with open(filename, 'r') as file:
    file_data = file.read()

# Parse the file contents as a dictionary
qna_list = json.loads(file_data)

# Randomly select a list from the loaded data
qna_list = random.choice(list(qna_list.values()))

# Loop through the list and ask the questions
for qna in qna_list:
    prize = qna["prize"]
    question = qna["question"]
    options = qna["options"]
    Answer = qna["Answer"]
    print("Here's a question for ₹",prize)
    print(question)
    
    # Print the Answer options
    letters = ['A', 'B', 'C', 'D']
    for i, option in enumerate(options):
        print(f"{letters[i]}. {option}")

    while True:
    # Get the user's answer
        user_answer = input("Enter your Answer (A-D): ")
        if user_answer.upper() in letters:
            index = letters.index(user_answer.upper())
            break
        else:
            print("Invalid input. Please enter a valid option (A-D).")


    # Check if the Answer is correct
    if options[index] == Answer:
        print("The correct answr is:"),time.sleep(3),print(user_answer.upper()+".",Answer)
        print("congratulations you have won",prize)
        print("Would you like to use your ₹",prize)
        if prize == "70,000,000":
            print("advut you have won: 7 crore")
            break
        choice = input("Do you want to continue(y/n):")
        if choice == "y":
            continue
        elif choice == "n":
            print("congratulations you are going home with ₹",prize)
            break   
    else:
        print("The correct answr is:"),time.sleep(3),print(user_answer.upper()+".",Answer)
        print("Sorry but Answer is incorrect")
        break
