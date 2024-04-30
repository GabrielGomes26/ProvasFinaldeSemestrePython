print("Gabriel Gomes da Silva")
print("Cálculo de Salários - N2.C")
with open("SALARIO.txt", "r") as arquivo1, open("CALCULOS.txt", "a") as arquivo2:
    arquivo2.write("Bruto    AliqINSS    Val.INSS    BaseIR    AliqIR    Val.IR    Liquido\n")
    
    for linha in arquivo1:
        SB = float(linha.strip())
        
        if SB < 1751.81:
            ALQINSS = 0.08
        elif 1751.82 <= SB < 2919.72:
            ALQINSS = 0.09
        elif 2919.73 <= SB < 5839.45:
            ALQINSS = 0.11
        else:
            ALQINSS = 1
        
        VINSS = SB * ALQINSS
        BIR = SB - VINSS

        if BIR <= 1903.98:
            ALQIR = 0
            DED = 0
        elif 1903.99 <= BIR <= 2826.65:
            ALQIR = 0.075
            DED = 142.80
        elif 2826.66 <= BIR <= 3751.05:
            ALQIR = 0.15
            DED = 354.80
        elif 3751.06 <= BIR <= 4664.68:
            ALQIR = 0.225
            DED = 636.13
        else:
            ALQIR = 0.275
            DED = 869.36

        VALIR = BIR * ALQIR - DED
        if VALIR < 10:
            VALIR = 0
        SL = BIR - VALIR
        
        resultados = "{:.2f}   {:.2f}       {:.2f}      {:.2f}     {:.2f}     {:.2f}      {:.2f}\n".format(SB, ALQINSS * 100, VINSS, BIR, ALQIR * 100, VALIR, SL)
        arquivo2.write(resultados)
