class Login:
    _instance=None
    _logged_in_user=None
    def __new__(cls):
        if cls._instance is None:
            cls._instance=super(Login,cls).__new__(cls)
        return cls._instance
    def logged_in(self,user,password):
        if not self._logged_in_user:
            if user=="Paran" and password==1234:
                self._logged_in_user=user
                print(f"{user} logged in")
            else:
                print("Login failed. Invalid username or password.")
        else:
            print(f"{user} already logged in")

l1=Login()
l2=Login()
l1.logged_in("Paran",1234)
l2.logged_in("Paran",1234)



import re

class Login:
    _instance = None
    _logged_in_user = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Login, cls).__new__(cls)
        return cls._instance

    def logged_in(self, user, password):
        if not self._logged_in_user:
            if user == "Paran" and re.match(r'\d', password):
                self._logged_in_user = user
                print(f"{user} logged in")
            else:
                print("Login failed. Invalid username or password.")
        else:
            print(f"{user} already logged in")

# Example usage
l1 = Login()
l2 = Login()

l1.logged_in("Paran", "1234")  # This will succeed
l2.logged_in("Paran", "password")  # This will fail due to an invalid password



import re
import unittest

class Login:
    _instance = None
    _logged_in_user = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Login, cls).__new__(cls)
        return cls._instance

    def logged_in(self, user, password):
        if self._logged_in_user:
            # Reset logged-in user if someone else tries to log in
            self._logged_in_user = None

        if not self._logged_in_user:
            if user == "Paran" and re.match(r'\d', password):
                self._logged_in_user = user
                return f"{user} logged in"
            else:
                return "Login failed. Invalid username or password."
        else:
            return f"{user} already logged in"

class TestLogin(unittest.TestCase):

    def setUp(self):
        self.l1 = Login()
        self.l2 = Login()

    def test_login_successful(self):
        result = self.l1.logged_in("Paran", "1234")
        self.assertEqual(result, "Paran logged in")


if __name__ == '__main__':
    unittest.main()
