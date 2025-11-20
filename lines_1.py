"""

*
* *    --> for n = 3
* * *
"""


def lines(n):
    for i in range(n):
        for j in range(i):
            print("*", end = ' ')
        print("*",end = '\n')
    
    return True

num = int(input("enter the number of line u want to print: "))
result = lines(num)