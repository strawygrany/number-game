import random 
print("Number Guesssing Game!")
number = random.randint(1,9)
chances=0
print("Guess A Number(Between 1 And 9)!")

while  chances < 5:
    guess = int(input("Type Your Number Here:"))
    

    if guess== number:
     print("Congratulations,You Win!")
     break

    elif guess > number:
     print("Too High,Try again.")

    else:
     print("Too Low,Try Again")

     chances+=1

    if not chances > 5:
     print("You Lost!")
     