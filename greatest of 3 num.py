def num():
    a = int(input())
    b = int(input())
    c = int(input())
    return a,b,c

def check(a,b,c):
    if a>b and a>c:
        print(f"{a} is largest")
    elif b>a and b>c:
        print(f"{b} is largest")
    elif c>a and c>b:
        print(f"{c} is largest")
    return True

a,b,c = num()
check(a,b,c)

if __name__ == "__num__":
    num()