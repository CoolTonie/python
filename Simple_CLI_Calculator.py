#write a python calculator that can perform; addition, substraction, division, multiplication and modulus operations.
print('select an operation to perform')
print('1. ADD')
print('2. SUBSTRACT')
print('3. DIVIDE')
print('4. MULTIPLY')
print('5. MODULUS')

operation = input()
if operation == '1':
    num1 = input('enter first number:')
    num2 = input('enter second number:')
    print(str (int(num1) + int(num2)))
elif operation == '2':
    num1 = input('enter first number:')
    num2 = input('enter second number:')
    print(str (int(num1) - int(num2)))
elif operation == '3':
    num1 = input('enter first number:')
    num2 = input('enter second number:')
    print(str(int(num1) / int(num2)))
elif operation == '4':
    num1 = input('enter first number:')
    num2 = input('enter second number:')
    print(str(int(num1) * int(num2)))
elif operation == '5':
    num1 = input('enter first number:')
    num2 = input('enter second number:')
    print(str(int(num1) % int(num2)))
else: 
    print('invalid entry')