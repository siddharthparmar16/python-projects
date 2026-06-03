def main():
    print("""
                    This program returns the sum of N numbers,
                    type number u want to get the sum of - """)
    num = int(input("enter a number: "))
    sum(num)
    result = sum(num)
    print(f"the sum of {num} natural number is {result}")

 def sum(n):
     return int((n*(n+1))/2)


if __name__ == "__main__":
    main()
