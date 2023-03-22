def add(num1, num2):
    return num1+num2
def subtract(num1, num2):
    return num1-num2
def multiply(num1,num2):
    return num1*num2
def divide(num1,num2):
    return num1/num2
   
def calculate():
    symbols=["+", "-", "*","%"]
    num1=float(input("First number: "))
    for i in symbols: print(i)
    operation=input("Type an operation: ")
    while operation!='+' and operation!='-' and operation!= '*' and operation!='%':
        for i in symbols: print(i)
        operation=input("Type an operation: ")
    num2=float(input('Second number: '))    
    if operation=="+":
        ans=add(num1,num2)
    elif operation=="-":
        ans=subtract(num1,num2)
    elif operation=="*":
        ans=multiply(num1,num2)
    else:
        ans=divide(num1,num2)
    print(f"{num1} {operation} {num2} = {ans}")
    again= input(f"Do you want to continue with {ans}? ")
    while again=='y' or again=="Y":
        num1=ans
        for i in symbols: print(i)
        operation=input("Type an operation: ")
        while operation!='+' and operation!='-' and operation!= '*' and operation!='%':
            for i in symbols: print(i)
            operation=input("Type an operation: ")
        num2=float(input('Second number: '))    
        if operation=="+":
            ans=add(num1,num2)
        elif operation=="-":
            ans=subtract(num1,num2)
        elif operation=="*":
            ans=multiply(num1,num2)
        else:
            ans=divide(num1,num2)
        print(f"{num1} {operation} {num2} = {ans}")
        again= input(f"Do you want to continue with {ans}? ")
    else:
        calculate()
    
     
calculate()


