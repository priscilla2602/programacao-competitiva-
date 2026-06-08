#MATEMATICA SIMPLES

import sys

def main():
    input_data = sys.stdin.read().split()
    if not input_data:
        return
    
    A = int(input_data[0])
    B = int(input_data[1])
    C = int(input_data[2])
    
    MOD = 998244353
    
    soma_A = (A * (A + 1) // 2) % MOD
    soma_B = (B * (B + 1) // 2) % MOD
    soma_C = (C * (C + 1) // 2) % MOD
    
    multiplicacao_intermediaria = (soma_A * soma_B) % MOD
    resultado_final = (multiplicacao_intermediaria * soma_C) % MOD
    
    print(resultado_final)

if __name__ == '__main__':
    main()
