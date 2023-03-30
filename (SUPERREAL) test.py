from calendar import c
from re import A


points = 0
def check(options , user_input):
    if user_input in options and user_input in options[0]:
        return True
    else:
        return False
       

ValidInputChecker = 0 
points = 0

#- Question 1 -#
options = ["b", "a", "c", "d"]
while ValidInputChecker < 100:
    Question = input("What city is known as the 'ETERNAL CITY'? \n A) Barcelona \n B) Rome \n C) Dubai \n D) Madrid\n\n>>").lower().strip()
    if check(options, Question):
        print("You got the right awnser!\n\n")
        points += 1 
    elif Question in options and Question in options[1:]:
        print("Wrong awnser!")
    else: 
        print("Please enter a valid input(a,b,c or d are valid inputs)")
        ValidInputChecker += 1
    
print("The correct answer is B!")
print("Your current score is {" + str(points) + "}")


