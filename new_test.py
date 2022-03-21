from adventurelib import*






@when("brush teeth")
def brush_teeth():
	print("you brush your teeth")

@when("comb hair")
@when("comb")
def comb_hair():
	say("""
		You brush your long flowing locks with
		the gold hairbrush that you have selected from the
		in the red basket.
		""")

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
escape_pods(""")


current_room=spaceship


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






def main():
	start()

if __name__== '__main__':
 main()