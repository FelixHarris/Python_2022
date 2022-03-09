"""
user_icecreams=int(input("How many ice creams do you need."))
if user_icecreams >20:
	print("sorry there arnt enough ice creams.")
elif user_icecreams <20: 
 print("Here you go.")
travel_distance=int(input("How far are you going to travel"))
if travel_distance <200:
	print("Have a nice travel")
elif travel_distance >=200:
	print("Fill up your gas tank.")

age=int(input("How old are you?"))
if age >=18:
	print("You are an adult.")
elif age <18:
	print("You are not an adult.")

movie=input("What is your favourite movie?")
if movie == "Lord of the rings":
 print("You have excellent taste.")
else:
 print(" You smell.")


tradgedy=input("Do you know the tradgedy of darth plagueis the wise?")
if tradgedy.lower()=="no":
	print(" I thought not. It’s not a story the Jedi would tell you. It’s a Sith legend. Darth Plagueis was a Dark Lord of the Sith, so powerful and so wise he could use the Force to influence the midichlorians to create life… He had such a knowledge of the dark side that he could even keep the ones he cared about from dying. The dark side of the Force is a pathway to many abilities some consider to be unnatural. He became so powerful… the only thing he was afraid of was losing his power, which eventually, of course, he did. Unfortunately, he taught his apprentice everything he knew, then his apprentice killed him in his sleep. Ironic. He could save others from death, but not himself.")
elif tradgedy.lower()=="yes":
	print("Oh cool")

director=input("Do you know who directed Passion of the christ?")
if director .lower()== "Mel Gibson":
	print("Correct")
else:
	print("Mel Gibson.")
"""
score=0
question1=int(input("How many friends does Riley have?"))

if question1 == 0:
	print(score+1)

else:
	print("Wrong")

print("\n")

question2=input("True or False does Riley have any friends?")

if question2.lower()== "false":
	print(score+1)

else:
	print("Wrong")

print("\n")

question3=input("How many friends does Riley have.\n A)1 B)2 C)3 D)0")

joe