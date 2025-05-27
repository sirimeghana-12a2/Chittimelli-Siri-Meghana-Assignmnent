# Build a student grade management system using the following Python concepts:
# - List of dictionaries
# - Function with required arguments, *args, **kwargs
# - Function decorator
# - Loops and control statements

# Requirements
# 1. Use a **decorator** to log function activity.
# 2. Use a function to **add student data** using `*args` and `**kwargs`.
# 3. Store student records in a **list of dictionaries**.
# 4. Use **loops and conditionals** to calculate and display results.

students = []
# Decorator to log function calls
def log_function(func):
    def wrapper(*args, **kwargs):
        print(f"Running function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Finished function: {func.__name__}\n")
        return result
    return wrapper

# Function to add student data
@log_function
def add_student(student_id, name, *subjects, **marks):
    student = {
        'id': student_id,
        'name': name,
        'subjects': subjects,
        'marks': marks
    }
    students.append(student)
    print(f"Added student: {name}")

# Function to calculate and show grades
@log_function
def show_results():
    for student in students:
        print(f"--- Result for {student['name']} ---")
        total = 0
        count = 0
        for sub in student['subjects']:
            mark = student['marks'].get(sub, 0)
            print(f"{sub}: {mark}")
            total += mark
            count += 1

        if count > 0:
            avg = total / count
            grade = get_grade(avg)
            print(f"Average: {avg:.2f} | Grade: {grade}")
        else:
            print("No subjects found.")

# Function to get grade based on average
def get_grade(avg):
    if avg >= 90:
        return 'A'
    elif avg >= 80:
        return 'B'
    elif avg >= 70:
        return 'C'
    elif avg >= 60:
        return 'D'
    else:
        return 'F'

add_student(1, "Alice", "Math", "Science", Math=85, Science=90)
add_student(2, "Bob", "English", "History", English=75, History=65)
add_student(3, "Charlie", "Math", Math=55)
show_results()
#Output
# Running function: add_student
# Added student: Alice
# Finished function: add_student

# Running function: add_student
# Added student: Bob
# Finished function: add_student

# Running function: add_student
# Added student: Charlie
# Finished function: add_student

# Running function: show_results
# --- Result for Alice ---
# Math: 85
# Science: 90
# Average: 87.50 | Grade: B
# --- Result for Bob ---
# English: 75
# History: 65
# Average: 70.00 | Grade: C
# --- Result for Charlie ---
# Math: 55
# Average: 55.00 | Grade: F
# Finished function: show_results