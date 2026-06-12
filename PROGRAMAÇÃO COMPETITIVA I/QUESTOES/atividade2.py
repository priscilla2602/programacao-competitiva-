#MISTURA VERMELHO E AZUL

def continha():
    t = int(input())
    for j in range(t):
        n = int(input())
        vermelho = input().strip()
        azul = input().strip()
        vit_vermelho = 0
        vit_azul = 0
        for i in range(n):
            if vermelho[i] > azul[i]:
                vit_vermelho += 1
            elif vermelho[i] < azul[i]:
                vit_azul += 1
        if vit_vermelho > vit_azul:
            print("RED")
        elif vit_azul > vit_vermelho:
            print("BLUE")
        else:
            print("EQUAL")
if __name__ == '__main__':
    continha()