#sequences of lowercase letters joined by an underscore
import re
def text_match(text):
        patterns = '^[a-z]+_[a-z]+$'
        if re.search(patterns,  text):
                return 'Found match!'
        else:
                return('Not matched!')

print(text_match("aab_cbbb"))
print(text_match("aab_Abbbc"))
print(text_match("Aaab_abbbc"))





def login(org_user,org_pass):
        username=r"[A-Za-z]"
        password=r"[A-Za-z]+[!@#$$]+[0-9]"
        if re.search(username,org_user):
            if re.search(password,org_pass):
                return 'User is correct!'
        return('User is not correct!')

print(login(org_user="paranthgan",org_pass="Paran@1234"))





#matches a string that has an a followed by zero or more b's
import re
def text_match(text):
        patterns = '^a(b*)$'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')
print(text_match("ac"))
print(text_match("abc"))
print(text_match("a"))
print(text_match("ab"))
print(text_match("abb"))




#program that matches a word containing 'z'
import re
def text_match(text):
        patterns = '\w+z.\w*'
        if re.search(patterns,  text):
                return 'Found a match!'
        else:
                return('Not matched!')

print(text_match("The quick brown fox jumps over the lazy dog."))
print(text_match("Python Exercises."))





#program to remove leading zeros from an IP address
import re
ip = "216.008.094.196"
string = re.sub('\.[0]+', '.', ip)
print(string)




#to check that a string contains only a certain set of characters 
#(in this case a-z, A-Z and 0-9)
import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9]')
    string = charRe.search(string)
    return not bool(string)

print(is_allowed_specific_char("ABCDEFabcdef123450")) 
print(is_allowed_specific_char("*&%@#!}{"))
print(is_allowed_specific_char("Aaaaaaaaaa")) 
print(is_allowed_specific_char("aaaaaaaaaa")) 


class A:
    def show(self):
        print("Class A")


class B(A):
    def show(self):
        print("Class B")


class C(A):
    def show(self):
        print("Class C")


class D(B, C):
    pass


# Create an instance of D
obj = D()

# Call the show method
print(obj.show())
