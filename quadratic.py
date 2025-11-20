import math

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

D = b**2 - 4*a*c

if D == 0:
    print("for discriminent = 0, there are same roots: ")
    root1 = -b/(2*a)
    root2 = -b/(2*a)
    print(f"Root 1 = {root1} \n Root 2 = {root2}")

elif D > 0:
    root1 = (-b + math.sqrt(D))/(2*a)
    root2 = (-b - math.sqrt(D))/(2*a)
    print(f"Root 1 = {root1} \n Root 2 = {root2}")

elif D <0: 
    real_part = -b/(2*a)
    imaginary_part = math.sqrt(abs(D))/(2*a)
    root1 = real_part + imaginary_part
    root2 = real_part - imaginary_part
    print(f"Root 1 = {real_part} + {imaginary_part}i")
    print(f"Root 2 = {real_part} - {imaginary_part}i")