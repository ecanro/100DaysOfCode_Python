## Debug Odd or Even
number = int(input("Which number do you want to check?"))

if number % 2 == 0:# in this case the comparison operator is == not =
    print("This is an even number.")
else:
    print("This is an odd number.")


## Debug Leap Year
year = int(input("Which year do you want to check?"))  # the year was in string format

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")

## Debug FizzBuzz
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:#we need a "and"
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)#why print a list?
