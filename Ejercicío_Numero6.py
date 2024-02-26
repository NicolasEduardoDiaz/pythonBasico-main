def par(n):
    if n % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
n = int(input("Escribir un numero: "))
resultados = par(n)
print("El numero es: ",par(n))