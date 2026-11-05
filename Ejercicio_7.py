#"""1. Pedir el precio
# 2. multiplicar el precio por el descuento
# 3. dividir el resultado entre 100
# 4. restar el resultado de la division entre 100 al precio
# 5. mostrar el precio del producto con el descuento aplicado"""

precio = int(input("Ingrese el precio del producto: "))
calculo_1 = precio * 21
calculo_2 = calculo_1 / 100
precio_final = precio - calculo_2
print(f"El precio final del producto con el descuento aplicado es de {precio_final}")