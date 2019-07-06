# https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

"""

Guess the Number

Concepts to keep in mind:

Random function
Variables
Integers
Input/Output
Print
While loops
If/Else statements

"""

import random

class NumberGuess:

    numero = random.randint(1,10)
    adivinar = False
    while(adivinar==False):
        guess = input("Intente adivinar el numero aleatorio del 1 al 10: ")
        diferencia = numero - int(guess)
        if (diferencia>0):
            print("Un poco mas alto")
        elif(diferencia<0):
            print("Un poco mas bajo")
        else: 
            adivinar = True
    print("ACERTASTE!!!!!")
        
