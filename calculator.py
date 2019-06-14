# input 2 numbers
# print message : input + - * / Q
# + == sum ...
# if user not entered + - * / Q , ignore, continue
# if user asked to / by zero - break

x = int(input("Enter first number:"))
y = int(input("Enter second number:"))
oper = ''
while oper.upper() != 'Q':
    oper = input("Enter operation + - / * Q: ")
    if oper in ['+', '-', '*', '/'] == False:
        continue
    if oper == '/' and y == 0:
        print("cannot divide by zero....")
        break
    if oper == '+':
        print(f'{x} + {y} = {x + y}')
        #print(x, '+', y, x+y)
        #print(x + ' + ' + y + ' = ' + (x +y))
    elif oper == '-':
        print(f'{x} - {y} = {x - y}')
    elif oper == '*':
        print(f'{x} * {y} = {x * y}')
    elif oper == '/':
        print(f'{x} / {y} = {x / y}')
