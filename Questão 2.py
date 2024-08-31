def pertence_a_fibonacci(numero):
    a, b = 0, 1
    while b < numero:
        a, b = b, a + b
    return b == numero

#verificando numero
num = int(input("Informe um número: "))

# Verificando se o numero pertence a sequência de Fibonacci
if pertence_a_fibonacci(num):
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
