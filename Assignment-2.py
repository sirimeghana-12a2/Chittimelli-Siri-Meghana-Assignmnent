university_data = {
    "S101": {
        "name": "Alice Johnson",
        "major": "Computer Science",
        "courses": {
            "Python101": {"midterm": 88, "final": 92, "project": 94},
            "Math201": {"midterm": 78, "final": 85, "project": 80}
        }
    },
    "S102": {
        "name": "Bob Smith",
        "major": "Mathematics",
        "courses": {
            "Math201": {"midterm": 90, "final": 93, "project": 88},
            "Stats101": {"midterm": 84, "final": 80, "project": 85}
        }
    },
    "S103": {
        "name": "Clara Lopez",
        "major": "Physics",
        "courses": {
            "Physics101": {"midterm": 75, "final": 82, "project": 78},
            "Math201": {"midterm": 70, "final": 72, "project": 68}
        }
    }
}

#Print all student names and their majors
for student_id, student_info in university_data.items():
    print(f"Name: {student_info['name']}, Major: {student_info['major']}")
#Output
# Name: Alice Johnson, Major: Computer Science
# Name: Bob Smith, Major: Mathematics
# Name: Clara Lopez, Major: Physics

# Average score per course per student
for student in university_data.values():
    print(f"\nStudent: {student['name']}")
    for course, scores in student['courses'].items():
        avg_score = sum(scores.values()) / len(scores)
        print(f"  Course: {course}, Average Score: {avg_score:.2f}")
#Output
# Student: Alice Johnson
#   Course: Python101, Average Score: 91.33
#   Course: Math201, Average Score: 81.00
  
# Student: Bob Smith
#   Course: Math201, Average Score: 90.33
#   Course: Stats101, Average Score: 83.00

# Student: Clara Lopez
#   Course: Physics101, Average Score: 78.33
#   Course: Math201, Average Score: 70.00

#Find students who scored >90 in final of Python101
for student in university_data.values():
    if "Python101" in student["courses"]:
        if student["courses"]["Python101"]["final"] > 90:
            print(f"{student['name']} scored {student['courses']['Python101']['final']} in Python101 final.")
#Output
#Alice Johnson scored 92 in Python101 final.

#Add new course AI101 for student S101
university_data["S101"]["courses"]["AI101"] = {"midterm": 89, "final": 95, "project": 92}
print(university_data)
#Output
#{'S101': {'name': 'Alice Johnson', 'major': 'Computer Science', 'courses': {'Python101': {'midterm': 88, 'final': 92, 'project': 94}, 'Math201': {'midterm': 78, 'final': 85, 'project': 80}, 'AI101': {'midterm': 89, 'final': 95, 'project': 92}}}, 'S102': {'name': 'Bob Smith', 'major': 'Mathematics', 'courses': {'Math201': {'midterm': 90, 'final': 93, 'project': 88}, 'Stats101': {'midterm': 84, 'final': 80, 'project': 85}}}, 'S103': {'name': 'Clara Lopez', 'major': 'Physics', 'courses': {'Physics101': {'midterm': 75, 'final': 82, 'project': 78}, 'Math201': {'midterm': 70, 'final': 72, 'project': 68}}}}

#Print average for each course
course_totals = {}
course_counts = {}
for student in university_data.values():
    for course, scores in student["courses"].items():
        avg_score = sum(scores.values()) / len(scores)
        
        if course in course_totals:
            course_totals[course] += avg_score
            course_counts[course] += 1
        else:
            course_totals[course] = avg_score
            course_counts[course] = 1
for course in course_totals:
    overall_avg = course_totals[course] / course_counts[course]
    print(f"Course: {course}, Average Score: {overall_avg:.2f}")
#Output
#Course: Python101, Average Score: 91.33
# Course: Math201, Average Score: 80.44
# Course: AI101, Average Score: 92.00
# Course: Stats101, Average Score: 83.00
# Course: Physics101, Average Score: 78.33