operadores = input("Digite qual operador você deseja: (+ - / *) ")
num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

if operadores == '+':
    resultado = num1 + num2 
    print(f'O resultado da soma foi: {resultado}')
elif operadores == '-':
    resultado = num1 + num2 
    print(f'O resultado da subtração foi: {resultado}')
elif operadores == '/':
    resultado = num1 + num2 
    print(f'O resultado da divisão foi: {resultado}')
elif operadores == '*':
    resultado = num1 + num2 
    print(f'O resultado da multiplicação foi: {resultado}')
else:
    print('opção invalida! os operadores são: + - / * ')