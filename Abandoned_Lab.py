from adventurelib import*
import random
import sys



Room.items = Bag()

#Room modifications
Room.add_direction("up","down")


#defines room
entrance = Room (""" Entrance
	It's a white room with doors in all 4 directions. 
	There is a desk near the south side of the room, 
	there seems to be some sort of level 1 access card on the desk.
	""")



computer_lab = Room (""" Computer Lab
	There are computers in the room, the smell of coffee lingers in the air. 
	You might be able to use the computers.""")


#differnt elevators on different floors

elevator_1 = Room (""" Elevator Floor 1
	As you enter the elevator you can feel the ground sway, there are 3 buttons on the wall.
	One button has floor 1 next to it, another button has floor 2 and the last button is unlabled 
	and seems to have some sort of scanner next to it.""")

elevator_2 = Room (""" Elevator Floor 2
	As you enter the elevator you can feel the ground sway, there are 3 buttons on the wall.
	One button has floor 1 next to it, another button has floor 2 and the last button is unlabled 
	and seems to have some sort of scanner next to it.""")

elevator_3 = Room (""" Elevator Basement
	As you enter the elevator you can feel the ground sway, there are 3 buttons on the wall.
	One button has floor 1 next to it, another button has floor 2 and the last button is unlabled 
	and seems to have some sort of scanner next to it.""")



open_lab = Room (""" Open Lab
	As you walk in your nasal passages begin to burn
	after the chemicals went into your nose.
	The east side of the room has been over taken by black tentacles.
	There is another card sitting in between 2 tentacles.""")


supply_Room = Room (""" Supply Room
	The room is stacked full of boxes, chemicals, and other useful equipment. 
	Something catches your eye, that thing being a hazmat suit.""")

computation_dry_lab = Room (""" Computation Dry Lab
	You walk into the room, it seems to be a normal lab. 
	There are lab coats hanging from a wall, one lab coat has has something in its pocket, 
	it's an ID.""")

specialized_wet_lab = Room (""" Specialized Wet Lab
	After finding out the code you walk into the lab instantly noticing the chill air.
	There seems to be another card on a desk, you begin to ask yourself how many cards are there?""")

security_room=Room (""" Security Room
	On the south wall there are monitors all over the wall showing different rooms that you have been in.
	Underneath those monitors is a giant terminal covered in all sorts of buttons""")

cloning_room=Room ("""Cloning Room
	As you enter the cloning room you feel some familiarity as if youve been here before.
	There are cloning pods scattered throughout this giant warehouse.
	Most of the cloning pods seem to have humans in them except for two.
	On the ground you spot another ID. """)


#define connections
#this code shows how the rooms connect to each other
entrance.east = elevator_1
entrance.south = open_lab
entrance.west = computer_lab
open_lab.west = supply_Room
elevator_3.west = cloning_room
elevator_2.west = computation_dry_lab
computation_dry_lab.west = specialized_wet_lab
specialized_wet_lab.south = security_room
elevator_1.up = elevator_2
elevator_1.down = elevator_3




#define items
Item.description = ""
#the access cards get messy so I added many names 
level_1_access_card = Item("level 1 access card","keycard","card", "card 1","keycard 1","card one","keycard two","level one access card","level 1 card","level one card","card1")
level_1_access_card.description = ("Its a white card with the number 1 on it, that has some sort of bar code on it")

level_2_access_card = Item("level 2 access card","keycard 2","card two","keycard two","card 2","level two access card","level 2 card","level two card","card2","card","second card","2nd card")
level_2_access_card.description = ("Its a white card with the number 2 on it, that has some sort of bar code on it")

level_3_access_card = Item("level 3 access card","keycard 3","card three","keycard three","card 3","level three access card","level 3 card", "level three card","card3","card")
level_3_access_card.description = ("Its a white card with the number 3 on it, that has some sort of bar code on it")

scientist_id = Item("scientist ID","ID","ID 1","ID one")
scientist_id.description = ("It's some sort of ID, it has a picture of someone with glasses and a white coat. "
	"On the back is a qr code maybe you can scan this.")

security_id = Item("security ID","ID 2","ID","ID two","ID","2nd ID","second ID")
security_id.description = ("It's another ID but it seems to be for one of the security personel." 
	"Like the scientist ID it has a QR code on the back.")

hazmat_suit = Item("hazmat suit","suit")
hazmat_suit.description = ("Its a yellow hazmat suit that doesnt have any crease marks.")




#add items to the bag
entrance.items.add(level_1_access_card)
open_lab.items.add(level_2_access_card)
supply_Room.items.add(hazmat_suit)
computation_dry_lab.items.add(scientist_id)
specialized_wet_lab.items.add(level_3_access_card)
cloning_room.items.add(security_id)


#defines variables
current_room = entrance
inventory = Bag()
#the list is here because there is no other place to put it
jump_list = ["Boing","You jumped","Why?","Up, up and away"]
entrance_unlocked = False
elevator_unlocked = False
elevator_unlocked_2 = False
security_room_unlocked = False
specialized_wet_lab_unlocked = False
computation_dry_lab_unlocked = False
hazmat_suit_on = False
terminal_access = False


#binds
#This code adds more ways you can print the directions

@when("n", direction = "north")
@when("e", direction = "east")
@when("s", direction = "south")
@when("w", direction = "west")
@when("u", direction = "up")
@when("d", direction = "down")
@when("north", direction = "north")
@when("east", direction = "east")
@when("south", direction = "south")
@when("west", direction = "west")
@when("up", direction = "up")
@when("down", direction = "down")
@when("go DIRECTION")
@when("head DIRECTION")
def travel(direction):
	global current_room
	#The code below makes locked doors


	if current_room == entrance and direction == "east" and entrance_unlocked == False:
		print("The door is locked it looks like a card could be inserted here.")
		return
		print(current_room)
	
	if current_room == entrance and direction == "west" and entrance_unlocked == False:
		print("The door is locked it looks like a card could be inserted here.")
		return
		print(current_room)

	if current_room == entrance and direction == "south" and entrance_unlocked == False:
		print("The door is locked it looks like a card could be inserted here.")
		return
		print(current_room)


	if current_room == elevator_1 and direction == "up" and elevator_unlocked == False:
		print("You press the top button on the elevator but nothing happens.")
		return
		print(current_room)
		
	if current_room == elevator_1 and direction == "down" and elevator_unlocked_2 == False:
		print("You press the bottom button and a buzzing noise played, nothing happened.")
		return

	if current_room == computation_dry_lab and direction == "west" and computation_dry_lab_unlocked == False:
		print("The door needs a password.")
		return


	if current_room == elevator_2 and direction == "west" and hazmat_suit_on == False:
		print("You open the elevator doors and step into the room.")
		print("Violent coughs begin to exit out your throat.")
		print("You believe the black tentacle creature produced an enzyme that attacks your throat")
		print("You scurry back to the elevator.")
		return

			

    #this code shows directions you can go to in the current room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"\nYou go {direction}\n")
		print(current_room)
		print(current_room.exits())		

	else:
		print("You cant go that way")

#This code chooses one of the 4 jump options from the jump list.
#This code also adds a comedic ending to the game
@when("jump")
def jump():
	if current_room == elevator_1 or current_room == elevator_2 or current_room == elevator_3:
		sys.exit("You jump, the ground begins to tremble. Snap! The elevator falls down instantly killing you.")
	else:
		print(random.choice(jump_list))




#This code allows the player to dance. I dont know why I added this.
@when("boogie")
@when("dance")
def dance():
	print("You begin to lose yourself in the groove.")


#this code prints the current room, items in the current room and the exits when you type look.
@when("look")
def look():
	print(current_room)
	print(f"There are exits to the {current_room.exits()}.\n")
	if len(current_room.items) > 0: 
		print("You also see:")
		for item in current_room.items:
			print(item)




#This code allows you to obtain an item.
@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
	else:
		print(f"You don't see a {item}")



#Shows items in inventory
@when("i")
@when("inventory")
@when("show inventory")
@when("what is in my pocket")
@when("what am i holding")
def player_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)

#shows item description in inventory
@when("look at ITEM")
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying an {item}")



#this code allows the user to use items. It usually prints something and changes a variable
@when("use ITEM")
def use(item):
	global entrance_unlocked
	global elevator_unlocked
	global hazmat_suit_on
	global elevator_unlocked_2
	if inventory.find(item) == scientist_id and current_room == computer_lab:
		#This text here will give you a code later on in the game
		print("You scanned the QR code on the ID using the computers extension scanner, a message appears.\n")
		print("21/10/27: Hello this is Pedro the founder of Synthetic Science Industries.")
		print("Today we are aiming to change this world forever by starting our research into the realm of cloning technology.")
		print("We have started the production of a new facility that has the main goal of being the first labratory ever to clone a human being.")
		print("Our cloning development will have the code name project ditto, so the government can't find out what we are trying to achieve and shut our business down.")
	elif inventory.find(item) == level_1_access_card and current_room == entrance:
		print("You went around the room unlocking the doors with the level 1 access card apart from the North side door")
		print("because the door has been locked by some sort of security system.")
		entrance_unlocked = True
	elif inventory.find(item) == level_2_access_card and current_room == elevator_1:
		print("You used the level 2 access card now you can go to the top floor")
		elevator_unlocked = True
	elif inventory.find(item) == level_3_access_card and current_room == elevator_1 or inventory.find(item) == level_3_access_card and current_room == elevator_2:
		print("You used the level 3 access card now you can go to the basement")
		elevator_unlocked_2 = True
	elif inventory.find(item) == security_id and current_room == computer_lab:
		print("You scanned the QR code on the ID using the computers extension scanner, a video appears.\n")
		print("26/5/31: Day four hundred and seventy three working at this dump and finnaly the science team seem to have made a working human clone.")
		print("Seconds later you hear a muffled voice in the backround.")
		print("All security personal report to sector C imedietly a second pod has burst open.")
		print("The video carried on playing for a few minutes but was black and silent apart from the occasional fear induced scream.")
	elif inventory.find(item) == hazmat_suit:
		print("You put the hazmat suit on.")
		hazmat_suit_on = True
	
	elif not inventory.find(item):
		print("You don't have any items")

	else:
		print("You can't use that item here")


#This code allows the user to enter codes that they learned into terminals
@when("enter code")
@when("enter password")
@when("put in code")
@when("put in password")
def enter_code():
	global computation_dry_lab_unlocked
	global terminal_access

	if current_room == computation_dry_lab:
		print("You go over to the terminal next to the west side door.")
		print("The terminal displays a message.")
		print("What is the name of the project.")
		@when("ditto")
		def ditto():
			global computation_dry_lab_unlocked
			print("Correct, you may proceed.")
			computation_dry_lab_unlocked = True

	if terminal_access == False and current_room == security_room:
		print("You walk over to the terminal it displays a message.")
		print("How many days was it since I worked at this place. ")
		@when("four hundred and seventy three")
		def days():
			global terminal_access
			print("Correct, now you are allowed to access the terminal.")
			terminal_access = True 
	
		


#this code makes it so you are allowed to finish the game. I did this with the .sys exit function 
#that makes it so your game instantly ends with some text
#there are two endings bad and good
@when("access terminal")
@when("access the terminal")
@when("terminal")
def terminal_use():
	global terminal_access
	if terminal_access == False and current_room == security_room:
		print("You walk over to the terminal it displays a message.")
		print("How many days was it since I worked at this place. ")
		@when("four hundred and seventy three")
		def days():
			global terminal_access
			print("Correct, now you are allowed to access the terminal.")
			terminal_access = True 
	
	elif terminal_access == True and current_room == security_room:
		print("There is a button that says shutoff the lockdown.")
		print("There is another button that says turret controls.")
		@when("turret")
		@when("press turret")
		@when("push turret")
		@when("activate turret")
		def turret():
			sys.exit("You deployed the turrets and activated them to shoot at the creature."
				" The creature was instantly oblierated. You exited out the lab happily knowing that the monstar was dealt with.")
		@when("shutoff lockdown")
		@when("push shutoff lockdown")
		@when("push shutoff lockdown button")
		@when("activate shutoff lockdown")
		@when("push the shutoff lockdown button")
		@when("push turn off lockdown button")
		@when("push the turn off lockdown button")
		def shutoff_lockdown():
			sys.exit("You turned off the lockdown systems now you can exit out the front door."
				" As you exit out the front door you turned around to see black tentacles reaching out through the door."
				" What have you done?")
		

		

	else:
		print("There are no terminals.")

	



#this code makes it so when you start the game the current room and exits appear
print(current_room)
print(current_room.exits())







def main():
	start()

if __name__== '__main__':
 main()
