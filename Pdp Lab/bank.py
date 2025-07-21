from abc import ABC
from abc import abstractmethod


class Loan(ABC):

    def __init__(self, loan_amount, account_type, location, borrower_details):

        self.borrower_details = borrower_details
        self.loan_amount = loan_amount
        self.account_type = account_type
        self.location = location

    @abstractmethod
    def calculate_interest(self):
        ...

    @abstractmethod
    def DisplayDetails(self):
        ...

    @abstractmethod
    def MonthlyPaymentInterest(self):
        ...

    @abstractmethod
    def MonthlyPaymentTotal(self):
        ...


class EducationLoan(Loan):
    
    def __init__(self, loan_amount, account_type, location, course_fee, borrower_details):

        super().__init__(loan_amount, account_type, location, borrower_details)
        self.course_fee = course_fee

    def calculate_interest(self):

        if self.location == "urban":
            location_factor = 1
        else:
            location_factor = 0.95

        if self.account_type == "Savings":
            account_type_factor = 1.05
        else:
            account_type_factor = 1
        
        base_interest_rate = 0.08
        return self.loan_amount * base_interest_rate * location_factor * account_type_factor

    def DisplayDetails(self):

        print(f"Borrower name is {self.borrower_details[0]}")
        print(f"Borrower age is {self.borrower_details[1]}")
        print(f"Borrower martial status is {self.borrower_details[2]}")
    
    def MonthlyPaymentInterest(self,years):
        
        interest = self.calculate_interest()
        return interest / (years * 12)
    
    def MonthlyPaymentTotal(self,years):

        interest_per_month = self.MonthlyPaymentInterest(years)
        loan_amt_per_month = self.loan_amount / (years * 12)
        return loan_amt_per_month + interest_per_month


class HomeLoan(Loan):

    def __init__(self, loan_amount, account_type, location, borrower_details):

        super().__init__(loan_amount, account_type, location, borrower_details)
    
    def calculate_interest(self):
    
        base_interest_rate = 0.06 
        location_factor = 1.02 if self.location == "urban" else 1.0 
        account_type_factor = 1.05 if self.account_type == "Savings" else 1.0 
        return self.loan_amount * base_interest_rate * location_factor * account_type_factor

    def DisplayDetails(self):

        print(f"Borrower name is {self.borrower_details[0]}")
        print(f"Borrower age is {self.borrower_details[1]}")
        print(f"Borrower martial status is {self.borrower_details[2]}")

    def MonthlyPaymentInterest(self,years):
        
        interest = self.calculate_interest()
        return interest / (years * 12)
    
    def MonthlyPaymentTotal(self,years):

        interest_per_month = self.MonthlyPaymentInterest(years)
        loan_amt_per_month = self.loan_amount / (years * 12)
        return loan_amt_per_month + interest_per_month


class PersonalLoan(Loan):

    def __init__(self, loan_amount, account_type, location, borrower_details):

        super().__init__(loan_amount, account_type, location, borrower_details)

    def calculate_interest(self):

        base_interest_rate = 0.1 
        location_factor = 1.05 if self.location == "urban" else 0.98
        account_type_factor = 1.08 if self.account_type == "Savings" else 1.0
        return self.loan_amount * base_interest_rate * location_factor * account_type_factor

    def DisplayDetails(self):

        print(f"Borrower name is {self.borrower_details[0]}")
        print(f"Borrower age is {self.borrower_details[1]}")
        print(f"Borrower martial status is {self.borrower_details[2]}")

    def MonthlyPaymentInterest(self,years):
        
        interest = self.calculate_interest()
        return interest / (years * 12)
    
    def MonthlyPaymentTotal(self,years):

        interest_per_month = self.MonthlyPaymentInterest(years)
        loan_amt_per_month = self.loan_amount / (years * 12)
        return loan_amt_per_month + interest_per_month


#driver code
if __name__ == '__main__':
    #The code provided here will not be executed when imported

    try:
        education_loan = EducationLoan(100000, "Savings", "urban", 8000, ["Ram",19,"Unmarried"])
        home_loan = HomeLoan(500000, "Current", "rural",["Vivek",50,"Married"])
        personal_loan = PersonalLoan(200000, "Savings", "urban",["Nikhil",28,"Married"])

        education_loan.DisplayDetails()
        print()

        home_loan.DisplayDetails()
        print()

        personal_loan.DisplayDetails()
        print()

        print(f"Education Loan Interest:{education_loan.calculate_interest()}")
        print()

        print(f"Home Loan Interest:{home_loan.calculate_interest()}")
        print()

        print(f"Personal Loan Interest:{personal_loan.calculate_interest()}")
        print()

        print(f"Education Loan Payment interest per month for 5 years : {education_loan.MonthlyPaymentInterest(5)}")
        print()

        print(f"Home Loan Payment interest per month for 5 years : {home_loan.MonthlyPaymentInterest(5)}")
        print()

        print(f"Personal Loan Interest per month for 5 years : {personal_loan.MonthlyPaymentInterest(5)}")
        print()

        print(f"Education Loan total payment per month for 5 years : {education_loan.MonthlyPaymentTotal(5)}")
        print()

        print(f"Home Loan total payment per month for 5 years : {home_loan.MonthlyPaymentTotal(5)}")
        print()

        print(f"Personal Loan total payment per month for 5 years : {personal_loan.MonthlyPaymentTotal(5)}")
        print()

    except Exception as e:
        print("Error:", str(e))
