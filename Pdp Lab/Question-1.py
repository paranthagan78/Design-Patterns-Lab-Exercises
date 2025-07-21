"""
Name:M.Madhusudhanan
Reg no:3122225002067
"""

class Course:
    def __init__(self,course_code,course_name,credit_hours, *args,**kwargs):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours
        self.additional_args = args
        self.additional_kwargs = kwargs
    def add_info(self):
        self.course_code = input("enter the course_code : ")
        self.course_name = input("enter the course_name: ")
        self.credit_hours = int(input("enter the credit_hours: "))
        self.additional_args = input("any additional info: ")
        self.additional_kwargs = input("any additional kwags: ")
    def display_info(self):
        print(f"Course_code:{self.course_code}")
        print(f"couse_name:{self.course_name}")
        print(f"credit_hours:{self.credit_hours}")
        if self.additional_args:
            print(f"additional_args:{self.additional_args}")

        
class Corecourse(Course):
    def __init__(self,*args,**kwargs):
        
        super().__init__(*args,**kwargs)
    def add_info(self):
        super().add_info()
        self.required_prerequistes = input("prerequistes: ")
    def display_info(self):
        print(f"required_prerequistes={self.required_prerequistes}")
        super().display_info()
class Elective(Course):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    def add_info(self):
        super().add_info()
        self.available_terms_property = input("enter the lab properties: ")

    def display_info(self):
        super().display_info()
        print(f"available terms:{self.available_terms_property}")
class Labcourses(Course):
    def __init__(self,*args,**kwargs):
        
        super().__init__(*args,**kwargs)
    def add_info(self):
        super().add_info()
        self.lab_location = input("enter the lab location: ")

    
    
    def display_info(self):
        super().display_info()
        print(f"lab_location:{self.lab_location}")
# Create instances of CoreCourse, Elective, and Labcourses
# Create instances of CoreCourse, Elective, and Labcourses
core_course = Corecourse("CS100", "CS101", 3, required_prerequisites="CS100")
elective_course = Elective(["Fall", "Spring"], "MATH201", 4, available_terms_property="Fall only")
lab_course = Labcourses("Lab Building 2", "CHEM301", 2, lab_location="Lab A")

# Add information to each course
core_course.add_info()
elective_course.add_info()
lab_course.add_info()

# Display course information
print("\nCore Course Information:")
core_course.display_info()
print("\nElective Course Information:")
elective_course.display_info()
print("\nLab Course Information:")
lab_course.display_info()
