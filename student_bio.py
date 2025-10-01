
# student_bio.py

def student_bio_formatter():
    #Formats and prints the bios for a list of students.
    
    # Store 5 students’ names, ages, and majors in a list of dictionaries.
    students = [
        {"name": "Moses", "age": 20, "major": "Computer Science"},
        {"name": "Shawa", "age": 21, "major": "Mechanical Engineering"},
        {"name": "Mj", "age": 19, "major": "Business Administration"},
        {"name": "Adee", "age": 22, "major": "Electrical Engineering"},
        {"name": "Margret", "age": 20, "major": "Graphic Design"},
    ]

    print("\n-- Student Bio Formatter --")
    
    # Format and print each student's info into a readable bio.
    for student in students:
        print(f"\nStudent Name: {student['name']}")
        print(f"Age: {student['age']}")
        print(f"Major: {student['major']}")

    print("\n------\n")

if __name__ == "__main__":
    student_bio_formatter()

