from tkinter import *
from tkinter import ttk
import subprocess

total_segundos = 0
rodando = False

def adicionar_tempo(segundos):
    global total_segundos
    total_segundos += segundos
    atualizar_label()

def atualizar_label():
    hora = total_segundos // 3600
    resto = total_segundos % 3600
    minuto =  resto // 60
    segundo = resto % 60
    label_total.config(text=f"{hora:02d}:{minuto:02d}:{segundo:02d}")


def limpar_total():
    global total_segundos
    global rodando
    if not rodando:
        total_segundos = 0
        atualizar_label()

def aplicar():
    global rodando
    if total_segundos > 0 and not rodando:
        rodando = True
        countdown()
        subprocess.run(['shutdown','-s','-t',str(total_segundos)],shell=True)

def cancelar_aplicacao():
    global rodando
    if rodando:
        rodando = False
        subprocess.run(['shutdown','-a'],shell=True)
        limpar_total()

def countdown():
    global total_segundos, rodando

    if rodando and total_segundos > 0:
        total_segundos -= 1
        atualizar_label()
        root.after(1000, countdown)
    else:
        rodando = False


root = Tk()
root.title("Temporizador")
root.geometry("565x275")
root.resizable(False, False)

# Tema moderno
style = ttk.Style()
style.theme_use("clam") # existe esses: ('clam','default','classic')

# Estilo botão

#botao aplicar (verde)
style.configure("verde.TButton",font=("Segoe UI", 12, "bold"),background="#1d7e19",foreground="white",padding=3)
style.map("verde.TButton",background=[("active", "#186615")])

#botao cancelar (cinza)
style.configure("cinza.TButton",font=("Segoe UI", 12, "bold"),background="#7e7e7e",foreground="white",padding=3)
style.map("cinza.TButton",background=[("active", "#6d6d6d")])

#botao limpar (azul)
style.configure("azul.TButton",font=("Segoe UI", 12, "bold"),background="#1c6ac4",foreground="white",padding=3)
style.map("azul.TButton",background=[("active", "#135197")])

#botao tempo (branco)
style.configure("branco.TButton",font=("Segoe UI", 12, "bold"),background="#ffffff",foreground="black",padding=3)
style.map("branco.TButton",background=[("active", "#DFDFDF")])

frm = ttk.Frame(root, padding=20)
frm.grid()

ttk.Button(frm, text="1H",style="branco.TButton", command=lambda: adicionar_tempo(3600)).grid(column=0, row=1, padx=10, pady=10)
ttk.Button(frm, text="30min",style="branco.TButton", command=lambda: adicionar_tempo(1800)).grid(column=1, row=1, padx=10, pady=10)
ttk.Button(frm, text="5min",style="branco.TButton", command=lambda: adicionar_tempo(300)).grid(column=2, row=1, padx=10, pady=10)

label_total = ttk.Label(frm, text="00:00:00", font=("Segoe UI", 40, "bold"),foreground="#000000",border=10)
label_total.grid(column=0, row=2, columnspan=3, pady=20)

ttk.Button(frm, text="Limpar",style="azul.TButton", command=limpar_total).grid(column=3, row=1, padx=10, pady=10)
ttk.Button(frm, text="Aplicar",style="verde.TButton", command=aplicar).grid(column=3, row=2, padx=10, pady=10)
ttk.Button(frm, text="Cancelar",style="cinza.TButton", command=cancelar_aplicacao).grid(column=3, row=3, padx=10, pady=10)

root.mainloop()
