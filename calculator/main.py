def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Cannot divide by zero"

def main():
    print("Simple Calculator")
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        operation = int(input("Select operation (1/2/3/4): "))
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
        
        if operation == 1:
            result = add(num1, num2)
        elif operation == 2:
            result = subtract(num1, num2)
        elif operation == 3:
            result = multiply(num1, num2)
        elif operation == 4:
            result = divide(num1, num2)
        else:
            print("Invalid operation choice")
            return
        
        print("Result:", result)
    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if __name__ == "__main__":
    main()
