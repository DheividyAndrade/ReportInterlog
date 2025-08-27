# === IMPORTS ===
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

# ========== CONFIG ==========

ARQUIVO_CREDENCIAIS = 'soy-surge-397101-970c2a316ba9.json'
ID_PLANILHA = '1M-VbVx94Y86uNnBUXDjPoEk1VB4kF6YyIQ8n9nkad2k'
NOME_ABA = 'Página1'
ARQUIVO_CHAVE_SALVA = 'chave_acesso.txt'

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

# ========== FUNÇÕES AUXILIARES ==========


def carregar_credenciais():
    if not os.path.exists(ARQUIVO_CREDENCIAIS):
        pyautogui.alert(
            f"Arquivo de credenciais '{ARQUIVO_CREDENCIAIS}' não encontrado.")
        return None
    try:
        creds = service_account.Credentials.from_service_account_file(
            ARQUIVO_CREDENCIAIS)
        service = build('sheets', 'v4', credentials=creds)
        return service
    except Exception as e:
        pyautogui.alert(f"Erro ao carregar as credenciais do Google:\n{e}")
        return None


def verificar_chave(chave_usuario):
    service = carregar_credenciais()
    if not service:
        return False
    try:
        sheet = service.spreadsheets()
        resultado = sheet.values().get(spreadsheetId=ID_PLANILHA,
                                       range=f"{NOME_ABA}!A2:C").execute()
        valores = resultado.get('values', [])

        for linha in valores:
            if len(linha) >= 3:
                chave, status, data_expiracao = linha[0].strip(
                ), linha[1].strip().lower(), linha[2].strip()
                if chave_usuario.strip() == chave and status == 'sim':
                    try:
                        data_exp = datetime.strptime(
                            data_expiracao, "%Y-%m-%d").date()
                        hoje = datetime.now().date()
                        if hoje <= data_exp:
                            return True
                        else:
                            pyautogui.alert("❌ Chave expirada.")
                            return False
                    except ValueError:
                        pyautogui.alert(
                            f"⚠️ Data inválida para a chave '{chave}'.")
                        return False
        return False
    except Exception as e:
        pyautogui.alert(f"Erro ao acessar a planilha:\n{e}")
        return False


def salvar_chave_local(chave):
    with open(ARQUIVO_CHAVE_SALVA, 'w') as f:
        f.write(chave)

# ========== VERIFICAÇÃO DA CHAVE ==========


chave_digitada = pyautogui.prompt("🔐 Digite sua chave de acesso:")

if not chave_digitada:
    pyautogui.alert("❌ Nenhuma chave foi digitada. Encerrando.")
    sys.exit()

if verificar_chave(chave_digitada):
    salvar_chave_local(chave_digitada)
    pyautogui.alert("✅ Chave válida! Bot liberado!")
else:
    pyautogui.alert("❌ Chave inválida, inativa ou expirada. Bot bloqueado.")
    sys.exit()

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

# ... suas funções corteva(), Stine(), LP(), whatsapp(), Lembrar_Amanda() continuam exatamente como estão ...


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


def alerta_com_fechamento():
    def fechar_depois():
        time.sleep(5)
        pyautogui.press('enter')

    threading.Thread(target=fechar_depois).start()
    pyautogui.alert("O REPORT SERÁ LANÇADO AGORA!", title="Alerta", button="OK")

def alerta_com_fechamento2():
    def fechar_depois():
        time.sleep(5)
        pyautogui.press('enter')

    threading.Thread(target=fechar_depois).start()
    pyautogui.alert("REPORT ENVIADO!", title="Alerta", button="OK")

# === CONTINUAÇÃO DA EXECUÇÃO ===

escolher_opcoes()

if not executar_corteva and not executar_stine and not executar_LP:
    pyautogui.alert(
        "Nenhuma opção foi selecionada. O programa será encerrado.", title="Aviso", button="OK")
    exit()

threading.Thread(target=interface_parada, daemon=True).start()

horarios_execucao = [time(h, 30) for h in range(8, 24, 2)]
horarios_execucao.append(time(0, 30))

horarios_lembrete_amanda = [(datetime.combine(
    datetime.today(), h) - timedelta(minutes=5)).time() for h in horarios_execucao]

ultimo_horario_executado = None
ultimo_lembrete_amanda = None

while not parar_execucao:
    agora = datetime.now().time()
    hora_atual = time(agora.hour, agora.minute)

    if hora_atual in horarios_lembrete_amanda and hora_atual != ultimo_lembrete_amanda:
        Lembrar_Amanda()
        ultimo_lembrete_amanda = hora_atual

    if hora_atual in horarios_execucao and hora_atual != ultimo_horario_executado:

        # Inicia as threads
        threading.Thread(target=alerta_com_fechamento).start()
    
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

        # Inicia as threads
        threading.Thread(target=alerta_com_fechamento2).start()

        ultimo_horario_executado = hora_atual

        # Aguarda 5 minutos antes de permitir nova execução
        for _ in range(300):
            if parar_execucao:
                break
            sleep(1)

        if parar_execucao:
            break

    sleep(1)

pyautogui.alert("Execução finalizada manualmente.",
                title="Encerrado", button="OK")
print("Programa encerrado.")
