cadena = input("Ingrese una cadena de texto: ")

for enumerado, letra in enumerate(cadena):
    if enumerado % 2 == 0:
        print(letra)