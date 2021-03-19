## Data Types
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

num1 = int(two_digit_number[0])
num2 = int(two_digit_number[1])

print(num1+num2)

## BMI Calculator
# 🚨 Don't change the code below 👇
height = input("enter your height in m: \n")
weight = input("enter your weight in kg: \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
bmi = float(weight)/ float(height)**2
bmi_int = int(bmi)
print(bmi_int)

## Your Life in Weeks
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

age = int(age)
age = 90 - age

# age in days
age_in_days = age*365

# age in weeks
age_in_weeks = age*52

# age in months
age_in_months = age*12

message =f"You have {age_in_days} days, {round(age_in_weeks)} weeks, and {age_in_months} months left."
print(message)
