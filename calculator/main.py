from service import calculation
if __name__=="__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    operation = input("Enter operation (add/sub/mul/div): ")

    try:
        calculation.calculate(a,b,operation)
    except Exception as e:
        print(f"Error: {e}")