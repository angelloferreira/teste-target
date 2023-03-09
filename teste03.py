string = input("Digite uma palavra ou frase: ")

lista_caracteres = list(string)

string_invertida = []

for i in range(len(lista_caracteres) - 1, -1, -1):
    string_invertida.append(lista_caracteres[i])

string_final = ''.join(string_invertida)

print(string_final)
