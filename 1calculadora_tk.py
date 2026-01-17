import tkinter as tk
from tkinter import messagebox

# --- Funções da calculadora ---
def clicar(botao):
    atual = visor.get()
    visor.delete(0, tk.END)
    visor.insert(0, atual + botao)

def limpar():
    visor.delete(0, tk.END)

def calcular():
    expressao = visor.get()
    try:
        expressao = expressao.replace('×', '*').replace('÷', '/')
        resultado = eval(expressao)
        visor.delete(0, tk.END)
        visor.insert(0, str(resultado))
    except ZeroDivisionError:
        messagebox.showerror("Erro", "Divisão por zero não é permitida.")
        visor.delete(0, tk.END)
    except Exception:
        messagebox.showerror("Erro", "Expressão inválida.")
        visor.delete(0, tk.END)

def sair():
    janela.destroy()

# --- Criação da janela principal ---
janela = tk.Tk()
janela.title("Calculadora Simples")

largura = 360
altura = 480  # reduzi um pouco a altura total
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
pos_x = (largura_tela // 2) - (largura // 2)
pos_y = (altura_tela // 2) - (altura // 2)
janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
janela.resizable(False, False)
janela.configure(bg="#f0f0f0")

# --- Campo de visor ---
visor = tk.Entry(janela, width=20, font=('Segoe UI', 28),
                 borderwidth=5, relief="ridge", justify='right')
visor.grid(row=0, column=0, columnspan=4, padx=12, pady=18, sticky='nsew')

# --- Configuração da grid ---
for i in range(4):
    janela.grid_columnconfigure(i, weight=1, minsize=80)
for r in range(1, 6):  # reduzi o número de linhas configuradas
    janela.grid_rowconfigure(r, weight=1, minsize=60)
janela.grid_rowconfigure(5, minsize=45)  # rodapé menor

# --- Lista de botões ---
botoes = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('×', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
]

btn_font = ('Segoe UI Symbol', 16)

for (texto, linha, coluna) in botoes:
    if texto == '=':
        botao = tk.Button(janela, text=texto, font=(btn_font[0], 16, 'bold'),
                          bg="#ff9800", fg="white", command=calcular)
    else:
        botao = tk.Button(janela, text=texto, font=(btn_font[0], 16),
                          bg="#ececec", fg="#111", command=lambda t=texto: clicar(t))
    botao.grid(row=linha, column=coluna, padx=10, pady=8, sticky='nsew')

# --- Rodapé menor ---
botao_limpar = tk.Button(janela, text='C', font=(btn_font[0], 14, 'bold'),
                         bg="#f44336", fg="white", command=limpar)
botao_limpar.grid(row=5, column=0, padx=10, pady=8, sticky='nsew')

botao_sair = tk.Button(janela, text='Sair', font=(btn_font[0], 14, 'bold'),
                       bg="#9e9e9e", fg="white", command=sair)
botao_sair.grid(row=5, column=1, columnspan=3, padx=10, pady=8, sticky='nsew')

janela.mainloop()





# import tkinter as tk
# from tkinter import messagebox

# # --- Funções da calculadora ---
# def clicar(botao):
#     operadores_permitidos = ['+', '-', '*', '/', '×', '÷']
#     atual = visor.get()

#     # Se o botão tiver mais de um caractere, usa apenas o primeiro
#     if len(botao) > 1:
#         botao = botao[0]

#     # Se o botão tiver mais de um caractere, usa apenas o primeiro
#     if len(botao) > 1:
#         botao = botao[0]

#     # Verifica se o caractere é válido
#     if not (botao.isdigit() or botao == '.' or botao in operadores_permitidos or botao == '='):
#         messagebox.showerror("Erro", f"Caractere inválido: '{botao}'. Use apenas números ou operadores (+ - × ÷).")
#         return

#     # Substitui operador anterior se o novo também for operador
#     if atual and atual[-1] in operadores_permitidos and botao in operadores_permitidos:
#         novo_texto = atual[:-1] + botao
#         visor.delete(0, tk.END)
#         visor.insert(0, novo_texto)
#         return

#     visor.delete(0, tk.END)
#     visor.insert(0, atual + botao)

# def limpar():
#     visor.delete(0, tk.END)

# def calcular(event=None):  # aceita evento do teclado
#     expressao = visor.get()

#     # Evita cálculo se o visor estiver vazio
#     if not expressao:
#         return

#     # Evita cálculo se já for um número (sem operadores)
#     operadores = ['+', '-', '*', '/', '×', '÷']
#     if all(op not in expressao for op in operadores):
#         return

#     try:
#         expressao = expressao.replace('×', '*').replace('÷', '/')
#         resultado = eval(expressao)
#         visor.delete(0, tk.END)
#         visor.insert(0, str(resultado))
#     except ZeroDivisionError:
#         messagebox.showerror("Erro", "Divisão por zero não é permitida.")
#         visor.delete(0, tk.END)
#     except Exception:
#         messagebox.showerror("Erro", "Expressão inválida.")
#         visor.delete(0, tk.END)

# def sair():
#     janela.destroy()

# # --- Criação da janela principal ---
# janela = tk.Tk()
# janela.title("Calculadora Simples")

# largura = 360
# altura = 480
# largura_tela = janela.winfo_screenwidth()
# altura_tela = janela.winfo_screenheight()
# pos_x = (largura_tela // 2) - (largura // 2)
# pos_y = (altura_tela // 2) - (altura // 2)
# janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")
# janela.resizable(False, False)
# janela.configure(bg="#f0f0f0")

# # --- Campo de visor ---
# visor = tk.Entry(janela, width=20, font=('Segoe UI', 28),
#                  borderwidth=5, relief="ridge", justify='right')
# visor.grid(row=0, column=0, columnspan=4, padx=12, pady=18, sticky='nsew')
# visor.bind("<Return>", calcular)  # tecla Enter ativa cálculo

# # --- Configuração da grid ---
# for i in range(4):
#     janela.grid_columnconfigure(i, weight=1, minsize=80)
# for r in range(1, 6):
#     janela.grid_rowconfigure(r, weight=1, minsize=60)
# janela.grid_rowconfigure(5, minsize=45)

# # --- Lista de botões ---
# botoes = [
#     ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('÷', 1, 3),
#     ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('×', 2, 3),
#     ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
#     ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
# ]

# btn_font = ('Segoe UI Symbol', 16)

# for (texto, linha, coluna) in botoes:
#     if texto == '=':
#         botao = tk.Button(janela, text=texto, font=(btn_font[0], 16, 'bold'),
#                           bg="#ff9800", fg="white", command=calcular)
#     else:
#         botao = tk.Button(janela, text=texto, font=(btn_font[0], 16),
#                           bg="#ececec", fg="#111", command=lambda t=texto: clicar(t))
#     botao.grid(row=linha, column=coluna, padx=10, pady=8, sticky='nsew')

# # --- Rodapé menor ---
# botao_limpar = tk.Button(janela, text='C', font=(btn_font[0], 14, 'bold'),
#                          bg="#f44336", fg="white", command=limpar)
# botao_limpar.grid(row=5, column=0, padx=10, pady=8, sticky='nsew')

# botao_sair = tk.Button(janela, text='Sair', font=(btn_font[0], 14, 'bold'),
#                        bg="#9e9e9e", fg="white", command=sair)
# botao_sair.grid(row=5, column=1, columnspan=3, padx=10, pady=8, sticky='nsew')

# janela.mainloop()



