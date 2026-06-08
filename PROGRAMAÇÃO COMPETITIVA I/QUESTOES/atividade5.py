#RESTAURANDO 3 NUMEROS

import sys

def main():
    dados_entrada = sys.stdin.read().split()
    if not dados_entrada:
        return
    
    numeros = [int(x) for x in dados_entrada]
    numeros.sort()
    
    soma_total = numeros[3]
    val1 = numeros[0]  
    val2 = numeros[1]  
    val3 = numeros[2]  
    
    a = soma_total - val3
    b = soma_total - val2
    c = soma_total - val1
    print(f"{a} {b} {c}")

if __name__ == '__main__':
    main()
