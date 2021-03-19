# catching exceptions
# basic struture:
"""
try:  Something might that cause an error
except: Do this if there was an exception
else: Do this if  there were no exception
finally: Do this not matter what happens
"""
# FileNotFound
try:
    file = open("a_file.txt")
    a_dict = {"key":"value"}
    print(a_dict["asfdsdasf"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was close")
    raise KeyError("using raise to get my own errors")