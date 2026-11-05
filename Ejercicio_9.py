cadena = input("Ingrese una cadena de texto: ")
letras = 0

for caracter in cadena:
    if caracter.isupper():
        letras += 1
    elif caracter.islower():
        letras += 1
print(f"la cadena tiene {letras} letras")