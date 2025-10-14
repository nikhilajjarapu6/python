# Basic decorator that prints before and after function execution
def my_decorator(func):
    """A simple decorator that wraps a function"""
    def wrapper(*args, **kwargs):
        print("Something is happening before the function is called.")
        result = func(*args, **kwargs)
        print("Something is happening after the function is called.")
        return result
    return wrapper


# Using the decorator with @ syntax
@my_decorator
def say_hello(name):
    """A simple function that greets someone"""
    print(f"Hello, {name}!")


@my_decorator
def add_numbers(a, b):
    """A function that adds two numbers"""
    result = a + b
    print(f"The sum of {a} and {b} is {result}")
    return result


# Another decorator example: timing decorator
import time

def timer_decorator(func):
    """Decorator that measures execution time"""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Function '{func.__name__}' took {end_time - start_time:.4f} seconds")
        return result
    return wrapper


@timer_decorator
def slow_function():
    """A function that takes some time to execute"""
    print("Working on something...")
    time.sleep(1)
    print("Done!")


# Main execution
if __name__ == "__main__":
    print("=== Basic Decorator Example ===")
    say_hello("Alice")
    
    print("\n=== Decorator with Return Value ===")
    total = add_numbers(5, 3)
    print(f"Returned value: {total}")
    
    print("\n=== Timer Decorator Example ===")
    slow_function()