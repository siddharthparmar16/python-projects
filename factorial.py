fact = int(input("Enter: "))

factorial = 1

if fact <= 1:
    print(fact)

else:
    for i in range(1,fact+1):
        factorial = factorial*i

    print(factorial)