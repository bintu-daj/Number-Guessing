import random
intentos=7

def Reglas():
    print("¡Bienvenido al juego de adivinar números!\n")
    print("He seleccionado un número del 1 al 100.")
    print('Tienes 7 intentos para adivinarlo.\n')

def juego(number, intento=1):
    if intento>intentos:
        print("\n Game over!")
        print("El número que tenía pensado es:", number)
        return
    adivina= input(f"Intento{intento}/7 - pon el número que crees: ")
    try:
        adivina= int(adivina)
    except ValueError:
        print('Por favor pon un número!')
        return juego(number, intento)

    if adivina < 1 or adivina >100:
        print('Pon un número entre 1 y 100')
        return juego(number, intento)
    revisa_adivina= lambda x, y: "correcto" if x==y else ('menos' if x<y else 'más')
    result = revisa_adivina (adivina, number)
    if result == "correcto":
        print('\nFelicidades! Has adivinado el número correcto!')
        print('Lo has adivinado al', intento, "intento.")
        return
    if result == "menos":
        print("Aún te falta! Prueba con un número más alto.\n")
    else:
        print("Te has pasado! Prueba con un numeró más pequeño.\n")

    juego(number, intento + 1)


#inicio del juego
Reglas()

random_number= random.randint(1,100)   

juego(random_number)
        