# grade_calculator.py

def calculate_grade(mark):
    """
    Calculates and returns the letter grade for a given mark.
    """
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

# Store student names and their marks in two lists
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
marks = [95, 82, 67, 74, 89]

# Use a for loop to print each student's grade
for i in range(len(names)):
    name = names[i]
    mark = marks[i]
    grade = calculate_grade(mark)  # Call the function to get the grade
    print(f"{name}: {mark} – Grade {grade}")
