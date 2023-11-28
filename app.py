#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------

import random

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")




usuario = 0
cpu = 0

#Muestra en consola una bienvenida al usuario
print("\n")
print("***** Bienvenido al juego de piedra, papel o tijeras *****")
print("\n")

#Pide al usuario que escriba un número del uno al tres, indicando su significado y asigna el valor a la variable usuario
#1 = piedra
#2 = papel
#3 = tijeras
usuario = input("Escribe 'rock' para elegir piedra, 'paper' para elegir papel o 'scissors' para elegir tijeras: ")

#Si el usuario escribe rock, asigna el valor 1 a la variable usuario
if usuario == "rock":
    usuario = 1

#Si el usuario escribe paper, asigna el valor 2 a la variable usuario
elif usuario == "paper":
    usuario = 2

#Si el usuario escribe scissors, asigna el valor 3 a la variable usuario
elif usuario == "scissors":
    usuario = 3




#Genera un número aleatorio del 1 al 3 y asigna el valor a la variable cpu
cpu = random.randint(1, 3)

#Si el usuario y la cpu tienen el mismo valor, muestra en consola que hay un empate
if usuario == cpu:
    print("Empate")

#Si el usuario tiene el valor 1 y la cpu el valor 2, muestra en consola que la cpu gana
elif usuario == 1 and cpu == 2:
    print("El usuario eligio piedra y la CPU eligio papel")
    print("Gana la CPU")

#Si el usuario tiene el valor 1 y la cpu el valor 3, muestra en consola que el usuario gana
elif usuario == 1 and cpu == 3:
    print("El usuario eligió piedra y la CPU eligió tijeras")
    print("Gana el usuario")

#Si el usuario tiene el valor 2 y la cpu el valor 1, muestra en consola que el usuario gana
elif usuario == 2 and cpu == 1:
    print("El usuario eligió papel y la CPU eligió piedra")
    print("Gana el usuario")

#Si el usuario tiene el valor 2 y la cpu el valor 3, muestra en consola que la cpu gana
elif usuario == 2 and cpu == 3:
    print("El usuario eligió papel y la CPU eligió tijeras")
    print("Gana la CPU")

#Si el usuario tiene el valor 3 y la cpu el valor 1, muestra en consola que la cpu gana
elif usuario == 3 and cpu == 1:
    print("El usuario eligió tijeras y la CPU eligió piedra")
    print("Gana la CPU")

#Si el usuario tiene el valor 3 y la cpu el valor 2, muestra en consola que el usuario gana
elif usuario == 3 and cpu == 2:
    print("El usuario eligió tijeras y la CPU eligió papel")
    print("Gana el usuario")

#Si el usuario tiene un valor diferente a 1, 2 o 3, muestra en consola que el usuario ha introducido un valor incorrecto
else:
    print("El usuario eligió un valor incorrecto")
    print("No se puede determinar un ganador")

#Pregunta al usuario si quiere jugar otra vez
print("\n")
print("¿Quieres jugar otra vez?  (yes/no): ")

#Si el usuario escribe yes, vuelve a ejecutar el programa
if input() == "yes":
    exec(open("app.py").read())

#Si el usuario escribe no, muestra en consola un mensaje de despedida
else:
    print("Gracias por jugar")
    print("***** Fin del juego *****")
    print("\n")

