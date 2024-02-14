# from turtle import Turtle, Screen

# timmy = Turtle()
# print(timmy)
# timmy.shape('turtle')
# timmy.color('coral')
# timmy.forward(100)


# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable

table = PrettyTable()

table.add_column("Pokemon Name", ['pikachu','Squirtle','Charmander'])
table.add_column("Type", ['Electric','Water','Fire'])
table.align = 'l'
print(table)

class User:
    
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        
        
    def follow(self, user):
        user.followers +=1
        self.following +=1
        



user_1 = User("1308250", "Ephrem")
user_2 = User("130","Fev")
user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)