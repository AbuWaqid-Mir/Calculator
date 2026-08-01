import time
import math

time.sleep(1)
print("""
#######################################################
                    CALCULATOR                        
#######################################################    
    """)

# Validation for all calculation functions (saves lines)
def get_num(message):
    while True:
        # Exception Handling
        try:
            number = int(input(message))
            return number
        except ValueError:
            print("Invalid input - please enter a number")

# Display menu options
def options():
    time.sleep(0.8)
    print("""
#############################################""")
    time.sleep(0.8)
    print("1. Addition ")
    time.sleep(0.4)
    print("2. Subtraction")
    time.sleep(0.4)
    print("3. Multiplication ")
    time.sleep(0.4)
    print("4. Division")
    time.sleep(0.4)
    print("5. Exponents ")
    time.sleep(0.4)
    print("6. Square Root ")
    time.sleep(0.4)
    print("7. History ")
    time.sleep(0.4)
    print("8. Clear History")
    time.sleep(0.4)
    print("9. EXIT ")
    select_choice()

# Checks user selection & calls matching calculation function
def select_choice():
    while True:
        time.sleep(0.6)
        print("""
#############################################""")
        time.sleep(0.6)
        feature = input("Please enter an option from 1-9: ")
        if feature == "1":
            add()
            break
        elif feature == "2":
            subtract()
            break
        elif feature == "3":
            multiply()
            break
        elif feature == "4":
            divide()
            break
        elif feature == "5":
            exponents()
            break
        elif feature == "6":
            sq_root()
            break
        elif feature == "7":
            show_history()
            break
        elif feature == "8":
            clear_history()
            break
        elif feature == "9":
            end()
        else:
            print("Invalid option - choose between 1-8")

# Addition Function
def add():
    time.sleep(0.6)
    print("""
#############################################
                ADDITION
#############################################
    """)
    time.sleep(0.4)
    num1 = get_num("Enter a number: ")
    time.sleep(0.4)
    num2 = get_num("Enter another number: ")
    answer = num1 + num2
    time.sleep(0.4)
    print(num1,"+",num2,"=",answer)
    # Opens text file and (a) appends calculation to end of file
    with open("history.txt", "a") as file:
        file.write(f"{num1} + {num2} = {answer}\n")
    options()

# Subtraction Function
def subtract():
    time.sleep(0.6)
    print("""
#############################################
                SUBTRACTION
#############################################
    """)
    time.sleep(0.4)
    num1 = get_num("Enter a number: ")
    time.sleep(0.4)
    num2 = get_num("Enter another number: ")
    answer = num1 - num2
    time.sleep(0.4)
    print(num1,"-",num2,"=",answer)
    with open("history.txt", "a") as file:
        file.write(f"{num1} - {num2} = {answer}\n")
    options()

# Multiplication Function
def multiply():
    time.sleep(0.6)
    print("""
#############################################
            MULTIPLICATION
#############################################
    """)
    time.sleep(0.4)
    num1 = get_num("Enter a number: ")
    time.sleep(0.4)
    num2 = get_num("Enter another number: ")
    answer = num1 * num2
    time.sleep(0.4)
    print(num1, "x", num2, "=", answer)
    with open("history.txt", "a") as file:
        file.write(f"{num1} x {num2} = {answer}\n")
    options()

# Division Function
def divide():
    time.sleep(0.6)
    print("""
#############################################
                DIVISION
#############################################
    """)
    time.sleep(0.4)
    num1 = get_num("Enter a number: ")
    time.sleep(0.4)
    # Keep asking until user enters a number that's not 0
    while True:
        num2 = get_num("Enter another number: ")
        if num2 == 0:
            print("Invalid input - cannot divide by zero")
        else:
            break
    answer = num1 / num2
    time.sleep(0.4)
    print(num1,"÷",num2,"=",answer)
    with open("history.txt", "a") as file:
        file.write(f"{num1} ÷ {num2} = {answer}\n")
    options()

# Exponentiation (to the power of) function
def exponents():
    time.sleep(0.6)
    print("""
#############################################
            EXPONENTIATION
#############################################
    """)
    time.sleep(0.4)
    num1 = get_num("Enter a number: ")
    time.sleep(0.4)
    num2 = get_num("Enter another number: ")
    time.sleep(0.4)
    # ** means to raise a number to the power of another number
    answer = num1 ** num2
    print(num1,"^",num2,"=",answer)
    with open("history.txt", "a") as file:
        file.write(f"{num1} ** {num2} = {answer}\n")
    options()

# Square root function
def sq_root():
    time.sleep(0.6)
    print("""
#############################################
                SQUARE ROOT
#############################################
    """)
    num = get_num("Enter a number: ")
    # math.sqrt(num) = find the square root of a number
    answer = math.sqrt(num)
    print("√", num, "=", math.sqrt(num))
    with open("history.txt", "a") as file:
        file.write(f"√{num} = {answer}\n")
    options()

# Shows the calculations stored in "history.txt"
def show_history():
    time.sleep(0.6)
    print("""
#############################################
                HISTORY
#############################################
""")
    # Creates "history.txt" if it doesn't already exist
    with open("history.txt", "a"):
        pass

    # Open file in read mode
    with open("history.txt", "r") as file:
        # Store all the lines in "history.txt" in a variable
        calculations = file.readlines()

    # Check if there are any lines in the file
    if len(calculations) == 0:
        print("No calculations yet")
    else:
        # Check each calculation in the text file
        for calculation in calculations:
            # Prevents extra blank lines when displaying history
            print(calculation, end="")

    options()

# Clears the contents of "history.txt"
def clear_history():
    time.sleep(0.6)
    print("""
#############################################
""")
    time.sleep(0.6)
    clear = input("Do you want to clear history? (Y/N): ").upper()
    if clear == "Y":
        # w (write mode) clears all existing content in "history.txt"
        with open("history.txt", "w") as file:
            pass
        print("History cleared")
    else:
        print("History NOT cleared")

    options()

# End the program
def end():
    time.sleep(0.8)
    print("""
#######################################################
                    POWER OFF                        
####################################################### 
    """)
    exit()


options()