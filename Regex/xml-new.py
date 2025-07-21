import xml.etree.ElementTree as ET
from xml_marshaller import xml_marshaller 
class Student:
    def __init__(self, name, roll, marks):
        self.name = name
        self.roll = roll
        self.marks = marks

def serialize_students(students, filename):
    root = ET.Element("students")
    for student in students:
        student_element = ET.SubElement(root, "student")
        ET.SubElement(student_element, "name").text = student.name
        ET.SubElement(student_element, "roll").text = str(student.roll)
        ET.SubElement(student_element, "marks").text = str(student.marks)
    tree = ET.ElementTree(root)
    tree.write(filename)

def deserialize_students(filename):
    tree = ET.parse(filename)
    return [Student(
        student.find("name").text,
        int(student.find("roll").text),
        float(student.find("marks").text)
    ) for student in tree.getroot()]

class Teacher:
    def __init__(self, students_filename):
        self.students = deserialize_students(students_filename)

    def sort_students_by_rank(self):
        self.students.sort(key=lambda student: student.marks, reverse=True)

    def display_ranked_students(self):
        print("Rank  Name        Roll  Marks")
        for rank, student in enumerate(self.students, start=1):
            print(f"{rank:4d}  {student.name:10s}  {student.roll:4d}  {student.marks:.2f}")

if __name__ == "__main__":
    students = [
        Student("Alice", 101, 95.5),
        Student("Bob", 102, 88.0),
        Student("Charlie", 103, 92.5),
        Student("David", 104, 78.0),
        Student("Eve", 105, 99.0)
    ]

    serialize_students(students, "students.xml")

    teacher = Teacher("students.xml")
    teacher.sort_students_by_rank()
    teacher.display_ranked_students()
