class Student:
    def __init__(self, name, cgpa):
        self.name = name
        self.cgpa = cgpa

def sort_students(student_list):
    # Sort the list of student objects based on CGPA in descending order
    sorted_students = sorted(student_list, key=lambda x: x.cgpa, reverse=True)
    return sorted_students

# Example usage:
students = [
    Student("Alice", 3.9),
    Student("Bob", 3.5),
    Student("Charlie", 4.0),
    Student("David", 3.7)
]

sorted_students = sort_students(students)

for student in sorted_students:
    print(f"Name: {student.name}, CGPA: {student.cgpa}")