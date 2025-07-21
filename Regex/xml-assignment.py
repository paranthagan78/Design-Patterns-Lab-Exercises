# import xml.etree.ElementTree as ET

# class Student:
#     def __init__(self, name, roll, marks):
#         self.name = name
#         self.roll = roll
#         self.marks = marks

# def serialize_students(students, filename):
#     root = ET.Element("students")
#     for student in students:
#         student_element = ET.Element("student")
#         name_element = ET.Element("name")
#         name_element.text = student.name
#         roll_element = ET.Element("roll")
#         roll_element.text = str(student.roll)
#         marks_element = ET.Element("marks")
#         marks_element.text = str(student.marks)
#         student_element.append(name_element)
#         student_element.append(roll_element)
#         student_element.append(marks_element)
#         root.append(student_element)
#     tree = ET.ElementTree(root)
#     with open(filename, "wb") as f:
#         tree.write(f)

# def deserialize_students(filename):
#     students = []
#     tree = ET.parse(filename)
#     root = tree.getroot()
#     for student_element in root.findall("student"):
#         name = student_element.find("name").text
#         roll = int(student_element.find("roll").text)
#         marks = float(student_element.find("marks").text)
#         students.append(Student(name, roll, marks))
#     return students

# class Teacher:
#     def __init__(self, students_filename):
#         self.students = deserialize_students(students_filename)

#     def sort_students_by_rank(self):
#         self.students.sort(key=lambda student: student.marks, reverse=True)

#     def display_ranked_students(self):
#         print("Rank  Name        Roll  Marks")
#         for rank, student in enumerate(self.students, start=1):
#             print(f"{rank:4d}  {student.name:10s}  {student.roll:4d}  {student.marks:.2f}")

# if __name__ == "__main__":
#     student1 = Student("Alice", 101, 95.5)
#     student2 = Student("Bob", 102, 88.0)
#     student3 = Student("Charlie", 103, 92.5)
#     student4 = Student("David", 104, 78.0)
#     student5 = Student("Eve", 105, 99.0)

#     students = [student1, student2, student3, student4, student5]

#     serialize_students(students, "students.xml")

#     teacher = Teacher("students.xml")
#     teacher.sort_students_by_rank()
#     teacher.display_ranked_students()


from xml_marshaller import  xml_marshaller

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

class Teacher:
    def sort_students_by_marks(students):
        return sorted(students, key=lambda student: student.marks, reverse=True)

if __name__ == '__main':
    # Serialize students to XML
    students = [
        Student("Alice", 85),
        Student("Bob", 92),
        Student("Charlie", 78)
    ]

    # Serialize students to XML string
    students_xml = xml_marshaller.dumps(students)

    # Deserialize students from XML string
    students = xml_marshaller.loads(students_xml, Student)

    # Use Teacher class to sort students by marks
    teacher = Teacher()
    sorted_students = teacher.sort_students_by_marks(students)

    for student in sorted_students:
        print(f"Name: {student.name}, Marks: {student.marks}")