# age_category.py
# Get the user's input, for name and age


name = input("Please enter your name: ")
age = int(input("Please enter your age: "))

# Check the age category using if-elif-else
if 0 <= age <= 12:
    category = "Child"
elif 13 <= age <= 19:
    category = "Teen"
elif 20 <= age <= 59:
    category = "Adult"
else:
    category = "Senior"

# Printes output format
print(f"\nName: {name}")
print(f"Age: {age}")
print(f"Category: {category}")
