try:
    num1 = float(input('Digite o primeiro número: '))
    operador = input('Digite o operador( + - * / ): ')
    num2 = float(input('Digite o segundo numero: '))

    if operador == '+':
        resultado = num1 + num2
        print(f'O resultado da soma é: {resultado}')
    elif operador == '-':
        resultado = num1-num2
        print(f'O resultado da subtração é: {resultado}')
    elif operador == '*':
        resultado = num1*num2
        print(f'Oresultado da multiplicação é: {resultado}')
    elif operador == '/':
        if num2 != 0:
            resultado = num1/num2
            print(f'O resultado da divisão é: {resultado:.3}')
        else:
            print('Erro, não é possivel dividir por zero!!!')
    else:
        print('Você não digitou um caractere valido')

except ValueError:
    print('Um ou ambos os números digitados são inválidos.')
    