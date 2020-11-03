n = int(input("Digite um numero "))
div = 0
cont = n

while cont > 0:
    if n % cont == 0:
        div = div + 1
    cont = cont - 1

if div == 2:
    print("Este numero %d é primo!" % n)
else:
    print("Este numero %d não é primo!" % n)