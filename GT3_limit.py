from tkinter import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sympy import symbols, sympify, latex

win = Tk()
win.geometry("700x650")
win.title("Calculadora de Limites Simples")

x, y, z = symbols('x y z')

MARGEM_ERRO = 1e-9  # Ajuste conforme necessário

def limite_duas_variaveis(f_str, x0, y0):
    try:
        f = sympify(f_str)
        denominador = f.as_numer_denom()[1]

        if float(abs(denominador.subs({x: x0, y: y0}))) == 0.0:
            return "Indeterminado."
        
        limiteFinal = f.subs({x: x0, y: y0})
        return latex(limiteFinal)

    except Exception as e:
        return f"Ocorreu um erro no input"

def limite_tres_variaveis(f_str, x0, y0, z0):
    try:
        f = sympify(f_str)
        denominador = f.as_numer_denom()[1]

        if float(abs(denominador.subs({x: x0, y: y0, z: z0}))) == 0.0:
            return "Indeterminado."

        limiteFinal = f.subs({x: x0, y: y0, z: z0})
        return latex(limiteFinal)

    except Exception as e:
        return f"Ocorreu um erro no input."

# Função para calcular o limite
def calcular_limite():
    f_str = entry_funcao.get()
    try:
        x0 = float(entry_x.get())
        y0 = float(entry_y.get())
        
        if tipo_var.get() == 1: 
            resultado = limite_duas_variaveis(f_str, x0, y0)
            z0 = None
        else:
            z0 = float(entry_z.get())
            resultado = limite_tres_variaveis(f_str, x0, y0, z0)

        wx_funcao.clear()
        wx_resultado.clear()
        
        funcao_latex = latex(sympify(f_str))
        if tipo_var.get() == 1:
            wx_funcao.text(0.05, 0.5, f"$\\lim_{{(x,y) \\to ({x0}, {y0})}} {funcao_latex}$", fontsize=16)
        else:
            wx_funcao.text(0.05, 0.5, f"$\\lim_{{(x,y,z) \\to ({x0}, {y0}, {z0})}} {funcao_latex}$", fontsize=16)

        canvas_funcao.draw()

        wx_resultado.text(0.05, 0.5, resultado, fontsize=20)
        canvas_resultado.draw()

    except ValueError:
        wx_resultado.text(0.05, 0.5, "Entrada inválida!", fontsize=20)
        canvas_resultado.draw()

frame = Frame(win)
frame.pack()

tipo_var = IntVar(value=1)
radio_duas = Radiobutton(frame, text="Duas Variáveis (f(x,y))", variable=tipo_var, value=1)
radio_duas.pack()
radio_tres = Radiobutton(frame, text="Três Variáveis (f(x,y,z))", variable=tipo_var, value=2)
radio_tres.pack()

label_funcao = Label(frame, text="Função f(x,y) ou f(x,y,z):")
label_funcao.pack()
entry_funcao = Entry(frame, width=70)
entry_funcao.pack()

label_x = Label(frame, text="Digite x0:")
label_x.pack()
entry_x = Entry(frame, width=10)
entry_x.pack()

label_y = Label(frame, text="Digite y0:")
label_y.pack()
entry_y = Entry(frame, width=10)
entry_y.pack()

label_z = Label(frame, text="Digite z0 (opcional):")
label_z.pack()
entry_z = Entry(frame, width=10)
entry_z.pack()

botao_calcular = Button(frame, text="Calcular Limite", command=calcular_limite)
botao_calcular.pack()

fig_funcao = matplotlib.figure.Figure(figsize=(7, 2), dpi=100)
wx_funcao = fig_funcao.add_subplot(111)
canvas_funcao = FigureCanvasTkAgg(fig_funcao, master=frame)
canvas_funcao.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

fig_resultado = matplotlib.figure.Figure(figsize=(7, 2), dpi=100)
wx_resultado = fig_resultado.add_subplot(111)
canvas_resultado = FigureCanvasTkAgg(fig_resultado, master=frame)
canvas_resultado.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

wx_funcao.get_xaxis().set_visible(False)
wx_funcao.get_yaxis().set_visible(False)
wx_resultado.get_xaxis().set_visible(False)
wx_resultado.get_yaxis().set_visible(False)

win.mainloop()
