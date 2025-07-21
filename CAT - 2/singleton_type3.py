class Singleton1:

  instance = None

  def __init__(self):
    if Singleton1.instance is not None:
       raise Exception("Singleton object already created!")
    else:
       Singleton1.instance = self

s3=Singleton1()
print(s3)


class Singleton:

    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

# Example Usage:

s1 = Singleton()
print(s1)

s2 = Singleton()
print(s2)

print(s1 is s2)  # Output: True (both references point to the same instance)


class LoginPage:

    _instance = None
    _logged_in_user = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoginPage, cls).__new__(cls)
            # Additional initialization can be done here if needed
        return cls._instance

    def login(self, username, password):
        # Simulating login logic
        if not self._logged_in_user:
            # Check username and password (this is a simplistic example)
            if username == "example_user" and password == "example_password":
                self._logged_in_user = username
                print(f"User '{username}' logged in successfully.")
            else:
                print("Login failed. Invalid username or password.")
        else:
            print("Already logged in. Please log out first.")

    def logout(self):
        if self._logged_in_user:
            print(f"User {self._logged_in_user} logged out.")
            self._logged_in_user = None
        else:
            print("Not logged in. Cannot log out.")

# Example Usage:

# Creating instances of LoginPage
login_page1 = LoginPage()
login_page2 = LoginPage()

# Attempting to log in with valid credentials
login_page1.login("example_user", "example_password")

# Attempting to log in again (should print a message that the user is already logged in)
login_page2.login("example_user", "example_password")

# Logging out
login_page1.logout()

# Logging out again (should print a message that the user is not logged in)
login_page2.logout()
