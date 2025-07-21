# Define a family of algorithms
class Amazon:
    def sales_operation(self, year):
        pass

# Implement concrete strategies
class Diwali_Sales(Amazon):
    def sales_operation(self, year):
        return f"Diwali sales of 50% in {year}"

class Thanksgiving_Sales(Amazon):
    def sales_operation(self, year):
        return f"TG sales of 10% in {year}"

# Context class that uses a strategy
class Sales:
    def __init__(self, sales):
        self.sales = sales

    def execute_sales(self, year):
        return self.sales.sales_operation(year)

# Example usage
year= 2023

# Use Diwali strategy
diwali_sales = Diwali_Sales()
sales = Sales(diwali_sales)
result = sales.execute_sales(year)
print(f"Sales: {result}")

# Use Thanksgiving strategy
tg_sales = Thanksgiving_Sales()
sales = Sales(tg_sales)
result = sales.execute_sales(year)
print(f"Sales: {result}")

