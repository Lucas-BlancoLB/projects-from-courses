class User:

    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user_1 = User('001', 'angela')
user_2 = User('002', 'jack')

user_1.follow(user_2)

print(user_1.followers, '\n' + str(user_1.following))
print(user_2.followers, '\n' + str(user_2.following))


################
# class User:
#
#     def __init__(self):
#         print("new user being created...")
#
#
# user_1 = User()
# user_1.id = '001'
# user_1.username = "angela"
#
# print(user_1.username)
#
# user_2 = User()
# user_2.id = "002"
# user_2.username = "jack"
