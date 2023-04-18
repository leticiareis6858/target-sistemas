def pertence_fibonacci(n):
    a, b = 0, 1
    while b < n:
        a, b = b, a + b
    if b == n:
        return True
    else:
        return False

numero_informado = int(input("Informe um número: "))
if pertence_fibonacci(numero_informado):
    print("Pertence à sequência de Fibonacci.")
else:
    print(" Não pertence à sequência de Fibonacci.")