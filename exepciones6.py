def leerentero(msj="Ingrese un entero: "):
    while True: 
        try:
            n = int(input(msj))
        except ValueError:
            print("Dato Inválido.")
            print("Intente nuevamente.")
        else: 
            break 
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
