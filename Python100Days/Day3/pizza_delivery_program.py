"""
Automatically calculate the bill based on the number of options
User is going to be asked 3 questions : 
    Small pizza (S):$15
    Medium pizza(M):$20
    Large pizza (L):$25

    Pepperoni for S : $2
    Pepperoni for M or L: $3

    Extra Cheeze for any sized pizza : $1
 
Calculate final bill based on User choices
"""

print("Welcome to Python Pizza Deliveries!")

size = input("What size pizz do you want? S, M, L :")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")

bill = 0

if size=="S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill +=25
else:
    print("You typed the Wrong Input")

if pepperoni == "Y":
    if size =="S":
        bill += 2
    else:
        bill +=3

if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is : ${bill}")