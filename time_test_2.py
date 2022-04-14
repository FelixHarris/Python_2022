import sys
from time import * 
import threading
from adventurelib import*



hp=False
stop_threads=False
@when("begin")
def begin():
	global my_timer
	global hp
	global countdown
	print("left")
	

	def countdown():
		global my_timer
		global hp
		my_timer=5
		

		

		for x in range(5):
			my_timer=my_timer-1
			sleep(1)
		sys.exit("")


		
			
		




		

		




	countdown_thread=threading.Thread(target=countdown)
	countdown_thread.start()



	while my_timer > 0:

		attack = input("")
		if attack == "left":
			print("you attacked it\n")
			stop_threads=True

	else:
		sys.exit("")
			
			
			
			
			
	
		
		
	
			

		

		



def main():
	start()

if __name__== '__main__':
 	main()
	
	

