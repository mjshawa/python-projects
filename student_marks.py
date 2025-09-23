# student_marks.py

# Store student names and their marks in two lists
names = ["Alice", "Bob", "Charlie", "David", "Eve"]
marks = [85, 92, 78, 88, 95]

# Calculate the average marks
total_marks = sum(marks)
average_marks = total_marks / len(marks)

# Print the summary table header
print("Student Marks Summary")
print("---------------------")

# Iterate through the lists to print each student's summary
for i in range(len(names)):
    name = names[i]
    mark = marks[i]
    
    # Assign grades using if-elif-else
    if mark >= 90:
        grade = "A"
    elif mark >= 80:
        grade = "B"
    elif mark >= 70:
        grade = "C"
    elif mark >= 60:
        grade = "D"
    else:
        grade = "F"
    
    # Print the student's details
    print(f"{name}: {mark} – Grade {grade}")

# Print the average marks at the end
print("---------------------")
print(f"Average marks: {average_marks:.1f}")
