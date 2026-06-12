# A GAME WITH INTEGERS

def conta():
    t = int(input())
    for _ in range(t):
        n = int(input())
        if n % 3 != 0:
            print("First")
        else:
            print("Second")
if __name__ == '__main__':
    conta()