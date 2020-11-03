Renda_usuario = float(input("Qual sua renda: "))

if Renda_usuario < 2000:
    print("Liberado R$1000 de limite.")
elif Renda_usuario < 4000:
    print("Liberado R$2000 de limite.")
elif Renda_usuario < 6000:
    print("Liberado R$3000 de limite no seu cartão.")
elif Renda_usuario > 10000:
    print("Fale com nosso gerente. ")