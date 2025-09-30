""" students = [
        ("Mjshawa", 23),
        ("Moses", 19),
        ("Sinai", 26),
        ("John", 22),
        ("Shawa", 25)
       ]

computer_science = {"Shawa", "Sinai", "Moses", "John"}

health_sciences = {"John", "Moses"}

print(" --- Majoring Analysis ---")


print("\n1. All students in all majors")
print(f" Computer Science students: {sorted(list(computer_science))"}
print(f" Health sciences majors: {sorted(list(healthy_sciences))"}



print("\n2. Common students (Intersection):")
print(f"  {sorted(list(common_students))}")

    print("\n3. Students Unique to Each Major (Difference):")
print(f"  Unique to Computer Science:  {sorted(list(unique_to_computer_science))}")
print(f"  Unique to Health Science: {sorted(list(unique_to_health_science))}")

print("\n--- Student Data (Tuples) ---")
print(f"  Student Data: {students}")
"""


# club_members.py

# 1. Store 5 students as tuples (name, age)
students = [
    ("Moses", 24),
    ("Mjshawa", 19),
    ("Sinai", 26),
    ("David", 20),
    ("Esther", 21)
]

# Extract only the names for the club sets, as the age is not needed for set operations
# and sets must contain immutable types.
# You could use the full tuples if you wanted, but it makes the output harder to read.
student_names = [student[0] for student in students]
# student_names is now: ['Alice', 'Bob', 'Charlie', 'David', 'Eve']

# 2. Create two sets representing different clubs.
# Club A: Science Club
computer_science = {"Moses", "Mjshawa", "David"}

# Club B: Debate Club
machanical_engineering = {"Sinai", "Mjshawa", "Esther", "Moses"}

print("--- Student Majoring Analysis ---")

## Perform set operations:

# 3. List all members of each club
print("\n## Students of Each Major")
print(f"Computer Science Students: {computer_science}")
print(f"Mechnical Engineering Students: {machanical_engineering}")

# 4. Find common members (Intersection)
common_students = computer_science.intersection(machanical_engineering)
print("\n## Common Students (Both Majors)")
print(f"The following studnets belong to BOTH Majors: {common_students}")

# 5. Find members unique to each club (Difference)

# Members ONLY in Club A (Science Club)
unique_to_computer_science = computer_science.difference(machanical_engineering)
# Alternatively: unique_to_club_a = club_a_members - club_b_members
print("\n## Students Unique to Each Major")
print(f"Students ONLY in Computer Science: {unique_to_computer_science}")

# Members ONLY in Club B (Debate Club)
unique_to_machanical_engineering = machanical_engineering.difference(computer_science)
# Alternatively: unique_to_club_b = club_b_members - club_a_members
print(f"Students ONLY in Machanical Engineering: {unique_to_machanical_engineering}")
