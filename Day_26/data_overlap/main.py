# 💪 This exercise is HARD
# read the file1 and file2 and save the common numbers in result list
with open("file1.txt") as file1:
    list1 = file1.readlines()
new_list1 = []
print(list1)
with open("file2.txt") as file2:
    list2 = file2.readlines()


result = [int(num) for num in list1 if num in list2]

# Write your code above 👆

print(result)
