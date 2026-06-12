# A MINIMAL COMPRIME

def conta():
    t = int(input())
    
    for k in range(t):
        l, r = map(int, input().split())
        if l == 1 and r == 1:
            print(1)
        else:
            print(r - l)
if __name__ == '__main__':
    conta()