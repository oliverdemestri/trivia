"""
# Challenge: Mini Trivia en Python

## Debes crear:
Un archivo llamado `trivia.py`

## Tu programa debe:
- pedir el nombre del jugador
- mostrar una bienvenida
- hacer 4 preguntas
- sumar 1 punto por cada respuesta correcta
- mostrar el nombre y el puntaje final

## Resultado final
- si `puntaje == 4` → **Excelente**
- si `puntaje >= 2` → **Muy bien**
- si no → **Puedes mejorar**

## Recuerda
- trabaja paso a paso
- no hace falta terminar perfecto
- usa Git durante el proceso
- haz varios commits pequeños"""
nombre_jugador = input("Ingrese su nombre: ")
print(f"Saludos jugador: {nombre_jugador}")
contador = 0
def cuestionario():
    respuesta1= input("Quien creo la luna: ").lower()
    respuesta2= int(input("Cuantas patas tiene oscar: ").lower())
    respuesta3= int(input("Cuanto es 2 + 2 : ").lower())
    respuesta4= input("Cual es el pokemon legendario que lleva el numero uno:  ").lower()

    if respuesta1 == "dios":
        contador +=1
    else:
        contador -=1
    if respuesta2 == 2:
        contador += 1
    else:
        contador -=1
    if respuesta3 == 4:
        contador += 1
    else:
        contador -=1
    if respuesta4 == "articuno":
        contador += 1
    else:
        contador -=1
    
cuestionario()
print(f"Eres {nombre_jugador} y lograste hacer {contador} puntos")
