from adventurelib import*

Room.items=Bag()


#defines room
entrance = Room(""" Entrance
	It's a white room with doors in all 4 directions. 
	There is a desk near the south side of the room, 
	there seems to be some sort of card on the desk.
	""")



computer_lab = Room (""" Computer Lab
	There are computers in the room, the smell of coffee lingers in the air. 
	You might be able to use the computers.""")


#differnt elevators on different floors

elevator_1= Room (""" Elevator
	As you enter the elevator you can feel the ground sway, there are 3 buttons on the wall.
	One button has floor 1 next to it, another button has floor 2 and the last button is unlabled 
	and seems to have some sort of scanner next to it.""")

elevator_2= Room (""" Elevator
	As you enter the elevator you can feel the ground sway, there are 3 buttons on the wall.
	One button has floor 1 next to it, another button has floor 2 and the last button is unlabled 
	and seems to have some sort of scanner next to it.""")

elevator_3= Room (""" Elevator
	As you enter the elevator you can feel the ground sway, there are 3 buttons on the wall.
	One button has floor 1 next to it, another button has floor 2 and the last button is unlabled 
	and seems to have some sort of scanner next to it.""")



open_lab = Room (""" Open Lab
	As you walk in your nasal passages begin to burn
	after the chemicals went into your nose.
	The east side of the room has been over taken by black tentacles. 
	There are doors to the North, West and East.  """)


supply_Room = Room(""" Supply Room
	The room is stacked full of boxes, chemicals, and other useful equipment. 
	Something catches your eye, that thing being a hazmat suit.""")

computation_dry_lab = Room(""" Computation Dry Lab
	You walk into the room, it seems to be a normal lab. 
	There are lab coats hanging from a wall, one lab coat has has something in its pocket. """)

specialized_wet_lab=Room(""" Specialized_Wet
	""")

security_room=Room(""" Security Room
	On the south wall there are monitors all over the wall showing different rooms that you have been in.
	Underneath those monitors is a giant terminal covered""")

cloning_room=Room("""Cloning Room
	As you enter the cloning room you feel some familiarity as if youve been here before.
	There are cloning pods scattered throughout this giant warehouse.
	Most of the cloning pods seem to have humans in them except for two.
	On the ground you spot another ID. """)

#define connections
entrance.east=elevator_1
entrance.south=open_lab
entrance.west=computer_lab
open_lab.west=supply_Room
elevator_3.west=cloning_room
elevator_2.west=computation_dry_lab
computation_dry_lab.west=specialized_wet_lab
specialized_wet_lab.south=security_room


#define items
Item.descriptiom=""

level_1_access_card=Item("card","keycard")

level_2_access_card=Item("card 2","keycard 2")

level_3_access_card=Item("card 3","keycard 3")

scientist_id=Item("ID","Scientist ID")

security_id=Item("ID 2","security ID",)

hazmat_suit=Item("suit","hazmat suit")

#add items to the bag
entrance.items.add(level_1_access_card)
open_lab.items.add(level_2_access_card)
supply_Room.items.add(hazmat_suit)
computation_dry_lab.items.add(scientist_id)
specialized_wet_lab.items.add(level_3_access_card)


#defines variables
current_room=entrance
inventory=Bag()
entrance_unlocked=False

#binds
@when("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room=current_room.exit(direction)
		print(f"\nYou go {direction}\n")
		print(current_room)
		print(current_room.exits())
		if entrance_unlocked == False and current_room== entrance:
			print("The doors locked")
			
	else:
		print("You cant go in that direction.")
		return




@when("look")
def look():
	print(current_room)
	print(f"There are exits to the {current_room.exits()}.\n")
	if len(current_room.items) > 0: 
		print("You also see:")
		for item in current_room.items:
			print(item)





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




@when("i")
@when("inventory")
@when("show inventory")
@when("what is in my pocket")
@when("what am i holding")
def player_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)


@when("look at ITEM")
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f"You aren't carrying an {item}")




@when("use ITEM")
def use(item):
	if inventory.find(item) == scientist_id and current_room == computer_lab:
		print("You scanned the QR code on the ID using the computers extension scanner, a message appears.\n")
		print("21/10/27: Hello this is Pedro the founder of Synthetic Science Industries.")
		print("Today we are aiming to change this world forever by starting our research into the realm of cloning technology.")
		print("We have started the production of a new facility that has the main goal of being the first labratory ever to clone a human being.")
	elif inventory.find(item)== level_1_access_card and current_room == entrance:
		print("You went around the room unlocking the doors with the level 1 access card.")
		entrance_unlocked=True
	elif inventory.find(item)== level_2_access_card and current_room == elevator_1:
		print("You used the level 2 access card now you can go to the top floor")
	elif inventory.find(item)== level_3_access_card and current_room == elevator_1 or elevator_2:
		print("You used the level 3 access card now you can go to the basement")
	elif inventory.find(item)== security_id and current_room == computer_lab:
		print("You scanned the QR code on the ID using the computers extension scanner, a video appears.\n")
		print("26/5/31: Day 473 working at this dump and finnaly the science team seem to have made a working human clone.")
		print("Seconds later you hear a muffled voice in the backround.")
		print("All security personal report to sector C imedietly a second pod has burst open.")
		print("The video carried on playing for a few minutes but was silent apart from the occasional fear induced scream.")
	elif inventory.find(item)==hazmat_suit:
		print("You put the hazmat suit on.")

	else:
		print("You cant use that item here")





















def main():
	start()

if __name__== '__main__':
 main()
