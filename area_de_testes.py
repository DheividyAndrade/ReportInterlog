import tkinter as tk
from tkinter import messagebox
import pyautogui
from time import sleep
import threading
from datetime import datetime

# Variáveis globais de controle
executar_corteva = False
executar_stine = False
parar_execucao = False

# Interface de seleção de relatórios
def escolher_opcoes():
    def iniciar():
        global executar_corteva, executar_stine
        executar_corteva = var_corteva.get()
        executar_stine = var_stine.get()
        if not executar_corteva and not executar_stine:
            messagebox.showwarning("Atenção", "Você precisa selecionar ao menos uma opção.")
        else:
            janela.destroy()

    janela = tk.Tk()
    janela.title("Selecionar Relatórios")
    janela.geometry("300x200")

    tk.Label(janela, text="Selecione os relatórios que deseja enviar:").pack(pady=10)

    var_corteva = tk.BooleanVar()
    var_stine = tk.BooleanVar()

    tk.Checkbutton(janela, text="Corteva + WhatsApp", variable=var_corteva).pack(anchor='w', padx=20)
    tk.Checkbutton(janela, text="Stine + WhatsApp", variable=var_stine).pack(anchor='w', padx=20)

    tk.Button(janela, text="Iniciar", command=iniciar).pack(pady=20)

    janela.mainloop()

# Interface de controle para parar execução
def interface_parada():
    def parar():
        global parar_execucao
        parar_execucao = True
        janela_parada.destroy()

    janela_parada = tk.Tk()
    janela_parada.title("Controle de Execução")
    janela_parada.geometry("250x100")
    tk.Label(janela_parada, text="Clique para parar o processo.").pack(pady=10)
    tk.Button(janela_parada, text="Parar Agora", command=parar, fg="white", bg="red").pack()
    janela_parada.mainloop()

# === Funções de relatório ===

def corteva():
    pyautogui.press('win')
    sleep(1)
    pyautogui.typewrite('google')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.click(533,518, duration=0.5)
    sleep(2)
    pyautogui.hotkey('ctrl', 't')
    sleep(1)
    pyautogui.click(328,491,duration=0.5)
    sleep(3)
    pyautogui.click(82,115, duration=1)
    sleep(2)
    pyautogui.click(1254,251, duration=0.5)
    sleep(1)
    pyautogui.typewrite('REPORT_OPERACIONAL_CARREGAMENTO_CO')
    sleep(0.5)
    pyautogui.click(438,353, duration=1)
    sleep(3)
    pyautogui.click(1318,849)
    sleep(0.5)
    pyautogui.typewrite('60')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.5)
    pyautogui.click(15,800)
    pyautogui.hotkey('win')
    sleep(1)
    pyautogui.typewrite('ferramenta de captura')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.click(491,503, duration=0.5)
    sleep(1.7)
    pyautogui.moveTo(33,234)
    pyautogui.mouseDown()
    pyautogui.moveTo(1345,424, duration=0.5)  # Coordenada final
    pyautogui.mouseUp()
    sleep(1)
    pyautogui.press('printscreen')
    sleep(1)
    pyautogui.click(509,60,duration=0.5)
    sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    sleep(1)
    pyautogui.hotkey('alt', 'f4')
    sleep(1)
    pyautogui.click(849,322,duration=1)

def Stine():
    pyautogui.press('win')
    sleep(1)
    pyautogui.typewrite('google')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.click(533,518, duration=0.5)
    sleep(2)
    pyautogui.hotkey('ctrl', 't')
    sleep(1)
    pyautogui.click(328,491,duration=0.5)
    sleep(3)
    pyautogui.click(82,115, duration=1)
    sleep(2)
    pyautogui.click(1254,251, duration=0.5)
    sleep(1)
    pyautogui.typewrite('REPORT_OPERACIONAL_CARREGAMENTO_STINE_A')
    sleep(0.5)
    pyautogui.click(438,353, duration=1)
    sleep(3)
    pyautogui.click(1318,849)
    sleep(0.5)
    pyautogui.typewrite('60')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.5)
    pyautogui.click(15,800)
    pyautogui.hotkey('win')
    sleep(1)
    pyautogui.typewrite('ferramenta de captura')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.click(491,503, duration=1)
    sleep(1.7)
    pyautogui.moveTo(33,234)
    pyautogui.mouseDown()
    pyautogui.moveTo(1327,437, duration=0.5)
    pyautogui.mouseUp()
    sleep(1)
    pyautogui.press('printscreen')
    sleep(1)
    pyautogui.click(509,60,duration=0.5)
    sleep(1)
    pyautogui.hotkey('ctrl', 'c')
    sleep(1)

def whatsapp():
    sleep(1)
    pyautogui.hotkey('win')
    sleep(1)
    pyautogui.typewrite('whatsapp')
    sleep(1)
    pyautogui.press('enter')
    sleep(5)
    pyautogui.typewrite('reports')
    sleep(1)
    pyautogui.hotkey('tab')
    sleep(1)
    pyautogui.press('enter')
    sleep(2)
    pyautogui.hotkey('ctrl','v')
    sleep(1)
    pyautogui.press('enter')
    sleep(0.5)
    pyautogui.click(751,21,duration=0.5)
    sleep(1)
    pyautogui.hotkey('alt', 'f4')

def Lembrar_Amanda():
    sleep(1)
    pyautogui.hotkey('win')
    sleep(1)
    pyautogui.typewrite('whatsapp')
    sleep(1)
    pyautogui.press('enter')
    sleep(5)
    pyautogui.typewrite('amanda')
    sleep(1)
    pyautogui.hotkey('tab')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.typewrite('[BOT] Report vai ser enviado em 5 minutos!')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.click(780,18, duration=0.5)
    sleep(1)
    pyautogui.hotkey('alt','f4')
    sleep(1)

# === Execução Principal ===

escolher_opcoes()

if not executar_corteva and not executar_stine:
    pyautogui.alert("Nenhuma opção foi selecionada. O programa será encerrado.", title="Aviso", button="OK")
    exit()

# Inicia a interface de parada em uma thread separada
threading.Thread(target=interface_parada, daemon=True).start()

# Horários de 08:30 até 22:30, e inclui 00:30 manualmente
horarios_execucao = [datetime.strptime(f"{h:02d}:30", "%H:%M").time() for h in range(8, 24, 2)]
horarios_execucao.append(datetime.strptime("00:30", "%H:%M").time())

ultimo_horario_executado = None

while not parar_execucao:
    agora = datetime.now().time()

    if any(agora.hour == h.hour and agora.minute == h.minute for h in horarios_execucao):
        horario_atual_minutos = agora.hour * 60 + agora.minute
        if ultimo_horario_executado != horario_atual_minutos:
            pyautogui.alert("O REPORT SERÁ LANÇADO AGORA")
