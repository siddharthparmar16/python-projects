def celsius():
    celsius = float(input("Celsius: "))
    return celsius

def fahrenheit(celsius):
    fahrenheit = (9*celsius)/5 + 32
    print(f"Fahrenheit: {fahrenheit}")
    return fahrenheit

if __name__ == "__main__":
    fahrenheit(celsius())