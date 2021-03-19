## Adding Evens
# Write your code below this row 👇
# option1
sum = 0
for n in range(2, 101, 2):
    sum += n
print(sum)

# option2
total = 0
for n in range(1, 101):
    if n % 2 == 0:
        total += n
print(total)
