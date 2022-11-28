def estaEnRango(valor, minimo, maximo):

    if valor > maximo:
        print("El número es mayor al intervalo indicado, por favor introduzca otra vez el valor")
        return False
    elif valor < minimo:
        print("El número es menor al intervalo indicado, por favor introduzca otra vez el valor")
        return False
    else:
        print("El número introducido se encuentra dentro del intervalo")
        return True
     

def estaEnLista(valor,lista):

    encontrado = 0

    for numeros in lista:
        if valor == numeros:
            encontrado = 1
    
    if encontrado == 1:
        print("El número se encuentra dentro de la lista")
        return True
    else:
        print("El número está fuera de la lista")
        return False


valor = int(input("Introduzca un número comprendido entre los dos límites: "))
minimo = 1
maximo = 20

estaEnRango(valor,minimo,maximo)
lista = [5, 14, 11, 3, 2, 1, 15, 19]

valor = int(input("Introduzca un número: "))
estaEnLista(valor,lista)