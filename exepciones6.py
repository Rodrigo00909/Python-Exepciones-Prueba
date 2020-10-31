""" Clausula else: Tambien se puede usar como exepcion """
"""
Es una clausa opcional en un bloque de try/except

Debe escribirse despues de todos los except

Solo se ejecuta cuando el bloque try precedente haya finalizado en forma normal, es decir sin haberse producido exepciones

Ejemplo:
Utilizar manejo de exepciones para continuar normalmente la ejecución de una función luego de producido un error

LA CLAUSULA ELSE QUE ESTA DEBAJO DE TODO SOLO SE EJECUTA SI NO HAY ERRORES
"""

def leerentero(msj="Ingrese un entero: "):
    while True: # Este while acordate que hace que sea un ciclo infinito porque si el usuario se equivoca lo podemos rehacer
        try:
            n = int(input(msj))
            # Antes el break estaba aca
        except ValueError:
            print("Dato Inválido.")
            print("Intente nuevamente.")
        else: # Primero se mira el try, si hay error se va a la exepcion, si no hay error se hace lo que esta dentro del else
            break # Que en este caso es break para romper el ciclo while infinito
    return n

#Programa principal
while True: 
    try:
        a = leerentero("Dividiendo? ")  
        b = leerentero("Divisor? ") 
        cociente = a // b 
        resto = a % b 
        break
    except ZeroDivisionError:
        print("No se puede dividir por cero.")
        print("Intente nuevamente.")
print()
print("Cociente: ", cociente)
print("Resto: ", resto)