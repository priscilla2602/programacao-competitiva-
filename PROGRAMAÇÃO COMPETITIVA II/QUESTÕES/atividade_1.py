#T-PRIMES

limite = 1000000
primo = [True] * (limite + 1)
primo[0] = False
primo[1] = False

for i in range(2, 1001):
    if primo[i] == True:
        for j in range(i * i, limite + 1, i):
            primo[j] = False

n = int(input())
numeros_entrada = input().split()

for i in range(n):
    x = int(numeros_entrada[i])
    
    raiz = int(x ** 0.5)

    if (raiz * raiz == x) and (primo[raiz] == True):
        print("YES")
    else:
        print("NO")
