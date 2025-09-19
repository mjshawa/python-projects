# grade_evaluator.py

name = input("Enter your name: ")

try:
    score = int(input("Enter your score (0-100): "))

    # Using of if-elif-else to determine the grade
    if 90 <= score <= 100:
        grade = 'A'
    elif 80 <= score <= 89:
        grade = 'B'
    elif 70 <= score <= 79:
        grade = 'C'
    elif 60 <= score <= 69:
        grade = 'D'
    elif 0 <= score < 60:
        grade = 'F'
    else:
        grade = "Invalid Score"
    
    # Print the result
    print(f"\nStudent: {name}")
    print(f"Score: {score}")
    print(f"Grade: {grade}")

except ValueError:
    print("Invalid input. Please enter a valid number for the score.")
