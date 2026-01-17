def pedir_numero(mensagem):
    """Pede um número ao usuário até receber um float válido ou um comando de saída."""
    while True:
        entrada = input(mensagem).strip()
        if entrada.lower() in ('sair', 'q'):    # permite sair digitando 'sair' ou 'q'
            return None
        try:
            return float(entrada)
        except ValueError:
            print('Entrada inválida. Digite um número válido ou "sair" para encerrar.')

def pedir_operador():
    """Pede um operador válido ao usuário."""
    operadores_permitidos = '+-*/'
    while True:
        op = input('Digite um operador (+ - * /) ou "sair": ').strip()
        if op.lower() in ('sair', 'q'):
            return None
        if len(op) == 1 and op in operadores_permitidos:
            return op
        print('Operador inválido. Digite apenas um dos seguintes: + - * /')

def format_num(n):
    """Formata número para esconder .0 quando inteiro (apenas para visual)."""
    if n == int(n):
        return str(int(n))
    return str(n)

def calculadora():
    print('Calculadora simples. Digite "sair" a qualquer momento para encerrar.')
    try:
        while True:
            num1 = pedir_numero('Digite o primeiro número: ')
            if num1 is None:
                break

            operador = pedir_operador()
            if operador is None:
                break

            num2 = pedir_numero('Digite o segundo número: ')
            if num2 is None:
                break

            # Checagem de divisão por zero
            if operador == '/' and num2 == 0:
                print('Erro: Divisão por zero não é permitida.')
                continue

            # cálculo
            if operador == '+':
                resultado = num1 + num2
            elif operador == '-':
                resultado = num1 - num2
            elif operador == '*':
                resultado = num1 * num2
            elif operador == '/':
                resultado = num1 / num2

            # exibe resultado com formatação simples
            print('\nResultado:')
            print(f'{format_num(num1)} {operador} {format_num(num2)} = {format_num(resultado)}')
            print('-' * 30)

            # pergunta curta se quer continuar
            resp = input('Continuar? (Enter para continuar, S para sair): ').strip().lower()
            if resp.startswith('s'):
                print('Calculadora encerrada.')
                break
    except KeyboardInterrupt:
        print('\nExecução interrompida pelo usuário. Calculadora encerrada.')

# roda a calculadora
calculadora()

