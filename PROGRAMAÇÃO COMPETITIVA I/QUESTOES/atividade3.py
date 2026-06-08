#POW (x,n)

import sys

def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    if n < 0:
        x = 1 / x
        n = -n
        
    resultado = 1.0
    base_atual = x
    expoente = n
    
    while expoente > 0:
        if expoente % 2 == 1:
            resultado *= base_atual
        base_atual *= base_atual
        expoente //= 2
        
    return resultado

def main():
    try:
        linhas = sys.stdin.read().split()
        if len(linhas) >= 2:
            x = float(linhas[0])
            n = int(linhas[1])
            print(f"{myPow(x, n):.5f}")
    except Exception:
        pass

if __name__ == '__main__':
    main()
