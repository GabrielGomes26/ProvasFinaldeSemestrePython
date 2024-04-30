print("Gabriel Gomes da Silva")
print("N2.B - Gerador de Senhas")
import random

def GeraSenha(tipo, tamanho):
    a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    b = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    c = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    d = a + b
    e = d + ["-", "_", ":", "@", "#", "$", "&", "?"]
    
    senha = []
    cont = 0

    while cont < tamanho:
        if tipo == "a":
            senha.append(random.choice(a))
        elif tipo == "b":
            senha.append(random.choice(b))
        elif tipo == "c":
            senha.append(random.choice(c))
        elif tipo == "d":
            senha.append(random.choice(d))
        elif tipo == "e":
            senha.append(random.choice(e))
        
        cont += 1

    return ''.join(senha)
Lista_Senhas = []
with open("MATR.txt", "r") as arquivo:
    for linha in arquivo:
        tipo = input("Tipo: ")
        tamanho = int(input("Tamanho: "))
        S = GeraSenha(tipo, tamanho)
        print(S)
        with open("SENHAS.txt", "a") as arquivo:
            arquivo.write(S + "\n")


    
