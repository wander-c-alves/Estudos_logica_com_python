def calculadora():
    """
    Função principal que executa uma calculadora simples em loop.
    """
    operadores_permitidos = '+-*/'
    
    # Loop principal da calculadora
    while True:
        # 1. Obter entradas do usuário
        numero1 = input('Digite o Primeiro número: ')
        operador = input('Digite um operador (+-*/): ')
        numero2 = input('Digite o Segundo número: ')

        # Inicializa variáveis para os números convertidos
        num_1_float = 0
        num_2_float = 0
        
        # 2. Validação dos números
        try:
            # Tenta converter as entradas para float
            num_1_float = float(numero1)
            num_2_float = float(numero2)
        except ValueError:
            # Se a conversão falhar (não for um número válido)
            print('Um ou ambos os números digitados são inválidos.')
            continue # Volta para o início do loop

        # 3. Validação do operador
        
        # Verifica se foi digitado exatamente um operador válido
        if len(operador) != 1 or operador not in operadores_permitidos:
            print('Operador inválido. Digite apenas um dos seguintes: + - * /')
            continue # Volta para o início do loop

        # 4. Realização do cálculo
        print('\nResultado:')
        
        resultado = 0
        
        # Usamos 'if/elif/else' para garantir que apenas um bloco de cálculo seja executado
        if operador == '+':
            resultado = num_1_float + num_2_float
        
        elif operador == '-':
            resultado = num_1_float - num_2_float
        
        elif operador == '*':
            resultado = num_1_float * num_2_float
            
        elif operador == '/':
            # Tratamento de erro para divisão por zero
            if num_2_float == 0:
                print('Erro: Divisão por zero não é permitida.')
                continue # Volta para o início do loop
            resultado = num_1_float / num_2_float

        # 5. Exibir o resultado
        # Formato a saída em uma única linha, usando f-string para tudo
        print(f'{num_1_float} {operador} {num_2_float} = {resultado}')
        print('-' * 30) # Separador para melhor visualização

        # 6. Pergunta se quer sair
        sair = input('Quer sair? [S]im: ').lower().startswith('s')

        if sair:
            print('Calculadora encerrada.')
            break # Sai do loop

# Chamando a função principal
calculadora()