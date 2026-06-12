#PON (prime or not)

def primo(n):
    if n < 2: 
        return False
    if n == 2 or n == 3: 
        return True
    if n % 2 == 0:
        return False
    c = n -1
    p = 0
    while c % 2 == 0:
        c //= 2
        p += 1
    bases = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for a in bases:
        if a >= n:
            break
        x = pow(a, c, n)
        if x == 1 or x == n - 1:
            continue
        for k in range(r-1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
            else:
                return False
    return True
def conta():
    input_data = sys.stdin.read().split
    if not input_data:
        return
    t = int(input_data[0])
    for i in range(1, t + 1):
        n = int(input_data[i])
        if primo(n):
            print("YES")
        else:
            print("NO")
if __name__ == '__main__':
    conta()