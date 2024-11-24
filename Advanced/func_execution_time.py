import time

# Define the decorator
def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Call the function
        end_time = time.time()  # Record end time
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result  # Return the result of the function
    return wrapper

# Example usage of the decorator
@execution_time
def sumof(n):
    # Simulate a time-consuming function
    sum_ = 0
    for i in range(n):
        sum_ += i
    return sum_

# Call the function
sumof(1000000)
