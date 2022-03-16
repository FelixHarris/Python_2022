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

space = room("""
	You are drifting in space. It feels very cold.
	A slate_blue spaceship sits completely silently to your left,
	its airlock open and waiting.
	""")


def main():
	start()

if __name__== '__main__':
 main()