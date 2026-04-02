import subprocess
import ttkbootstrap as tb
from ttkbootstrap import Separator
from ttkbootstrap.constants import *

total_segundos = 0
rodando = False

def mudarTema():
    novo_tema = boxSelect.get()
    root.style.theme_use(novo_tema)

def adicionar_tempo(segundos):
    global total_segundos
    total_segundos += segundos
    atualizar_label()

def atualizar_label():
    hora = total_segundos // 3600
    minuto =  (total_segundos % 3600) // 60
    segundo = (total_segundos % 3600) % 60
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


root = tb.Window(themename="cosmo")
root.title("Temporizador")
# root.geometry("565x275")
root.resizable(False, False)

janela = tb.Frame(root, padding=20)
janela.grid()

tb.Button(janela, text="Mudar", bootstyle="dark", command=mudarTema).grid(column=3, row=0,pady=2,ipadx=5)

boxSelect = tb.Combobox(janela,width=13,values=['cosmo','flatly','journal','litera','solar','superhero','darkly','cyborg','vapor'])
boxSelect.grid(column=2,row=0)
boxSelect.set("temas")

Separator(janela, orient="horizontal").grid(row=1, column=0, columnspan=4, sticky="ew", pady=20)

tb.Button(janela, text="5 Min", bootstyle="warning", command=lambda: adicionar_tempo(300)).grid(column=0, row=2, padx=1, pady=10,ipadx=25)
tb.Button(janela, text="30 Min", bootstyle="warning", command=lambda: adicionar_tempo(1800)).grid(column=1, row=2, padx=1, pady=10,ipadx=25)
tb.Button(janela, text="1 Hora", bootstyle="warning", command=lambda: adicionar_tempo(3600)).grid(column=2, row=2, padx=1, pady=10,ipadx=25)

label_total = tb.Label(janela, text="00:00:00", font=("Segoe UI", 40, "bold"),border=10)
label_total.grid(column=0, row=3, columnspan=3, pady=20)

tb.Button(janela, text="Limpar", command=limpar_total).grid(column=3, row=2, padx=10, pady=10,ipadx=5)
tb.Button(janela, text="Aplicar", bootstyle="success", command=aplicar).grid(column=3, row=3, padx=10, pady=10,ipadx=5)
tb.Button(janela, text="Cancelar",bootstyle="danger", command=cancelar_aplicacao).grid(column=3, row=4, padx=10, pady=10,ipadx=0)

root.mainloop()