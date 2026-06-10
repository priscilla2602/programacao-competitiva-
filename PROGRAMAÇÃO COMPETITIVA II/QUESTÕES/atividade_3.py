#ROBIN HOOD AND THE MAJOR OAK 

casos = int(input())

todas_as_entradas = []

while len(todas_as_entradas) < casos * 2:
    linha = input().split()
    for palavra in linha:
        todas_as_entradas.append(int(palavra))

indice = 0
for c in range(casos):
    n = todas_as_entradas[indice]
    k = todas_as_entradas[indice + 1]
    indice = indice + 2
    
    ano_inicio = n - k + 1
    ano_fim = n
    impares_ate_fim = (ano_fim + 1) // 2
    impares_antes_inicio = ano_inicio // 2
    
    total_impares = impares_ate_fim - impares_antes_inicio
    
    if total_impares % 2 == 0:
        print("YES")
    else:
        print("NO")
