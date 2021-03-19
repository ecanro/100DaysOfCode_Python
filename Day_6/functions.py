# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

# simple function


def greet():
    print('Hello!')
    print('nice')
    print('coders')


greet()

# function with parameters and arguments


def greet_with_name(name):
  print(f"Hello {name}")
  print(f"How do you do {name}?")


greet_with_name("Jack Bauer")

# Functions with more than 1 input


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}?")

# Calling greet_with() with Positional Arguments


greet_with("Jack Bauer", "Nowhere")
# vs.
greet_with("Nowhere", "Jack Bauer")


# Calling greet_with() with Keyword Arguments
greet_with(location="London", name="Angela")#=>important!


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(5))

