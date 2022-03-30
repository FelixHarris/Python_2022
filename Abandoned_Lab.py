from adventurelib import*


#Room Descriptions
entrance = Room(""" It's a white room with doors in all 4 directions. 
	There is a desk near the south side of the room, 
	there seems to be some sort of card on the desk.
	""")



computer_lab = Room (""" There are computers in the room, the smell of coffee lingers in the air. 
	You might be able to use the computers.""")




elevator= Room (""" As you enter the elevator you can feel the ground sway, there are 3 buttons on the wall.
	One button has floor 1 next to it, another button has floor 2 and the last button is unlabled 
	and seems to have some sort of scanner next to it.""")



open_lab = Room (""" As you walk in your nose achs in pain after smelling the chemicals in the air.
	The east side of the room has been over taken in black tentacles. 
	There are doors to the North, West and East.""")


Supply_Room = Room(""" The room is stacked full of boxes, chemicals, and other useful equipment. 
	One thing catches your eye, a hazmat suit.")


def main():
	start()

if __name__== '__main__':
 main()
