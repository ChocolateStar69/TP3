from Cancion import *
import random
from time import sleep
idiomas = ["Ingles", "Espaniol", "Frances", "Otro"]
discos = ["Calamidad", "Sinceridad", "Lujuria", "Poker", "Fe", "Cosmos", "Holy", "BTW", "FTW", "Same"]
interpretes = ["James", "MJ", "Alfred", "Robert", "Thanos", "Stark", "Nuenue", "CA", "Magnificent"]
generos = ["Rock", "Pop", "EDM", "Techno", "House", "Infantil", "Romance", "Cachengue", "Comercial"]
titulos = ["Cavernicola", "Spaceship", "Interstellar", "La Comarca", "Infinity", "Stones", "Bones", "Iron Man",
          "INSANO", "Rancio", "Coscu", "Uachaut", "World of Warcraft", "PUBG", "Aorus", "Kratos", "Peter Parker"]


def validar(min, max):
    a = int(input("Ingrese un numero mayor que " + str(min) + " y menor que " + str(max) + ":"))
    while a > max:
        a = int(input("Ingrese un numero mayor que " + str(min) + " y menor que " + str(max) + ":"))
    return a


def generar_vector(cantidad):
    vector = [0] * cantidad
    for i in range(0, cantidad):
        idioma = random.choice(idiomas)
        disco = random.choice(discos)
        interprete = random.choice(interpretes)
        genero = random.choice(generos)
        titulo = random.choice(titulos)
        reproducciones = random.randrange(0, 1000000)
        vector[i] = Cancion(titulo, disco, interprete, idioma, genero, reproducciones)
    return vector


def opcion1():
    n = validar(0, 20)
    print("="*100)
    canciones = generar_vector(n)
    return canciones


def opcion2():
    pass


def opcion3():
    pass


def opcion4():
    pass


def opcion5():
    pass


def opcion6():
    pass


def opcion7():
    pass


def opcion8():
    pass


def menu():
    op = -10
    while op != 0:
        print("\x1b[1;31m" + "Menu de opciones")
        print("\x1b[0;m" + "-"*100)
        print("1.- Generar canciones")
        print("2.- Mostrar canciones ordenas alfabeticamente")
        print("3.- Buscar el nombre del disco")
        print("4.- Canciones que superar el promedio de reproducciones")
        print("5.- Buscar artista y mostrar cual es su cancion mas escuchada")
        print("6.- Cantidad de canciones por idioma y genero")
        print("7.- Cantidad de canciones existentes por idioma")
        print("8.- Cantidad de reproducciones por genero")
        print("-"*100)
        op = validar(0, 8)
        print("-"*100)
        if op == 1:
            canciones = opcion1()
        elif op == 2:
            opcion2()
        elif op == 3:
            opcion3()
        elif op == 4:
            opcion4()
        elif op == 5:
            opcion5()
        elif op == 6:
            opcion6()
        elif op == 7:
            opcion7()
        elif op == 8:
            opcion8()
    print("\x1b[1;32m" + "Programa Finalizado")


menu()
