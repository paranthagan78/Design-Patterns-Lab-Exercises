# define a function
def test_sum_numbers():
    assert sum([100, 200, 300, 400]) == 1000, "Result should be 1000"

# define a function
def test_sum_tuple_values():
    assert sum((100, 200, 300, 400)) == 100, "Result should be 1000"

# Driver code
if __name__ == "__main__":
    # Call the test functions
    test_sum_numbers()
    test_sum_tuple_values()

    # If the code reaches this point, it means all tests passed
    print("All tests passed.")
