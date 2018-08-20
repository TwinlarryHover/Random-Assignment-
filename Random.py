import random 

a = random.randint (1,100)

b = int (input ("Enter any number of your choice:"))

while a !=b:
  if abs (a - b) <=10 :
   print ("You are close, try again")
  elif abs (a - b) >10:
   print ("You are not close, try again") 
  b = int (input ( "Enter a another number:"))
else:
   print ("You are correct")