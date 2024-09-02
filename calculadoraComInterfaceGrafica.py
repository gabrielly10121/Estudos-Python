import tkinter as tk
from math import sqrt, factorial, log

def click(event):
    current = display.get()
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval_expr(current))
            display.set(result)
        except Exception as e:
            display.set("Erro")
    elif text == "C":
        display.set("")
    elif text == "⌫":
        display.set(current[:-1])
    else:
        display.set(current + text)

def eval_expr(expression):
    if "√" in expression:
        expression = expression.replace("√", "sqrt(") + ")"
    if "!" in expression:
        expression = expression.replace("!", "")
        return str(factorial(int(expression)))
    if "log" in expression:
        expression = expression.replace("log", "log(") + ")"
    try:
        return eval(expression, {"__builtins__": None}, {"sqrt": sqrt, "factorial": factorial, "log": log})
    except:
        return "Erro"

root = tk.Tk()
root.title("Calculadora")

# Configurações de cores
bg_color = "#d3d3d3"  
button_color = "#000000"  
operation_color = "#ff0000"  
equal_color = "#8b0000"  
display_bg_color = "#ffffff"  

root.configure(bg=bg_color)

# StringVar para o display
display = tk.StringVar()
entry = tk.Entry(root, textvar=display, font="lucida 20 bold", bg=display_bg_color, fg=button_color, borderwidth=5)
entry.grid(row=0, column=0, columnspan=4, pady=10)

buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "0", ".", "⌫", "+",
    "√", "!", "log", "="
]

row_val = 1
col_val = 0

for button in buttons:
    btn = tk.Button(root, text=button, font="lucida 15 bold", borderwidth=3)

    if button in ["+", "-", "*", "/", "√", "!", "log", "C", "⌫"]:
        btn.configure(fg=operation_color, bg=bg_color)
    elif button == "=":
        btn.configure(fg="#ffffff", bg=equal_color)
    else:
        btn.configure(fg=button_color, bg=bg_color)

    btn.grid(row=row_val, column=col_val, padx=10, pady=10, sticky="nsew")
    btn.bind("<Button-1>", click)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
