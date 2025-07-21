import re
import json
import pickle
from datetime import datetime

class UsernamePassword(Exception):
    pass

class Chat:
    user_word = {}
    user_name = r'^[A-z][a-z]{3,14}$'
    pass_word = r'^[A-z][a-z]{3,10}[@][1-9]{2,5}$'

    def __init__(self, U_name, pass_W):
        self.name = U_name
        self.pasW = pass_W
        self.user_word[self.name] = self.pasW
        print(self.user_word)
        try:
            if (re.match(self.user_name, self.name) and re.match(self.pass_word, self.pasW) and self.pasW == self.user_word[self.name]):
                print("Username and password are verified...")
                json_string = json.dumps({self.name: self.pasW}, indent=2)
                filepath = "C:/Users/marim/OneDrive/Documents/sem-3/DESIGN PATTERN/Madhusudhanan-UIT2311-ex-08/USER_password.json"
                with open(filepath, 'a') as file:
                    file.write(json_string)
            else:
                raise UsernamePassword
        except UsernamePassword:
            print("Invalid Username and password...")
            return

    def Create_chat(self):
        self.file_name = self.name + "file"

        with open(self.file_name, 'ab') as file:
            pickle.dump("username:" + self.name, file)
            receiver_name = input("Enter the receiver username: ")
            pickle.dump("receivername:" + receiver_name, file)
            pickle.dump(datetime.now(), file)
            no_of_line = 10
            while no_of_line > 0:
                Chat_ = input("Enter the chat here--")
                pickle.dump(Chat_, file)
                no_of_line -= 1

    def History(self):
        try:
            with open(self.file_name, 'rb') as file:
                while True:
                    load_data = pickle.load(file)
                    print(load_data)
        except FileNotFoundError:
            print(f"File {self.file_name} not found.")
        except EOFError:
            print("File ended")

    def search_string(self, search_text):
        try:
            with open(self.file_name, 'rb') as file:
                while True:
                    load_data = pickle.load(file)
                    if search_text in str(load_data):
                        print("String found:", load_data)
        except FileNotFoundError:
            print(f"File {self.file_name} not found.")
        except EOFError:
            print("End of file")

# Example usage:
chat_instance = Chat("JohnDoe", "Abc@12345")
chat_instance.Create_chat()
chat_instance.History()
search_text = input("Enter the string to search: ")
chat_instance.search_string(search_text)
