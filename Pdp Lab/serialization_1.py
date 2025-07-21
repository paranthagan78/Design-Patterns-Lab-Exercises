from getpass import getpass
import re
import pickle
import sys
from datetime import datetime
import json


class User:
    """Represents a user with a username and password."""

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password


def check_password_strength(password):
    """
    Check if the password meets certain strength criteria.

    Args:
        password (str): The password to be checked.

    Returns:
        bool: True if the password is strong, False otherwise.
    """
    password_pattern = "^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$%^&*-]).{8,}$"
    if re.match(password_pattern, password):
        return True
    return False


def serialize_user(user: User):
    """
    Serialize and store a user object in a file.

    Args:
        user (User): The user object to be stored.
    """
    with open("users.pickle", "ab") as users_file:
        pickle.dump(user, users_file)


def check_credentials(username, password):
    """
    Check if the provided username and password match a registered user.

    Args:
        username (str): The username to be checked.
        password (str): The password to be checked.

    Returns:
        bool: True if the credentials are valid, False otherwise.
    """
    with open("users.pickle", "rb") as users_reader:
        while True:
            try:
                user = pickle.load(users_reader)
            except EOFError:
                return False
            if user.username == username and user.password == password:
                return True
            else:
                continue


def deserialize_users():
    """
    Deserialize and yield user objects from a file.

    Yields:
        User: A user object.
    """
    with open("users.pickle", "rb") as users_reader:
        while True:
            try:
                user = pickle.load(users_reader)
            except EOFError:
                return False
            yield user.username


def jsonify(message_str):
    """
    Serialize and store chat messages in a JSON file.

    Args:
        message_str (dict): Dictionary of chat messages.
    """
    try:
        with open("messages.json", "r") as file:
            chat_data = json.load(file)
    except FileNotFoundError:
        chat_data = {}

    for username, messages in message_str.items():
        if username in chat_data:
            chat_data[username].extend(messages)
        else:
            chat_data[username] = messages

    with open("messages.json", "w") as message_writer:
        json.dump(chat_data, message_writer, indent=4)


def display_messages(chat_data):
    """
    Display chat messages for the current user.

    Args:
        chat_data (dict): Dictionary of chat messages.
    """
    username = ChatApp.current_user

    if username in chat_data:
        messages = chat_data[username]
        print(f"Messages for {username}")
        for message in messages:
            timestamp = message["timestamp"]
            message_text = message["message"]
            status = "Sent:\t\t" if message["type"] == "sent" else "Received:\t"
            if message.get("to"):
                display_name = f"To {message.get('to')}"
            else:
                display_name = f"From {message.get('from')}"
            print(f"{status}{timestamp} - {display_name}: {message_text}")
    else:
        print(f"No messages found for {username}")


def search_messages(chat_data, content):
    """
    Search for messages containing a specific phrase.

    Args:
        chat_data (dict): Dictionary of chat messages.
        content (str): The phrase to search for.

    Returns:
        list: List of matching messages.
    """
    matching_messages = []
    messages = chat_data[ChatApp.current_user]
    for message in messages:
        if content in message["message"]:
            matching_messages.append(message)
    return matching_messages


class ChatApp:
    """A simple chat application."""

    usernames = []
    current_user = None

    def __init__(self):
        """Initialize the chat application."""
        user_db = open("users.pickle", "ab")
        user_db.close()
        ChatApp.usernames = list(deserialize_users())

    def add_user(self):
        """
        Create a new user and store their credentials.

        Returns:
            bool: True if the user is created successfully, False otherwise.
        """
        username = input("Please enter a username: ")
        print(
            "Note that your password contains minimum 8 characters and contain atleast\n"
            "1 uppercase character, 1 lowercase character,\n"
            "1 digit and 1 special character."
        )
        password = getpass("Please enter a password: ")
        re_password = getpass("Please re-enter your password: ")

        if password != re_password:
            print("Passwords are not the same!")
            return False
        elif username in ChatApp.usernames:
            print("Username already exists!")
            return False
        else:
            if not check_password_strength(password):
                print("Password is not strong enough!")
                return False
            else:
                user = User(username, password)
                ChatApp.usernames.append(user.username)
                serialize_user(user)
                return True

    def login(self):
        """
        Log in with a username and password.

        Returns:
            bool: True if the user is logged in successfully, False otherwise.
        """
        if ChatApp.current_user is not None:
            print("User already logged in! Please log out before logging in!")
            return False

        username = input("Please enter the username: ")
        password = getpass("Please enter the password: ")

        if username not in ChatApp.usernames:
            print("Invalid credentials! User not registered.")
            return False
        else:
            is_valid = check_credentials(username, password)
            if not is_valid:
                print("Invalid credentials!")
                return False
            else:
                ChatApp.current_user = username
                return True

    def send_message(self, user_choice, message_content):
        """
        Send a message to another user.

        Args:
            user_choice (int): Index of the user to send the message to.
            message_content (str): The message to be sent.
        """
        time_stamp = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")

        sender = ChatApp.current_user
        receiver = ChatApp.usernames[user_choice]

        message = {}

        message[sender] = []
        message[receiver] = []

        contents_send = {
            "message": message_content,
            "timestamp": time_stamp,
            "to": receiver,
            "type": "sent",
        }

        contents_rec = {
            "message": message_content,
            "timestamp": time_stamp,
            "from": sender,
            "type": "received",
        }

        message[sender].append(contents_send)

        message[receiver].append(contents_rec)

        jsonify(message)

    def display_all_messages(self):
        """Display all chat messages for the current user."""
        try:
            with open("messages.json", "r") as file:
                chat_data = json.load(file)
        except FileNotFoundError:
            chat_data = {}

        display_messages(chat_data)

    def search_message(self):
        """
        Search for messages containing a specific phrase and display the results.
        """
        if chatapp.current_user is None:
            print("You have not logged in! Log in first.")
            return

        search_phrase = input("Enter the message phrase to search: ")
        try:
            with open("messages.json", "r") as file:
                chat_data = json.load(file)
        except FileNotFoundError:
            chat_data = {}

        messages = search_messages(chat_data, content=search_phrase)

        if messages:
            for message in messages:
                timestamp = message["timestamp"]
                message_text = message["message"]
                status = "Sent:\t\t" if message["type"] == "sent" else "Received:\t"
                if message.get("to"):
                    display_name = f"To {message.get('to')}"
                else:
                    display_name = f"From {message.get('from')}"
                print(f"{status}{timestamp} - {display_name}: {message_text}")
        else:
            print("No messages found!")

    def log_out(self):
        """Log out the current user."""
        ChatApp.current_user = None

    def exit(self):
        """Exit the chat application."""
        ChatApp.current_user = None
        sys.exit(0)


if __name__ == "__main__":
    chatapp = ChatApp()
    while True:
        print("=" * 26)
        print("1. Create a user")
        print("2. Login")
        print("3. Chat")
        print("4. Display messages")
        print("5. Log out")
        print("6. Search for a message")
        print("7. Exit")

        ch = input("Enter your choice:").strip()

        if ch == "1":
            chk = chatapp.add_user()
            if chk:
                print("User created successfully!")
            else:
                continue

        elif ch == "2":
            chk = chatapp.login()

            if chk:
                print("User logged in successfully!")
                print(f"Current User: {chatapp.current_user}")
            else:
                continue

        elif ch == "3":
            if chatapp.current_user is None:
                print("You have not logged in! Log in first.")
                continue

            print("Choose the user you want to chat with:")
            for idx, user in enumerate(ChatApp.usernames):
                print(idx + 1, "\t", user)

            chat_choice = int(input("Enter the choice: "))

            if not ((chat_choice >= 1) and (chat_choice <= len(ChatApp.usernames))):
                print("Please enter the correct choice!")
                continue

            message_content = input("Please provide the message to be sent: ")

            chatapp.send_message(chat_choice - 1, message_content)

        elif ch == "4":
            if chatapp.current_user is None:
                print("You have not logged in! Log in first.")
                continue

            chatapp.display_all_messages()

        elif ch == "5":
            chatapp.log_out()
            print("Logged out successfully.")

        elif ch == "6":
            if chatapp.current_user is None:
                print("You have not logged in! Log in first.")
                continue

            chatapp.search_message()

        elif ch == "7":
            print("Exiting...")
            chatapp.exit()
