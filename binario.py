def binarioaDecimal(strbinario):
    numero_decimal = 0
    

    for posicion, digito_string in enumerate(strbinario[::-1]):
        numero_decimal += int(digito_string) * 2 ** posicion

    print(f"El número binario {strbinario} es el {numero_decimal} en decimal")
    return numero_decimal


def esBinario(strbinario):
    
    for digitos in strbinario:
        if ((digitos == "0") or (digitos == "1")):
            print("El numero es binario")
            

            binarioaDecimal(strbinario)
            return True

        else:
            print("El número no es binario")
            return False




numero = input("Introduce un número binario: ")
esBinario(numero)



