# TODO: Creating my own class

"""1- create the class"""
# class User:
#     pass
#
#
"""2- create you object with the class inside"""
# user_1 = User()
#
"""3-add all the attributes that object need"""
"""a attribute is a variable associate to mi object(what has the object)"""
# user_1.id = "001"
# user_1.username = "Yo"
#
# print(user_1.username)

"""But, what if we need create so many users?"""
"""In Python we can use the constructor function 'def __init__(self):' inside the class"""
class User:
    """we can add all the parameters need"""
    def __init__(self, user_id, user_name):
        self.user_id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    """4-add the methods(what things the object does)->a method is a function"""
    def follow(self, user):
        user.followers += 1
        self.following += 1


"""now create the new object, and provide the 2 parameters"""
user1 = User("001", "Edgar")
user2 = User("002", "Sarami")
user1.follow(user2)
print(user1.followers)#->followers is not a parameter but is provide in the function
print(user1.following)
print(user2.followers)
print(user2.following)


