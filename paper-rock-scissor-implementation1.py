from microbit import *
from radio import *
from random import*

#turn radio on and
on()
config(group=6, length=251)

typeTransmitted = randint(0,2)
# R – rock, S – scissors, P – paper
rps = [ "r", "s", "p" ]
shaken = False

# 0=stein, 1=saks, 2=papir
def win(me, he):
  if(me == 0 and he == 1):
      return True
  elif(me == 0 and he == 2):
      return False
  elif(me == 1 and he == 0):
      return False
  elif(me == 1 and he == 2):
      return True
  elif(me == 2 and he == 0):
      return True
  elif(me == 2 and he == 1):
      return False
  else:
      return False

while True:
   if button_a.was_pressed() and shaken:
       shaken = False
       send(str(typeTransmitted))

   
   if accelerometer.was_gesture("shake"):
       #send the images
       shaken = True
       
       typeTransmitted = randint(0,2)
       display.scroll(rps[typeTransmitted])
       
       display.clear()
   
   #receive data    
   data = receive()
   
   #check that we have received any data
   if data != None:
       display.scroll(str(win(typeTransmitted, int(data))))
       
       #split the data into different pictures by the marker
       #display.scroll(data)

       #clear the screen
       display.clear()
