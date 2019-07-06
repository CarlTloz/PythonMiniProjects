#https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/

"""

Mad Libs Generator

Concepts to keep in mind:

Strings
Variables
Concatenation
Print

"""

class MadLibsGenerator:


    def menu():
        invalida = True
        while(invalida):
            selection = input("Qué historia te gustaría contar? Inserta el número (1,2,3) o 'q' para salir: ")
            if selection in [str(1),str(2),str(3),"q"]:
                invalida = False
            else:
                print("Escriba opcion valida")
        return selection

    def story1():
        nombre = input("Enter a plural noun: ")
        ocupacion = input("Enter an occupation: ")
        animal = input("Enter an animal name: ")
        lugar = input("Enter a place: ")
        print("In the book War of the " + nombre + ", the main character is " +
              "anonymus " + ocupacion + " who records the arrival of the " +
              animal + "s in " + lugar)

    def story2():
        name = input("Enter a name: ")
        state = input("Enter a state/country: ")
        print(name + ", I've got a feeling we're not in " + state + " anymore")

    def story3():
        name = input("Enter a first name: ")
        relative = input("Enter a relative: ")
        verb = input("Enter a verb: ")
        print("Hello. My name is " + name + ". You killed my " + relative + ". Prepare to " + verb)

    choice = menu()
    while(choice!="q"):
        if(int(choice)==1):
            story1()
        elif(int(choice)==2):
            story2()
        elif(int(choice)==3):
            story3()
        else:
            print("Ha ocurrido un error")
        choice = menu()
    print("Adios!!!")
