from adventurelib import*

Room.items=Bag()

#ROOMS
space = Room("""
	You are drifting in space. It feels very cold.
	A slate_blue spaceship sits completely silently to your left,
	its airlock open and waiting.
	""")

spaceship=Room("""
	The bridge if the spaceship is shiny and white, with thousands of
	 small, red, blinking lights.
	""")

quarters=Room("""
	There are Beds.""")

cargo=Room("""
	Vent, SUS.""")

hallway=Room("""
	Red is actting kinda SUS.""")

mess_hall=Room("""
	Messi and Ronaldo.""")

docking=Room("""
	Riley.""")
bridge=Room("""
	Etika""")
escape_pods=Room("""
	Time to abandon ship""")


current_room=spaceship
inventory=Bag()

@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
	global  current_room
	if current_room is not space:
		say("There is no airlock here")
		return
	else:
		current_room=spaceship
		print("""You heave yourself into the spaceship and
			slam you hand on the button to close the door.
			""")
		print(current_room)

#Connections
spaceship.east=hallway
spaceship.south=quarters
hallway.east=bridge
hallway.north=cargo
cargo.east=docking
cargo.south=hallway
quarters.east=mess_hall
bridge.south=escape_pods


#Items
Item.description=""#this adds a blank description to each item


knife=Item("a dirty knife","Knife")
knife.description="the knife has a dull sheen to it but it looks rather sharp."

red_keycard= Item("A red keycard","Keycard","red card","red keycard") 
red_keycard.description="Its a red keycard. It probably opens a door or a locker."

red_button=Item("Red button","Button")
red_button.description=("Vote out the imposter")


bat=Item("bat")
bat.description=("its a bat")

#Bags
mess_hall.items.add(red_keycard)
cargo.items.add(knife)
cargo.items.add(bat)
quarters.items.add(red_button)


#Add items into bag
@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	if item in current_room.items:
		t=current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
	else:
		print(f"you dont see a {item}")



#Binds
@when ("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room=current_room.exit(direction)
		print(f"You go {direction}.")
		print(current_room)
		print(current_room.exits())
	else:
		print("You cant go that way.")

@when("look")
def look():
	print(current_room)
	print(f"there are exits to the{current_room.exits()}.")
	if len(current_room.items) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item)



#Functions
@when("inventory")
@when("show inventory")
@when("what is in my pocket")
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
		print(f"You arent carrying an {item}")





def main():
	start()

if __name__== '__main__':
 main()
