import random

x=input("Give a number (3 digits or less): ")
while x>=1000:
  x=input("Number too big! Give a new number (3 digits or less): ")
y=random.randint(1,x)
z=input("Guess! ")
while z!=y:
  if z>y:
    z=input("Too high! Try again ")
  if z<y:
    z=input("Too low! Try again ")
print("Correct! The number is "+z)
    
    
