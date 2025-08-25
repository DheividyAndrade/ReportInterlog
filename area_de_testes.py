import tkinter as tk
from tkinter import messagebox
import pyautogui
from time import sleep
import threading
from datetime import datetime, time
import pyautogui
from time import sleep
import tkinter as tk
from tkinter import scrolledtext
import threading
import queue
import time
import pyautogui._pyautogui_win
import random
from tkinter import ttk
from tkinter import messagebox
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
import requests
from google.oauth2.service_account import Credentials
import sys
from datetime import datetime


executar_corteva = False
executar_stine = False
executar_LP = False
parar_execucao = False

def escolher_opcoes():
    def iniciar():
        global executar_corteva, executar_stine, executar_LP
        executar_corteva = var_corteva.get()
        executar_stine = var_stine.get()
        executar_LP = var_LP.get()
        if not executar_corteva and not executar_stine and not executar_LP:
            messagebox.showwarning("Atenção", "Você precisa selecionar ao menos uma opção.")
        else:
            janela.destroy()

    janela = tk.Tk()
    janela.title("Selecionar Relatórios")
    janela.geometry("300x250")

    tk.Label(janela, text="Selecione os relatórios que deseja enviar:").pack(pady=10)

    var_corteva = tk.BooleanVar()
    var_stine = tk.BooleanVar()
    var_LP = tk.BooleanVar()

    tk.Checkbutton(janela, text="Corteva + WhatsApp", variable=var_corteva).pack(anchor='w', padx=20)
    tk.Checkbutton(janela, text="Stine + WhatsApp", variable=var_stine).pack(anchor='w', padx=20)
    tk.Checkbutton(janela, text="LP + WhatsApp", variable=var_LP).pack(anchor='w', padx=20)

    tk.Button(janela, text="Iniciar", command=iniciar).pack(pady=20)
    janela.mainloop()

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

def corteva():
    # Seu código pyautogui para Corteva aqui
    print("Executando Corteva...")
    # Coletando Informações Report
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

    #Clicando em busca
    pyautogui.click(1254,251, duration=0.5)
    sleep(1)
    pyautogui.typewrite('REPORT_OPERACIONAL_CARREGAMENTO_CO')
    sleep(0.5)
    pyautogui.click(438,353, duration=1)
    sleep(10)
    pyautogui.click(1318,849)
    sleep(0.5)
    pyautogui.typewrite('60')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.5)
    pyautogui.click(15,800)

    #Abrindo captura
    pyautogui.hotkey('win')
    sleep(1)
    pyautogui.typewrite('ferramenta de captura')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.click(491,503, duration=0.5)
    sleep(1.7)

    #Arrastando print e copiando
    pyautogui.moveTo(33,234)  # Coordenada inicial
    pyautogui.mouseDown()
    pyautogui.moveTo(1370,469, duration=0.5)  # Coordenada final
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
    pyautogui.hotkey('tab')
    sleep(1)
    pyautogui.press('enter')

def Stine():
    # Seu código pyautogui para Stine aqui
    print("Executando Stine...")
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

    #Clicando em busca
    pyautogui.click(1254,251, duration=0.5)
    sleep(1)
    pyautogui.typewrite('REPORT_OPERACIONAL_CARREGAMENTO_STINE_A')
    sleep(0.5)
    pyautogui.click(438,353, duration=1)
    sleep(10)
    pyautogui.click(1318,849)
    sleep(0.5)
    pyautogui.typewrite('60')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.5)
    pyautogui.click(15,800)

    #Abrindo captura
    pyautogui.hotkey('win')
    sleep(1)
    pyautogui.typewrite('ferramenta de captura')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.click(491,503, duration=1)
    sleep(1.7)

    #Arrastando print e copiando
    pyautogui.moveTo(33,234)  # Coordenada inicial
    pyautogui.mouseDown()
    pyautogui.moveTo(1327,437, duration=0.5)  # Coordenada final
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
    pyautogui.hotkey('tab')
    sleep(1)
    pyautogui.press('enter')

def LP():
    # Seu código pyautogui para Corteva aqui
    print("Executando Corteva...")
    # Coletando Informações Report
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

    #Clicando em busca
    pyautogui.click(1254,251, duration=0.5)
    sleep(1)
    pyautogui.typewrite('REPORT_OPERACIONAL_CARREGAMENTO_LP')
    sleep(0.5)
    pyautogui.click(438,353, duration=1)
    sleep(10)
    pyautogui.click(1318,849)
    sleep(1)
    pyautogui.typewrite('60')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.5)
    pyautogui.click(15,800)

    #Abrindo captura
    pyautogui.hotkey('win')
    sleep(1)
    pyautogui.typewrite('ferramenta de captura')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.click(491,503, duration=0.5)
    sleep(1.7)

    #Arrastando print e copiando
    pyautogui.moveTo(33,234)  # Coordenada inicial
    pyautogui.mouseDown()
    pyautogui.moveTo(1370,469, duration=0.5)  # Coordenada final
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
    pyautogui.hotkey('tab')
    sleep(1)
    pyautogui.press('enter')

def whatsapp():
    # Seu código pyautogui para enviar via WhatsApp aqui
    print("Enviando via WhatsApp...")
     # Enviando Report para Whatsapp
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
    # Seu código para lembrar Amanda no WhatsApp
    print("Lembrando Amanda...")
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

     
# === Início da execução principal ===

escolher_opcoes()

if not executar_corteva and not executar_stine and not executar_LP:
    pyautogui.alert("Nenhuma opção foi selecionada. O programa será encerrado.", title="Aviso", button="OK")
    exit()

threading.Thread(target=interface_parada, daemon=True).start()

# Horários fixos: 08:30, 10:30, ..., 22:30, 00:30
horarios_execucao = [time(h, 30) for h in range(8, 24, 2)]
horarios_execucao.append(time(0, 30))

ultimo_horario_executado = None

while not parar_execucao:
    agora = datetime.now().time()
    hora_atual = time(agora.hour, agora.minute)

    if hora_atual in horarios_execucao and hora_atual != ultimo_horario_executado:
        pyautogui.alert("O REPORT SERÁ LANÇADO AGORA!", title="Alerta", button="OK")

        if executar_corteva:
            corteva()
            whatsapp()
            print('Report Corteva Enviado')
            sleep(0.3)

        if executar_stine:
            Stine()
            whatsapp()
            print('Report Stine Enviado')
            sleep(0.3)

        if executar_LP:
            LP()
            whatsapp()
            print('Report LP Enviado')
            sleep(0.3)

        pyautogui.alert("O REPORT FOI LANÇADO COM SUCESSO!", title="Alerta", button="OK")

        ultimo_horario_executado = hora_atual

        for _ in range(300):
            if parar_execucao:
                break
            sleep(1)

        if parar_execucao:
            break

        pyautogui.alert("Lembrando a Amanda...", title="Alerta", button="OK")
        Lembrar_Amanda()
        print("Lembrei Amanda!")

    sleep(1)

pyautogui.alert("Execução finalizada manualmente.", title="Encerrado", button="OK")
print("Programa encerrado.")
