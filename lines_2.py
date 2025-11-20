"""

* * *
*   *  -->  FOR n = 3
* * *

"""

n = int(input("enter n: "))
def loop():
    try:
        if n >=3:
            for i in range(n):
                for j in range(n):
                    if i == 0 or i == n-1 or j == 0 or j == n-1:
                        print("*",end=' ')
                    else:
                        print(" ",end=' ')
                print(end='\n')
        else:
            print("try again with number greater than 3")
    except ValueError:
        print("try again")

    return True

if __name__ == "__main__":
    loop()