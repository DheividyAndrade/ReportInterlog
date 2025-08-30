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
import time


def corteva():
    # Seu código pyautogui para Corteva aqui
    print("Executando Corteva...")
    # Coletando Informações Report
    pyautogui.press('win')
    sleep(0.3)
    pyautogui.typewrite('google')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.3)
    pyautogui.click(533, 518)
    sleep(0.5)
    pyautogui.hotkey('ctrl', 't')
    sleep(0.3)
    pyautogui.click(328, 491)
    sleep(5)
    pyautogui.click(82, 115, duration=1)
    sleep(2)

    # Clicando em busca
    pyautogui.click(1254, 251, duration=0.5)
    sleep(1)
    pyautogui.typewrite('REPORT_OPERACIONAL_CARREGAMENTO_CO')
    sleep(0.5)
    pyautogui.click(438, 353, duration=1)
    sleep(11)
    pyautogui.click(1318, 849)
    sleep(0.5)
    pyautogui.typewrite('60')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.5)
    pyautogui.click(15, 800)

    # Abrindo captura
    pyautogui.hotkey('win')
    sleep(0.3)
    pyautogui.typewrite('ferramenta de captura')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.3)
    pyautogui.click(491, 503, duration=0.5)
    sleep(1.7)

    # Arrastando print e copiando
    pyautogui.moveTo(33, 234)  # Coordenada inicial
    pyautogui.mouseDown()
    pyautogui.moveTo(1358,597, duration=0.5)  # Coordenada final
    pyautogui.mouseUp()
    sleep(1)
    pyautogui.press('printscreen')
    sleep(0.3)
    pyautogui.click(509, 60, duration=0.5)
    sleep(0.3)
    pyautogui.hotkey('ctrl', 'c')
    sleep(0.3)
    pyautogui.hotkey('alt', 'f4')
    sleep(0.5)
    pyautogui.hotkey('tab')
    sleep(0.3)
    pyautogui.press('enter')

def Stine():
    # Seu código pyautogui para Stine aqui
    print("Executando Stine...")
    pyautogui.press('win')
    sleep(0.3)
    pyautogui.typewrite('google')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.3)
    pyautogui.click(533, 518)
    sleep(0.5)
    pyautogui.hotkey('ctrl', 't')
    sleep(0.3)
    pyautogui.click(328, 491)
    sleep(5)
    pyautogui.click(82, 115, duration=1)
    sleep(2)

    # Clicando em busca
    pyautogui.click(1254, 251, duration=0.5)
    sleep(1)
    pyautogui.typewrite('REPORT_OPERACIONAL_CARREGAMENTO_STINE_A')
    sleep(0.5)
    pyautogui.click(438, 353, duration=1)
    sleep(11)
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
    pyautogui.moveTo(1358,597, duration=0.5)  # Coordenada final
    pyautogui.mouseUp()
    sleep(1)
    pyautogui.press('printscreen')
    sleep(0.3)
    pyautogui.click(509, 60, duration=0.5)
    sleep(0.3)
    pyautogui.hotkey('ctrl', 'c')
    sleep(0.3)
    pyautogui.hotkey('alt', 'f4')
    sleep(0.5)
    pyautogui.hotkey('tab')
    sleep(0.3)
    pyautogui.press('enter')

def LP():
    # Seu código pyautogui para Corteva aqui
    print("Executando Corteva...")
    # Coletando Informações Report
    pyautogui.press('win')
    sleep(0.3)
    pyautogui.typewrite('google')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(0.3)
    pyautogui.click(533, 518)
    sleep(0.5)
    pyautogui.hotkey('ctrl', 't')
    sleep(0.3)
    pyautogui.click(328, 491)
    sleep(5)
    pyautogui.click(82, 115, duration=1)
    sleep(2)

    # Clicando em busca
    pyautogui.click(1254, 251, duration=0.5)
    sleep(1)
    pyautogui.typewrite('REPORT_OPERACIONAL_CARREGAMENTO_LP')
    sleep(0.5)
    pyautogui.click(438, 353, duration=1)
    sleep(11)
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
    pyautogui.moveTo(1358,597, duration=0.5)  # Coordenada final
    pyautogui.mouseUp()
    sleep(1)
    pyautogui.press('printscreen')
    sleep(0.3)
    pyautogui.click(509, 60, duration=0.5)
    sleep(0.3)
    pyautogui.hotkey('ctrl', 'c')
    sleep(0.3)
    pyautogui.hotkey('alt', 'f4')
    sleep(0.5)
    pyautogui.hotkey('tab')
    sleep(0.3)
    pyautogui.press('enter')

def whatsapp():
    # Seu código pyautogui para enviar via WhatsApp aqui
    print("Enviando via WhatsApp...")
    # Enviando Report para Whatsapp
    sleep(0.3)
    pyautogui.hotkey('win')
    sleep(0.3)
    pyautogui.typewrite('whatsapp')
    sleep(0.5)
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
    pyautogui.click(751, 21)
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


corteva()
whatsapp()
sleep(0.3)

'''
Stine()
whatsapp()
sleep(0.3)
'''

LP()
whatsapp()
sleep(0.3)

