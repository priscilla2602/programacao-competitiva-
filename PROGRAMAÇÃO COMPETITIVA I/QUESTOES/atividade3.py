#POW (x,n)

class Solution:
    def myPow(self, x: float, n: int) -> float:
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
                resultado = resultado * base_atual
            
            base_atual = base_atual * base_atual
            expoente = expoente // 2
            
        saida_formatada = f"{resultado:.5f}"
        saida_com_virgula = saida_formatada.replace('.', ',')
        print(saida_com_virgula)
        
        return resultado
