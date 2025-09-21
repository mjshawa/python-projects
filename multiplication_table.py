# multiplication_table.py

# Get a number from the user.
number = int(input("Enter a number to generate its multiplication table: "))

# Use a for loop to iterate from 1 to 10 without including 11
print(f"\nMultiplication table for {number}:")
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
