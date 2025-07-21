"""
Write a python program to develop a simple calculator program in Python. Users 
can enter two numbers and select an operation (addition, subtraction, 
multiplication, or division). Implement the following exception handling to ensure 
that the calculator behaves gracefully even when users provide incorrect input:
1. If operation is not one of the valid operations mentioned above, raise a 
ValueError with the message "Invalid operation. Please choose from 'add,' 
'subtract,' 'multiply,' or 'divide.'"
2. If the operation is "divide" and the num2 is zero, raise a ZeroDivisionError 
with the message "Division by zero is not allowed."
3. If either num1 or num2 is not a number (i.e., not an int or float), raise a 
TypeError with the message "Both numbers must be integers or floats."
Handle the exceptions raised by the function and display appropriate error 
messages. If the calculation is successful, display the result

"""

class Calculator:
    
        def add(self,a,b):
            c=a+b
            return f"Addition of {a} and {b} is {c}"
        
        def subract(self,a,b):
            d=a-b
            return f"Subraction of {a} and {b} is {d}"

        def multiply(self,a,b):
            e=a*b
            return f"Multiplication of {a} and {b} is {e}"

        def divide(self,a,b):
            if b==0:
                raise ZeroDivisionError("Division by Zero is not Allowed")
            else:
                f=a/b
            return f"Division of {a} and {b} is {f}"

c=Calculator()

a=input("Enter Number1: ")
b=input("Enter Number2: ")

try:
    a=float(a)
    b=float(b) 
    operation=input("Enter Operation: (Add, Sub, Mul, Div): ")

    if not ((isinstance(a ,int) or isinstance(b ,float)) and (isinstance(a ,float) or isinstance(b ,int))):
        raise TypeError("Both a and b must be Integer or Float")
    
    if operation=="Add":
        print(c.add(a,b))
    elif operation=="Sub":
        print(c.subract(a,b))
    elif operation=="Mul":
        print(c.multiply(a,b))
    elif operation=="Div":
        print(c.divide(a,b))
    else:
        raise ValueError("Invalid Operation, Please Enter Valid Operation like (Add, Sub, Mul, Div)")

except (ZeroDivisionError,ValueError,TypeError) as error:
    print(error)
    