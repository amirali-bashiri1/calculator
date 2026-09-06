

import math


def show_menu():
    print("\n" + "=" * 40)
    print(" PYTHON CALCULATOR")
    print("=" * 40)
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Square Root")
    print("7. Percentage")
    print("8. Exit")
    print("=" * 40)


def get_number(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a valid number.")


def calculate():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "8":
            print("Goodbye!")
            break

        if choice == "1":
            a = get_number("First number: ")
            b = get_number("Second number: ")
            print("Result:", a + b)

        elif choice == "2":
            a = get_number("First number: ")
            b = get_number("Second number: ")
            print("Result:", a - b)

        elif choice == "3":
            a = get_number("First number: ")
            b = get_number("Second number: ")
            print("Result:", a * b)

        elif choice == "4":
            a = get_number("First number: ")
            b = get_number("Second number: ")

            if b == 0:
                print("Error: Cannot divide by zero.")
            else:
                print("Result:", a / b)

        elif choice == "5":
            a = get_number("Base: ")
            b = get_number("Power: ")
            print("Result:", a ** b)

        elif choice == "6":
            a = get_number("Number: ")

            if a < 0:
                print("Error: Cannot calculate square root of a negative number.")
            else:
                print("Result:", math.sqrt(a))

        elif choice == "7":
            number = get_number("Number: ")
            percent = get_number("Percentage: ")
            print("Result:", number * percent / 100)

        else:
            print("Invalid option.")


if __name__ == "__main__":
    calculate()
