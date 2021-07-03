# #1 read input float type values and get the media
#
# summa = 0
# count = 0
# num = float(input("Input a number: "))
#
# while num >= 0:
#     summa += num
#     count += 1
#     num = float(input("Input another number: "))
# #podemos calcular si es division entre 0
# average = summa / count
# print(f"The media was: {round(average, 2)}")


# 2 read the numbers given in a list and get the par and impar numbers in others list

# from random import randint
#
# num_list = []
# even_list = []
# odd_list = []
#
#
# for n in range(6):
#     #num = int(input("enter a number: "))
#     num = randint(1, 50)
#     num_list += [num]
#
# for e in num_list:
#     if e % 2 == 0:
#         even_list.append(e)
#     else:
#         odd_list.append(e)
#
# print(f"The list for 6 random numbers is: {num_list}")
# print(f"The list for 6 random numbers is: {even_list}")
# print(f"The list for 6 random numbers is: {odd_list}")

# 3 Enter 10 values into a tuple, get the largest number, the smallest and the more close to average
#
# tuple_num = ()
# largest_num = 0
# smallest_num = 0
# summa = 0
# average = 0
# nearest = 0
# for n in range(10):
#     num = int(input("enter a number: "))
#     tuple_num = tuple_num + (num,)
#     largest_num = smallest_num = tuple_num[0]
#     summa += num
# average = summa / 10
#
# for e in tuple_num:
#     nearest = e
#     if largest_num < e:
#         largest_num = e
#     elif smallest_num > e:
#         smallest_num = e
#     elif nearest**2
#
#
# print(f"The elements in the tuple are: {tuple_num}")
# print(f"The average is: {average}")
# print(f"The largest number is: {largest_num}")
# print(f"The smallest number is: {smallest_num}")

# using functions
from random import randint
average = 0
num = 0
tuple_num = ()
for n in range(10):
    tuple_num = tuple_num + (randint(0, 50),)

print(tuple_num)


def get_smallest(tuple_num):
    smallest = tuple_num[0]
    for e in tuple_num:
        if e < smallest:
            smallest = e
    print(smallest)


def get_largest(tuple_num):
    largest = tuple_num[0]
    for e in tuple_num:
        if e > largest:
            largest = e
    print(largest)


def get_average(tuple_num):
    addition = 0
    elem = 0
    for e in tuple_num:
        addition += e
        elem += 1
    if elem != 0:
        average = addition / elem
    else:
        average = 0
    return average


def abs_val(tuple_num):
    for

def get_nearest(tuple_num, average):
    for e in tuple_num:
        nearest = []
        nearest.append(tuple_num[0])
        diff = abs_val(average - tuple_num[0])
        if nearest < diff:
            nearest = diff
            num = e
    print(num)


get_smallest(tuple_num)
get_largest(tuple_num)
get_average(tuple_num)
get_nearest(tuple_num, get_average)
