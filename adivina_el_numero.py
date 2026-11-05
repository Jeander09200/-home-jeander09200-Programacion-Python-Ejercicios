import random

aleatorio = random.randint(1, 100)


while True:
    num = int(input("Adivine el numero del 1 al 100: "))
    if num < aleatorio:
        print("El numero es mas alto")
    elif num > aleatorio:
        print("El numero es mas bajo")
    else:
        print("Adivinastes el numero")
        break