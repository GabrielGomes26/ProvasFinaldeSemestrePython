print("Gabriel Gomes da Silva")
print("Totalização Simples de Vendas de Produtos - N2.A")
vendas = []

while True:
    codigo = int(input("Digite um código, ou digite 0 para encerrar: "))
    
    if codigo == 0:
        break
    elif codigo < 10000 or codigo > 21000:
        print("Código inválido (deve ser entre 10000 e 21000)")
    
    total = 0  
    
    with open("vendas.txt", "r") as arquivo:
        for linha in arquivo:
            cod, q, valor = linha.strip().split(";")
            cod = int(cod)
            q = int(q)
            valor = float(valor)
            tot = q * valor
            if codigo == cod:
                vendas.append(tot)
                total = total + tot 
    
    print("Total vendido do produto {} = R$ {:.2f}".format(codigo, total))
