operadores = input("Digite qual operador você deseja: (+ - / *) ")
num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

if operadores == '+':
    resultado = num1 + num2 
    print(f'O resultado da soma foi: {round(resultado, 2)}')
elif operadores == '-':
    resultado = num1 + num2 
    print(f'O resultado da subtração foi: {round(resultado, 2)}')
elif operadores == '/':
    resultado = num1 + num2 
    print(f'O resultado da divisão foi: {round(resultado, 2)}')
elif operadores == '*':
    resultado = num1 + num2 
    print(f'O resultado da multiplicação foi: {round(resultado, 2)}')
else:
    print('opção invalida! os operadores são: + - / * ')