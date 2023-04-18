string_informada = input("Digite a string a ser invertida: ")

string_invertida = ""

for i in range(len(string_informada)-1, -1, -1):
    string_invertida += string_informada[i]

print("String invertida:", string_invertida)
