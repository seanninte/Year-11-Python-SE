import random

# Counter keeps track of how many times a question is answered
# Score keeps track of how many times the user got the correct answer
Counter = 0
Score = 0

# List of valid operators user can use in quiz
valid_operations = ['+', '-', 'x']

# Asks user to choose operation, if valid operators (+,-,x) are inputted the function will break
# If input is not a valid operator it will ask for input again
def ChooseOperation():
    while True:
        global operation
        # Asks user to choose valid operator
        operation = input(f"Choose operation (+, -, x): ")
        if operation not in valid_operations:
            print("That is not an operation. Please choose valid operator")
        elif operation == '+':
            break
        elif operation == '-':
            break
        elif operation == 'x':
            break

def Question():
    # Counter and Score are changed into a global variable so it can be changed in the function
    global Counter
    global Score
    # Chooses random number within number ranges
    number1 = random.randint(1, 100)
    number2 = random.randint(1, 100)
    multiply_num1 = random.randint(1, 12)
    multiply_num2 = random.randint(1, 12)
    # Asks question using random numbers and inputted operation
    if operation == "+" or operation == "-":
        print(f"What is {number1} {operation} {number2}? ")
    elif operation == "x":
        print(f"What is {multiply_num1} {operation} {multiply_num2}? ")
    # Asks for user input
    user_answer = int(input(''))
    # Depending on the inputted operation, answer differs
    if operation == '+':
        answer = number1 + number2
    elif operation == '-':
        answer = number1 - number2
    elif operation == 'x':
        answer = multiply_num1 * multiply_num2
    # When answer is correct, adds point to counter and score
    if user_answer == answer:
        print("Correct!")
        Counter += 1
        Score += 1
    # When answer is incorrect, only adds point to counter
    elif user_answer != answer:
        print(f"Incorrect. The correct answer is: {answer}")
        Counter += 1
    else:
        print(f"Incorrect. The correct answer is: {answer}")
        Counter += 1


def DisplayScore(Score, Counter):
    print(f"You got {Score} out of {Counter}")
    score_percentage = Score/Counter * 100
    # Creates percentage of how much the user got correct
    if score_percentage >= 90:
        grade = "A"
    elif score_percentage >= 70:
        grade = "B"
    elif score_percentage >= 50:
        grade = "C"
    elif score_percentage >= 30:
        grade = "D"
    elif score_percentage >= 10:
        grade = "E"
    elif score_percentage == 0:
        grade = "F"
    # Displays quiz grade based on score percentage
    print(f"{score_percentage}%, Your Grade: {grade}")


print("Welcome to the Math Quiz!")
ChooseOperation()
while Counter != 5:
    Question()

DisplayScore(Score, Counter)

# I got 31/40 for this. LETS GOOOOOOOOO