def regreso(a, b):
    if a * b <= 1000:
        return a * b
    else:
        return a + b
    
resultado = regreso(20, 50)
print(resultado) 