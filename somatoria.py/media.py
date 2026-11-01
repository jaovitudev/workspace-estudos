def nome(nm):
    return nm

def calcular_media(n1, n2, n3):
    return (n1 + n2 + n3) / 3

def ler_nota(mensagem):
    while True:
        nota = float(input(mensagem))
        if 0 <= nota <= 10:
            return nota
        print("Nota inválida! Digite um valor entre 0 e 10.")


nm = input("Digite o nome do aluno: ")

# 1º Bimestre
n1 = ler_nota("Digite a nota da prova mensal (1º bim): ")
n2 = ler_nota("Digite a nota do trabalho (1º bim): ")
n3 = ler_nota("Digite a nota da prova bimestral (1º bim): ")
m1 = calcular_media(n1, n2, n3)
print(f"A média do aluno {nome(nm)} no 1º bim é {m1:.2f}\n")

# 2º Bimestre
n1 = ler_nota("Digite a nota da prova mensal (2º bim): ")
n2 = ler_nota("Digite a nota do trabalho (2º bim): ")
n3 = ler_nota("Digite a nota da prova bimestral (2º bim): ")
m2 = calcular_media(n1, n2, n3)
print(f"A média do aluno {nome(nm)} no 2º bim é {m2:.2f}\n")

# 3º Bimestre
n1 = ler_nota("Digite a nota da prova mensal (3º bim): ")
n2 = ler_nota("Digite a nota do trabalho (3º bim): ")
n3 = ler_nota("Digite a nota da prova bimestral (3º bim): ")
m3 = calcular_media(n1, n2, n3)
print(f"A média do aluno {nome(nm)} no 3º bim é {m3:.2f}\n")

n1 = ler_nota("Digite a nota da prova mensal (4º bim): ")
n2 = ler_nota("Digite a nota do trabalho (4º bim): ")
n3 = ler_nota("Digite a nota da prova bimestral (4º bim): ")
m4 = calcular_media(n1, n2, n3)
print(f"A média do aluno {nome(nm)} no 4º bim é {m4:.2f}\n")


# Cálculo da média anual acumulada
media_final = (m1 + m2 + m3 + m4) / 4
print(f"Média final de {nome(nm)}: {media_final:.2f}")

# Verificação da situação do aluno
if media_final >= 5.0:
    print("Situação: Aprovado!")
else:
    print("Situação: Reprovado.")
