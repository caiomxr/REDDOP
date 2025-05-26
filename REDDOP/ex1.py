
n = int(input("Qual o tamanho que você gostaria que a lista tivesse? "))

lista = [] * n

for i in range(n):
    num = int(input("Digite um número: "))
    lista.append(num)

maior = max(lista)

N_maior = lista.copy()
while maior in N_maior:
    N_maior.remove(maior)

if len(N_maior) == 0:
    print("A lista nao tem um segundo maior numero")
else:
    seg_maior = max(N_maior)
    print(f"O segundo maior numero é '{seg_maior}'")
    print(f"Pois o maior é '{maior}', e o segundo maior é '{seg_maior}'")
