import time
import datetime
from adventurelib import*
import sys




@when("begin")
def begin():
    global total_seconds
    global joe
    def countdown(s):
 
   
        total_seconds =  s




        

        
   
 
    
        while total_seconds > 0:
            {




            

 
      
            timer = datetime.timedelta(seconds = total_seconds)
        
       
        
 
      
            time.sleep(1)
 
       
            total_seconds -= 1
            ;

        
            

            attack=input("")
            if attack=="left":
                print("You attacked it") ;}
       
 
        print("Bzzzt! The countdown is at zero seconds!")
        sys.exit()

       
   

    s = 5
    countdown(int(s))
    
    














def main():
    start()


if __name__== '__main__':
 main()
