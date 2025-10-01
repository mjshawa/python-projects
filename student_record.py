# student_record.py
DATA_FILE = "records.txt"

def add_student(name, age, major):
    """Appends student data (name, age, major) to the records file."""
    try:
        # Open file in append mode ('a')
        with open(DATA_FILE, 'a') as f:
            # Format data as a comma-separated string followed by a newline
            f.write(f"{name},{age},{major}\n")
        print(f"✅ Added student: {name}")
    except Exception as e:
        print(f"❌ Error adding student: {e}")

def view_students():
    """Displays all student records stored in the file."""
    try:
        # Open file in read mode ('r')
        with open(DATA_FILE, 'r') as f:
            records = f.readlines()
            
            if not records:
                print("No student records found.")
                return

            print("\n--- Day 18: Student Records ---")
            for record in records:
                # Remove newline and split the string by comma
                data = record.strip().split(',')
                if len(data) == 3:
                    name, age, major = data
                    print(f"Student Name: {name:<15} | Age: {age:<3} | Major: {major}")
            print("-------------------------------\n")

    except FileNotFoundError:
        print(f"❌ The data file '{DATA_FILE}' was not found. Please add students first.")
    except Exception as e:
        print(f"❌ An unexpected error occurred while viewing records: {e}")

def student_record_manager():
    """Main function to run the record manager and test functions."""
    print("--- Running Student Record Manager ---")

    # Clear file before adding new data for a clean test run
    # NOTE: In a real app, you'd check if the file exists first.
    open(DATA_FILE, 'w').close() 
    
    # Add at least 5 students
    add_student("Grace", 23, "Chemistry")
    add_student("Henry", 20, "Physics")
    add_student("Irene", 21, "Literature")
    add_student("Jack", 24, "Finance")
    add_student("Karen", 19, "Biology")

    # View all students
    view_students()

if __name__ == "__main__":
    student_record_manager()
