#"""1. pedir las 3 notas a calcular
# 2. sumar las 3 notas
# 3. dividir el resultado entre 3
# 4. mostrar el resultado"""
nota_1 = int(input("Ingrese la primera nota: "))
nota_2 = int(input("Ingrese la segunda nota: "))
nota_3 = int(input("Ingrese la tercera nota: "))

suma = nota_1 + nota_2 + nota_3

promedio = suma /3

print(f"Tu promedio es de {promedio} puntos")