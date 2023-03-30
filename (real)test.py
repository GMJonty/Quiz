#Created by Jonty Weber
#Date 27/02/2023
#Demonstrate asking the user a question, provide multiple choice awnsers, get the user's awnser, check if its correct

#Setting the users score to 0
score = 0

#asking the user for their name to start this quiz
name = input("What is your name?")
print("Hi {} Are you ready to try the least fun puzzle quiz?".format(name))

#First question
Q1 = input("Question 1: DQoNCk9PSEhPSE9P \nA)1    \nB)2   \nC)3  \nD)4\n>>")
#if the user types in the right awnser then tell them you got it right
if Q1 == "D" or "4":
    print("You got it right!.")
    #adding one score when they have it right
    score +=1 
else:
    #If the user entered the wrong awnser, tell them its incorrect and do not add any score to their total
    print("Incorrect!")

#Second question
Q2 = input("Question 2: aQRkgy3Quas \nA)95\nB)300\nC)39\nD)102\n>>")
#if the user types in the right awnser then tell them you got it right
if Q2 =="39" or "C":
    print("You got it right!.")
      #adding one score when they have it right
    score +=1
else:
    #If the user entered the wrong awnser, tell them its incorrect and do not add any score to their total
    print("Incorrect!")

#Third question
Q3 = input("Question 3: CAT BOUNCE! Rl5 \nA)looking eyes\nB)Deadly Nose\nC)Funny death\nD)Bad Ears\n>>")
#if the user types in the right awnser then tell them you got it right
if Q3 == "looking eyes" or "A":
    print("You got it right!.")
      #adding one score when they have it right
    score +=1
else:
    #If the user entered the wrong awnser, tell them its incorrect and do not add any score to their total
    print("Incorrect!") 

#Fourth question
Q4 = input("QuestioN 4- 12 SHIFT UTLAITOS.14M1E9D18Z20 \nA)car\nB)train\nC)bus\nD)airplane\n>>")
#if the user types in the right awnser then tell them you got it right
if Q4 == "train" or "B": 
    print("You got it right!.")
    #adding one score when they have it right
    score +=1
else:
    #If the user entered the wrong awnser, tell them its incorrect and do not add any score to their total
    print("Incorrect!")

#Fith question
Q5 = input("Question 5- <img src='https://chart.googleapis.com/chart?cht=qr&chl=https%3A%2F%2Fczep.net%2Fweblog%2F52cards.html&chs=180x180&choe=UTF-8&chld=L|2' alt='qr code'><a href='https://www.qr-code-generator.com' border='0' style='cursor:default' rel='nofollow'></a> \nA)23\nB)52\nC)84\nD)102\n>>")
#if the user types in the right awnser then tell them you got it right
if Q5 == "52" or "B": 
    print("You got it right!.")
    #adding one score when they have it right
    score +=1
else: 
    #If the user entered the wrong awnser, tell them its incorrect and do not add any score to their total
    print("Incorrect!")
 
#Sixth question
Q6 = input("Question 6: wiki-Trollface-ref-4-\nRayquel Moreno\nFlandrina Guerra\nFlandrina SanzLa\nLa Tercea\n>>")
#if the user types in the right awnser then tell them you got it right
if Q6 == "La Tercea": 
    print("You got it right!.")
    #adding one score when they have it right
    score +=1
else:
    #If the user entered the wrong awnser, tell them its incorrect and do not add any score to their total
    print("Incorrect!")

#Seventh question
Q7 = input("Question 7- TohZEocBOLdSEi Obsecure. XvFZjo5PgG0 YXN3aWZ0aW50ZXJhdGlvbnBhZ2VhZDJuZGdyZWVu \n GGS!\n LBozo\n yomama\nRatio+\n>>")
#if the user types in the right awnser then tell them you got it right
if Q7 == "LBozo": 
    print("You got it right!.")
     #adding one score when they have it right
    score +=1
else:
    #If the user entered the wrong awnser, tell them its incorrect and do not add any score to their total
    print("Incorrect") 

#Eigth question
Q8 = input("Question 8- 1+1+1+0.112\n3.0112\nconcatination\nFloat\nawnser is real\n>>")
#if the user types in the right awnser then tell them you got it right
if Q8 == "Float": 
    print("You got it right!.")
    #adding one score when they have it right
    score +=1
else:
    #If the user entered the wrong awnser, tell them its incorrect and do not add any score to their total
    print("Incorrect! ")

#Ninth question
Q9 = input("Question 9- h}#sx}}oh \nImpossible\nWth is this question\nez puzzle\nhard where?\n>>")
#if the user types in the right awnser then tell them you got it right
if Q9 == "ez puzzle": 
    print("You got it right!.")
    #adding one score when they have it right
    score +=1
else:
    #If the user entered the wrong awnser, tell them its incorrect and do not add any score to their total
    print("Incorrect! ")

#Tenth question
Q10 = input("Question 10- GLLLLL. L\nP\nM\nT\nZ\n>>")
#if the user types in the right awnser then tell them you got it right
if Q10 == "T": 
    print("You got it right! Well done.")
    #adding one score when they have it right
    score +=1
else:
    #If the user entered the wrong awnser, tell them its incorrect and do not add any score to their total4
    print("Incorrect! ")

print("Congrats you got {} right! well done.".format(score))

if int(score < 5):
    print("Rating : D")
elif int(score == 6):
    print("PASSED: rating : C")
elif int(score == 7):
    print("PASSED: rating : C+")
elif int(score == 8):
    print("PASSED: rating : B")
elif int(score == 9):
    print("PASSED: rating : A")
elif int(score == 10):
    print("PERFECT SCORE!!!! WELL DONE")

print("Its time for another quiz that is actually awnserable. The general knowledge quiz!") 
