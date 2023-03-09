# Solicita que o usuário informe um número
num = int(input("Digite um número inteiro positivo: "))

# Inicializa as variáveis que armazenarão os valores da sequência de Fibonacci
fib_ant = 0
fib_atual = 1

# Itera até encontrar (ou ultrapassar) o número informado
while fib_atual < num:
    # Imprime o valor atual da sequência (para acompanhar)
    print(fib_atual)
    
    # Atualiza os valores da sequência para o próximo termo
    fib_ant, fib_atual = fib_atual, fib_ant + fib_atual

# Verifica se o número informado está na sequência de Fibonacci
if fib_atual == num:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} NÃO pertence à sequência de Fibonacci.")
