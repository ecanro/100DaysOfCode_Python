# TODO: will create a file.txt, open, read, write and update this file

"""Basic code"""
# file = open("my_file.txt")
# content = file.read()
# print(content)
# file.close()

""" functional code always using 'with' """
# with open("my_file.txt") as file:
#     content = file.read()
#     print(content)

"""read"""
with open("snake_with_storage_score/my_file.txt") as file:
    content = file.read()
    print(content)

"""write"""
with open("../my_file.txt", mode="a") as file:
    file.write("\na new line from python")

"""new file"""
with open("snake_with_storage_score/new_file.txt", mode="w") as file:
    file.write("New text")
    print(file)

# """read and write"""
# with open("../my_file.txt", mode="r+") as file:
#     file.write("\n new linea")
#     file.read()
#     print(file)

"""relative and absolute path"""
# with open("C:/Users/Edgar Canro/Desktop/absolute.txt", mode="w") as absolute:
#     file.write("this is absolute file")
#
# with open("../relative.txt", mode="w") as relative:
#     file.write("this is a relative file")

