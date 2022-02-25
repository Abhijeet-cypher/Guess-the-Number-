import random as rand #importing random module and calling it rand 
a = int(input("Enter a number between 1 to 9 and I will try to guess the number: ")) 
b = rand.randrange(1,9) #generating a random range i.e 1 to 9 
print(b)
if a == b:
    print("I Won")
else: 
    print("Opps I failed lets try again")
