from datetime import datetime, time, timedelta
import pyautogui
from time import sleep
import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
from PIL import Image, ImageTk
import threading
import queue
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os
import json
from google.oauth2 import service_account
from googleapiclient.discovery import build
import requests
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from threading import Thread



# ========== SPLASH SCREEN ==========


def mostrar_splash():
    splash = tk.Tk()
    splash.overrideredirect(True)
    splash.geometry("400x300+500+300")  # Centraliza
    splash.configure(bg="black")

    try:
        imagem = Image.open("logo.jpg")
        imagem = imagem.resize((100, 100))
        imagem_tk = ImageTk.PhotoImage(imagem)
        label_img = tk.Label(splash, image=imagem_tk, bg="black")
        label_img.image = imagem_tk
        label_img.pack(pady=(30, 10))
    except Exception as e:
        print("Erro ao carregar imagem:", e)

    tk.Label(splash, text="DH Scripts", font=(
        "Helvetica", 24, "bold"), fg="white", bg="black").pack()
    tk.Label(splash, text="Iniciando...", font=("Helvetica", 12),
             fg="gray", bg="black").pack(pady=(10, 0))
    # Contato no canto inferior direito
    contato_label = tk.Label(splash, text="Cel. (82) 99121-7317",
                             font=("Helvetica", 10),
                             fg="white", bg="black")
    contato_label.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    def fechar():
        splash.destroy()

    splash.after(5000, fechar)
    splash.mainloop()


# ========== INÍCIO DO PROGRAMA ==========
mostrar_splash()


# ========== FLUXO PRINCIPAL ==========

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
            messagebox.showwarning(
                "Atenção", "Você precisa selecionar ao menos uma opção.")
        else:
            janela.destroy()

    janela = tk.Tk()
    janela.title("Selecionar Relatórios")
    janela.geometry("300x250")

    tk.Label(janela, text="Selecione os relatórios que deseja enviar:").pack(pady=10)

    var_corteva = tk.BooleanVar()
    var_stine = tk.BooleanVar()
    var_LP = tk.BooleanVar()

    tk.Checkbutton(janela, text="Corteva + WhatsApp",
                   variable=var_corteva).pack(anchor='w', padx=20)
    tk.Checkbutton(janela, text="Stine + WhatsApp",
                   variable=var_stine).pack(anchor='w', padx=20)
    tk.Checkbutton(janela, text="LP + WhatsApp",
                   variable=var_LP).pack(anchor='w', padx=20)

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
    tk.Button(janela_parada, text="Parar Agora",
              command=parar, fg="white", bg="red").pack()
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
    pyautogui.click(533, 518, duration=0.5)
    sleep(2)
    pyautogui.hotkey('ctrl', 't')
    sleep(1)
    pyautogui.click(328, 491, duration=0.5)
    sleep(5)
    pyautogui.click(82, 115, duration=1)
    sleep(2)

    # Clicando em busca
    pyautogui.click(1254, 251, duration=0.5)
    sleep(1)
    pyautogui.typewrite('REPORT_OPERACIONAL_CARREGAMENTO_CO')
    sleep(0.5)
    pyautogui.click(438, 353, duration=1)
    sleep(10)
    pyautogui.click(1318, 849)
    sleep(0.5)
    pyautogui.typewrite('60')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.5)
    pyautogui.click(15, 800)

    # Abrindo captura
    pyautogui.hotkey('win')
    sleep(1)
    pyautogui.typewrite('ferramenta de captura')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.click(491, 503, duration=0.5)
    sleep(1.7)

    # Arrastando print e copiando
    pyautogui.moveTo(33, 234)  # Coordenada inicial
    pyautogui.mouseDown()
    pyautogui.moveTo(1370, 469, duration=0.5)  # Coordenada final
    pyautogui.mouseUp()
    sleep(1)
    pyautogui.press('printscreen')
    sleep(1)
    pyautogui.click(509, 60, duration=0.5)
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
    pyautogui.click(533, 518, duration=0.5)
    sleep(2)
    pyautogui.hotkey('ctrl', 't')
    sleep(1)
    pyautogui.click(328, 491, duration=0.5)
    sleep(5)
    pyautogui.click(82, 115, duration=1)
    sleep(2)

    # Clicando em busca
    pyautogui.click(1254, 251, duration=0.5)
    sleep(1)
    pyautogui.typewrite('REPORT_OPERACIONAL_CARREGAMENTO_STINE_A')
    sleep(0.5)
    pyautogui.click(438, 353, duration=1)
    sleep(10)
    pyautogui.click(1318, 849)
    sleep(0.5)
    pyautogui.typewrite('60')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.5)
    pyautogui.click(15, 800)

    # Abrindo captura
    pyautogui.hotkey('win')
    sleep(1)
    pyautogui.typewrite('ferramenta de captura')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.click(491, 503, duration=1)
    sleep(1.7)

    # Arrastando print e copiando
    pyautogui.moveTo(33, 234)  # Coordenada inicial
    pyautogui.mouseDown()
    pyautogui.moveTo(1327, 437, duration=0.5)  # Coordenada final
    pyautogui.mouseUp()
    sleep(1)
    pyautogui.press('printscreen')
    sleep(1)
    pyautogui.click(509, 60, duration=0.5)
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
    pyautogui.click(533, 518, duration=0.5)
    sleep(2)
    pyautogui.hotkey('ctrl', 't')
    sleep(1)
    pyautogui.click(328, 491, duration=0.5)
    sleep(3)
    pyautogui.click(82, 115, duration=1)
    sleep(2)

    # Clicando em busca
    pyautogui.click(1254, 251, duration=0.5)
    sleep(1)
    pyautogui.typewrite('REPORT_OPERACIONAL_CARREGAMENTO_LP')
    sleep(0.5)
    pyautogui.click(438, 353, duration=1)
    sleep(10)
    pyautogui.click(1318, 849)
    sleep(1)
    pyautogui.typewrite('60')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.5)
    pyautogui.click(15, 800)

    # Abrindo captura
    pyautogui.hotkey('win')
    sleep(1)
    pyautogui.typewrite('ferramenta de captura')
    sleep(1)
    pyautogui.press('enter')
    sleep(1)
    pyautogui.click(491, 503, duration=0.5)
    sleep(1.7)

    # Arrastando print e copiando
    pyautogui.moveTo(33, 234)  # Coordenada inicial
    pyautogui.mouseDown()
    pyautogui.moveTo(1370, 469, duration=0.5)  # Coordenada final
    pyautogui.mouseUp()
    sleep(1)
    pyautogui.press('printscreen')
    sleep(1)
    pyautogui.click(509, 60, duration=0.5)
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
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)
    pyautogui.press('enter')
    sleep(0.5)
    pyautogui.click(751, 21, duration=0.5)
    sleep(1)
    pyautogui.hotkey('alt', 'f4')


def Lembrar_Amanda():
    # Configurações do remetente (quem envia)
    email_remetente = "deividyandradee@gmail.com"
    senha = "vlpn jeuk bslb jeso"  # não é a senha normal! É a senha de APP do Gmail

    # Configurações do destinatário (quem recebe)
    email_destinatario = "pcl.rv@interlogsolucoes.com.br"

    # Criando o e-mail
    mensagem = MIMEMultipart()
    mensagem["From"] = email_remetente
    mensagem["To"] = email_destinatario
    mensagem["Subject"] = "REPORT ALERTA!"

    # Corpo do e-mail
    corpo = "O REPORT SERA ENVIADO EM 5 MINUTOS!. 🚀"
    mensagem.attach(MIMEText(corpo, "plain"))

    # Conectando ao servidor do Gmail e enviando
    try:
        servidor = smtplib.SMTP("smtp.gmail.com", 587)
        servidor.starttls()
        servidor.login(email_remetente, senha)
        servidor.sendmail(email_remetente, email_destinatario,
                          mensagem.as_string())
        servidor.quit()
        print("✅ E-mail enviado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")


def mostrar_alerta(mensagem, cor_fundo):
    def janela():
        root = tk.Tk()
        root.overrideredirect(True)  # Remove bordas
        root.attributes("-topmost", True)  # Sempre na frente
        root.configure(bg=cor_fundo)

        # Centralizar a janela
        largura, altura = 400, 100
        x = (root.winfo_screenwidth() // 2) - (largura // 2)
        y = (root.winfo_screenheight() // 2) - (altura // 2)
        root.geometry(f"{largura}x{altura}+{x}+{y}")

        label = tk.Label(
            root,
            text=mensagem,
            font=("Arial", 16, "bold"),
            fg="white",
            bg=cor_fundo
        )
        label.pack(expand=True, fill="both")

        # Fecha sozinho em 5 segundos
        root.after(5000, root.destroy)
        root.mainloop()

    Thread(target=janela, daemon=True).start()


# === CONTINUAÇÃO DA EXECUÇÃO ===

escolher_opcoes()

if not executar_corteva and not executar_stine and not executar_LP:
    pyautogui.alert(
        "Nenhuma opção foi selecionada. O programa será encerrado.", title="Aviso", button="OK")
    exit()

threading.Thread(target=interface_parada, daemon=True).start()

# 🚀 MODO DE TESTE: Executa a cada 10 segundos em vez de esperar horários reais
intervalo_execucao = 10  # segundos
intervalo_lembrete = 5   # segundos antes da execução

ultimo_exec = datetime.now()

while not parar_execucao:
    agora = datetime.now()

    # Dispara lembrete alguns segundos antes
    if (agora - ultimo_exec).total_seconds() >= (intervalo_execucao - intervalo_lembrete):
       ''' Lembrar_Amanda()'''

    # Dispara execução completa
    if (agora - ultimo_exec).total_seconds() >= intervalo_execucao:
        mostrar_alerta("REPORTE SERÁ INICIALIZADO!", "red")
        sleep(6)
        if executar_corteva:
            corteva()
            whatsapp()
            sleep(0.3)

        if executar_stine:
            Stine()
            whatsapp()
            sleep(0.3)

        if executar_LP:
            LP()
            whatsapp()
            sleep(0.3)

        mostrar_alerta("REPORT ENVIADO!", "green")

        ultimo_exec = agora  # reinicia o timer

    sleep(1)

pyautogui.alert("Execução finalizada manualmente.",
                title="Encerrado", button="OK")
print("Programa encerrado.")
