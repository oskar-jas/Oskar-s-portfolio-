""" Maths
This code will allow you to Add, Subtract, Divide and Multiply 2 numbers """

while True:
	
    print("_________________")
    print("|_______________|")
    print("|              0|")
    print("|———————————————|")
    print("|               |")
    print("| 7 | 8 | 9 | / |")
    print("|---------------|")
    print("| 4 | 5 | 6 | * |")
    print("|---------------|")
    print("| 1 | 2 | 3 | - |")
    print("|---------------|")
    print("| 0 | . | + | = |")
    print("—————————————————")
    #This is just a calculator for ornamentation

    def add(x, y,):
        #This function adds two numbers
        return x + y
  
    def subtract(x, y,):
        #This function subtracts two numbers
        return x - y
  
    def divide(x, y,):
        #This function divides two numbers
        return x / y
       
    def multiply(x, y,):
        #This function multiplies two numbers
        return x * y
    
    print(" ")
    print(" ")
    
    print("1. Add")
    print("2. Subtraction")
    print("3. Divide")
    print("4. Multiply")
    
    print(" ")
    
    choice = input("What do you want to do?  (1, 2, 3 or 4): ")
    #This lets you choose what operation you want to do
    
    print(" ")
    
    number1 = int(input("Enter your first number: "))
    
    print(" ")
    
    number2 = int(input("Enter your second number: "))
    #This lets you choose the numbers you want to use
    
    print(" ")
    
    if choice =='1':
        print(number1,"+", number2,"=", add(number1,number2))
    
    
    elif choice =='2':
        print(number1,"-", number2,"=", subtract(number1,number2))
    
    
    elif choice =='3':
        print(number1,"/", number2,"=", divide(number1,number2))
    
    
    elif choice =='4':
        print(number1,"*", number2,"=", multiply(number1,number2))
    
    print(" ")
    print(" ")
    
    print("----------------------------------------------------------------")
