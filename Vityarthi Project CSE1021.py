import math


print("\n\n")
print("Scientific Calculator".center(50,'*'))
print("Available Operations are: ")
print("1. + for addition")
print("2. - for subtraction")
print("3. * for multiplication")
print("4. / for division")
print("5. sin for sine(in radians)")
print("6. cos for cosine(in radians)")
print("7. tan for tangent(in radians)")
print("8. log for logarithm")
print("9. exp for exponential")
print("10. sqrt for square root")
print("11. cbrt for cube root")
print("12. pow for power")
print("13. Exit for exiting the calculator")

if __name__ == "__main__":
    while True:
        operation = input("\nEnter the operation you want to perform: ")
        if operation == "Exit":
            print("\nExiting the calculator. Bye! Thank you for using my scientific calculator. :)")
            break
        elif operation in ["+", "-", "*", "/", "sin", "cos", "tan", "log", "exp", "sqrt", "cbrt", "pow"]:
            if operation in ["sin", "cos", "tan", "log", "exp", "sqrt", "cbrt"]:
                num = float(input("Enter the number: "))
                if operation == "sin":
                    result = math.sin(num)
                elif operation == "cos":
                    result = math.cos(num)
                elif operation == "tan":
                    result = math.tan(num)
                elif operation == "log":
                    result = math.log(num)
                elif operation == "exp":
                    result = math.exp(num)
                elif operation == "sqrt":
                    result = math.sqrt(num)
                elif operation == "cbrt":
                    result = math.cbrt(num)
            else:
                a = float(input("Enter the first number: "))
                b = float(input("Enter the second number: "))
                if operation == "+":
                    result = a + b
                elif operation == "-":
                    result = a - b      
                elif operation == "*":
                    result = a * b    
                elif operation =="pow":
                    result = math.pow(a, b)   
                elif operation == "/":
                    if b != 0:
                        result = a / b
                    else:
                        print("Error: Division by zero is not defined.")
                        continue
            print(f"The result is: {result}"  
        else:
            print("Invalid operation.")







