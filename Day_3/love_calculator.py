## Love Calculator
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
true = 0
love = 0

concatenateNames = (name1 + name2).lower()

t = concatenateNames.count('t')
r = concatenateNames.count('r')
u = concatenateNames.count('u')
e = concatenateNames.count('e')

l = concatenateNames.count('l')
o = concatenateNames.count('o')
v = concatenateNames.count('v')
e = concatenateNames.count('e')

true = t + r + u + e
love = l + o + v + e

loveScore = int(str(true) + str(love))

if (loveScore < 10) or (loveScore > 90):
    print(f'Your score is {loveScore}, you go together like coke and mentos.')
elif (loveScore >= 40) and (loveScore <= 50):
    print(f'Your score is {loveScore}, you are alright together.')
else:
    print(f'Your score is {loveScore}.')
