
num1=float(input('enter a number: '))
op=input('type an operation(+,-,*,/): ')
while op != '+' and op!='-' and op!= '*' and op!= '/':
    op=input('type an operation(+,-,*,/): ')
num2=float(input('enter another number: '))
def calculate():
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1-num2
    elif op == '*':
        return num1*num2
    else:
        return num1/num2   
    
   
ans=calculate()
print(ans)
cont=input(f'do you want to continue calculations with {ans}? type y or n: ')
while cont=='y' or cont=='n':
    if cont == 'y':
        num1=ans
        op=input('type an operation(+,-,*,/): ')
        while op != '+' and op!='-' and op!= '*' and op!= '/':
            op=input('type an operation(+,-,*,/): ')
        num2=float(input('enter another number: '))
        ans= calculate()
        print(ans)
        cont=input(f'do you want to continue calculations with {ans}? type y or n: ')
    else:
        num1=float(input('enter a number: '))
        op=input('type an operation(+,-,*,/): ')
        while op != '+' and op!='-' and op!= '*' and op!= '/':
            op=input('type an operation(+,-,*,/): ')
        num2=float(input('enter another number: '))
        ans=(calculate())
        print(ans)
        cont=input(f'do you want to continue calculations with {ans}? type y or n: ')




