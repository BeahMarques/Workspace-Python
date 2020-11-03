var = int(input("Quanto deseja sacar "))

n100 = 0 #n100 = 0 pq senao ele pegaum valor aleatorio
n50 = 0
n20 = 0
n10 = 0

while var > 0 :
    if var >= 100:
        var -= 100
        n100 = n100 + 1
    elif var >= 50:
        var -= 50
        n50 = n50 + 1
    elif var >= 20:
        var -= 20
        n20 = n20 + 1
    elif var >= 10:
        var -= 10
        n10 = n10 +1 

print("Voce recebera %d notas de R$100, %d notas de R$50, %d notas de R$20, %d notas de R$10" % (n100, n50, n20, n10))



