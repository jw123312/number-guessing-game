import random

won = True

while True:

    if won:    
        num = random.randint(1,100)
        won = False

    #ensure that number wont be blank
    while (inp := input("Number to guess:")) == '':
        pass
        
    
    if inp.lower() == 'q':
        break;

    inp = int(inp)
    
    if inp == num:
        print("you won!")
        won = True
    elif inp > num:
        print("Your number is greater")
    else:
        print("Your number is lower")
