def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n/2)+1):
        if n % i == 0:
            return False 
        return True

n = int(input("escribir un numero: "))
if primo(n):
    print("El numero ", n, "es primo")
else:
    print("El numero ", n, "NO es primo")