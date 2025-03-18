def divi(x, y):
    if y == 0:
        return None
    return x / y


def pow(x, y):
    return x ** y


def rem(x, y):
    if y == 0:
        return None
    return x % y


def summa(start, end):
    if start > end:
        return None
    return sum(range(start, end + 1))


def main():
    while True:
        print("\n-MATHEMATICAL OPERATIONS:-")
        print("[D] - Divide")
        print("[E] - Exponentiation")
        print("[R] - Remainder")
        print("[F] - Summation")
        print("[Q] - Quit")
       
        option = input("Enter your choice: ").strip().upper()
       
        if option == 'Q':
            print("Program ended, Thank you.")
            break
       
        if option in ['D', 'E', 'R', 'F']:
            try:
                num1 = int(input("Enter the first number: "))
                num2 = int(input("Enter the second number: "))
            except ValueError:
                print("Invalid input: Intigers only")
                continue
           
            if option == 'D':
                output = divi(num1, num2)
            elif option == 'E':
                output = pow(num1, num2)
            elif option == 'R':
                output = rem(num1, num2)
            elif option == 'F':
                output = summa(num1, num2)
           
            if output is None:
                print("Invalid operation based on given constraints.")
            else:
                print("Result:", output)
        else:
            print("Invalid input: Please select a valid option.")


if __name__ == "__main__":
    main()