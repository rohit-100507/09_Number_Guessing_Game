import random 

print("WELCOME TO NUMBER GUSSING GAME ")
print("GUESS THE NUMBER FROM 1 TO 100 ")


while True:
    number = random.randint(1, 100)
    

    while True :

        guess = int(input("GUESS THE NUMBER :"))

        if guess < number :
            print("WRONG..! NUMBER IS BIGGER THAN" , guess ,"TRY AGAIN...")
            continue     

        elif guess > number :
            print("WRONG..! NUMBER IS SMALLER THAN" , guess ,"TRY AGAIN...")
            continue

        else :
            print("RIGHT....! YOUR GUESS IS CORRECT")
            break


    while True:
        
        next_round = input("WANT TO PLAY ANOTHER ROUND ? (yes /no) :").lower()

        if next_round == "yes":
            print("CONTINUE AGAIN...!")
            break

        elif next_round == "no":
            print("GAME STOPPED")
            exit()

        else:
            print("ERROR: Please enter only yes or no")
             
