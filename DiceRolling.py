# https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

"""

Dice Rolling Simulator

Concepts to keep in mind:

Random
Integer
Print
While Loops

"""

import random

class Dice:

    dadomax = ""
    seguir = 1
    
    print("Bienvenido a la clase dado\n")
    dadomax = input("Escriba el numero maximo del dado: ")
    print("Establecido el maximo a: " + dadomax)
    while(bool(seguir)):
        numero = random.randint(1, int(dadomax))
        print("Su numero es: " + str(numero))
        seguir = int(input("Desea continuar? 0:No/1:Si"))
    print("Fin")
