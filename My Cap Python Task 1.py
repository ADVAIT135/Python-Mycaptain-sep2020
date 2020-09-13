while (True):
    import random
    COMP=('r','p','s')
    #r stands for Rock
    #s stands for Scissors
    #p stands for Paper
    C=random.choice(COMP)
    U=input("User \t: ").casefold()

    if (C == 'r') and (U == 'r'):
        print("Match Draw")
    elif (C == 'r') and (U == 'p'):
        print("Hooray!! You won this round")
    elif (C == 'r') and (U == 's'):
        print("Sorry!! You lost this round")

    elif (C == 'p') and (U == 'p'):
        print("Match Draw")
    elif (C == 'p') and (U == 's'):
        print("Hooray!! You won this round")
    elif (C == 'p') and (U == 'r'):
        print("Sorry!! You lost this round")

    elif (C == 's') and (U == 's'):
        print("Match Draw")
    elif (C == 's') and (U == 'r'):
        print("Hooray!! You won this round")
    elif (C == 's') and (U == 'p'):
        print("Sorry!! You lost this round")
    else:
        print("Please enter valid inputs r,p,s")

    print("\n")
    cont=input("Want to try again? (y/n): ").casefold()
    print("\n")

    if(cont == 'y') or (cont == 'yes'):
        continue
    else:
        print("See you again. BYE!!! Have a nice day!!!")
        break
        
























      
