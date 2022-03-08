"""
input("Press any key and then press enter.")#1
input("Type your name and press enter.")#2
input("Type your age and press enter.")#3

name=input("What is your name?")#4
age=input("How old are you?")#5
favourite_movie=("What is your favourite movie?")#6
book=input("Name a book.")#7
user_adjective=("Name an adjctive")#8
user_noun=("Name a noun")#9
user_verb=("Name a verb")#10
print(f"Hello {name}.")#11
print(f"You are {age} years old.")
print(f"{favourite_movie} is bad.")
print(f"{book} is good.")
print(f"{user_adjective} is a good describing word im going to use that more.")
print(f"{user_noun} is stupid.")
print(f"{user_verb} is dumb.")

user_age=int(input("How old are you?"))#12
print(f" you will be {user_age + 10} in 10 years")#13
print(f" you were born in {2022 - user_age}")#14
user_apples=int(input("How many apples do you have?"))
print(f"You have {user_apples} apples.")#15
friends_check=int(input("How many friends does Riley have"))
print(f"{friends_check}")#16

print(f"{user_apples/friends_check} you can have this many apples each.")#17

user_pizza=int(input("How many pizzas do you want?"))#18
user_feed=int(input("How many people do you want to feed?"))#19
print(f"Each person gets{user_pizza*8/user_feed}")#20
user_dollars=int(input("How many dollars do you have?"))#21
user_tv_price=int(input("How much does a tv cost?"))#22
print(f"You will have {user_dollars-user_tv_price} if you bought the tv.")#23
print(f"The tv will cost {0.8*user_tv_price} if it was 20% off.")#24

user_bitcoin=float(input("How many bitcoins do you have."))#25
bitcoin_cost=(55,661.97)#26
print(f"you have ${bitcoin_cost*user_bitcoin} bitcoin heres a gold medal.")#27
"""
user_wage=int(input("How much do you earn per week?"))#28
user_tax=float(input("How much is the tax as a decimal?"))#29
print(f"{user_wage-user_wage*taxed_money} ")