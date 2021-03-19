# If the bill was $150.00, split between 5 people, with 12% tip.
# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60
# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪
# HINT 1: https://www.google.com/search?q=how+to+round+number+to+2+decimal+places+python&oq=how+to+round+number+to+2+decimal
# HINT 2: https://www.kite.com/python/answers/how-to-limit-a-float-to-two-decimal-places-in-python

print('Welcome to the tip calculator')
bill = float(input('What was the total bill?: '))
tip = int(input('How much tip would you like to give? 10, 12, or 15?: '))
persons = int(input('How many people to split the bill?: '))

# calculators
tip_as_percent = tip/100
total_tip_amount = bill * tip_as_percent
total_bill = bill + total_tip_amount
bill_by_person = total_bill / persons
final_amount = round(bill_by_person, 2)
# this code work right when the second decimal is 0
final_amount = "{:.2f}".format(bill_by_person)

print(f'Each person should pay: ${final_amount}')