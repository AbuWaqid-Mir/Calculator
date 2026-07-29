import time
time.sleep(1)
print("""
#######################################################
                    CALCULATOR                        
#######################################################    
    """)

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
    print("8. EXIT ")
    time.sleep(0.6)
    select_choice()

def select_choice():
    while True:
        time.sleep(0.6)
        print("""
#############################################""")
        time.sleep(0.6)
        feature = input("Please enter an option from 1-8: ")
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
            history()
            break
        elif feature == "8":
            end()
            break
        else:
            print("Invalid option - choose between 1-8")

def add():
    time.sleep(0.6)
    print("""
#############################################
                ADDITION
#############################################
    """)
    while True:
        try:
            time.sleep(0.4)
            num1 = int(input("Enter a number: "))
            break
        except ValueError:
            time.sleep(0.4)
            print("Invalid input")
    while True:
        try:
            time.sleep(0.4)
            num2 = int(input("Enter another number: "))
            break
        except ValueError:
            time.sleep(0.4)
            print("Invalid input")
    time.sleep(0.4)
    print(num1,"+",num2,"=",num1+num2)
    options()

def subtract():
    time.sleep(0.6)
    print("""
#############################################
                SUBTRACTION
#############################################
    """)
    while True:
        try:
            time.sleep(0.4)
            num1 = int(input("Enter a number: "))
            break
        except ValueError:
            time.sleep(0.4)
            print("Invalid input")
    while True:
        try:
            time.sleep(0.4)
            num2 = int(input("Enter another number: "))
            break
        except ValueError:
            time.sleep(0.4)
            print("Invalid input")
    time.sleep(0.4)
    print(num1,"-",num2,"=",num1-num2)
    options()

def multiply():
    time.sleep(0.6)
    print("""
#############################################
            MULTIPLICATION
#############################################
    """)
    while True:
        try:
            time.sleep(0.4)
            num1 = int(input("Enter a number: "))
            break
        except ValueError:
            time.sleep(0.4)
            print("Invalid input")
    while True:
        try:
            time.sleep(0.4)
            num2 = int(input("Enter another number: "))
            break
        except ValueError:
            time.sleep(0.4)
            print("Invalid input")
    time.sleep(0.4)
    print(num1,"x",num2,"=",num1*num2)
    options()

def divide():
    time.sleep(0.6)
    print("""
#############################################
                DIVISION
#############################################
    """)
    while True:
        try:
            time.sleep(0.4)
            num1 = int(input("Enter a number: "))
            break
        except ValueError:
            time.sleep(0.4)
            print("Invalid input")
    while True:
        try:
            time.sleep(0.4)
            num2 = int(input("Enter another number: "))
            if num2 == 0:
                print("Can't divide by zero")
            else:
                break
        except ValueError:
            time.sleep(0.4)
            print("Invalid input")
    time.sleep(0.4)
    print(num1,"÷",num2,"=",num1/num2)
    options()

def end():
    time.sleep(0.8)
    print("""
#######################################################
                    POWER OFF                        
####################################################### 
    """)
    exit()


options()
