#"""1. pedir su año de nacimiento
# 2. restar el año de nacimiento al año actual
# 3. mostrar el resultado en pantalla"""
año_nacimiento = int(input("Ingrese su año de nacimiento: "))
año_actual = 2026
edad = año_actual - año_nacimiento
print(f"Tu tienes {edad} años")