
# Day 15 Task: Student Data Organizer

#File: student_data.py

# student_data.py

def calculate_grade(mark):
    """Assigns a letter grade based on the student's mark."""
    if mark >= 90:
        return 'A'
    elif mark >= 80:
        return 'B'
    elif mark >= 70:
        return 'C'
    elif mark >= 60:
        return 'D'
    else:
        return 'F'

def student_data_organizer():
    #Stores student data, calculates grades, and prints a formatted report.
    
    # 1. Store 5 students' data in a list of dictionaries
    students = [
        {"name": "Aliness", "age": 20, "marks": 95},
        {"name": "Albert", "age": 21, "marks": 82},
        {"name": "Charlie", "age": 19, "marks": 67},
        {"name": "Daniel", "age": 22, "marks": 40},
        {"name": "Memory", "age": 20, "marks": 89},
    ] 

    print("\n Student Data Organizer Report")
    
    # 2. Iterate, calculate grade, add to dictionary, and print report
    for student in students:
        mark = student["marks"]
        grade = calculate_grade(mark)
        
        # Add the grade to the student dictionary
        student["grade"] = grade
        
        # Print a formatted report
        print(f"{student['name']}: Age {student['age']}, Marks {mark} – Grade: {grade}")

    print("----------------\n")

if __name__ == "__main__":
    student_data_organizer()
