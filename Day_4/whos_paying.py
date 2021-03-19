## Who's Paying
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

import random
names_len = len(names) - 1
# print(names)
# print(names_len)
random_name = random.randint(0, names_len)
# print(random_name)

print(f'{names[random_name]} is going to buy the meal today!')

# solution 2
choice_name = random.choice(names)
print(choice_name + ' is going to buy the meal today')
