import pyautogui
from time import sleep
import tkinter as tk
from tkinter import messagebox
import threading

'''
# ========== CONFIG ==========

# Nome do seu JSON de credenciais
ARQUIVO_CREDENCIAIS = 'soy-surge-397101-709ce194e4f4.json'
# ID da sua planilha Google
ID_PLANILHA = '1M-VbVx94Y86uNnBUXDjPoEk1VB4kF6YyIQ8n9nkad2k'
NOME_ABA = 'Página1'  # Nome da aba na planilha
ARQUIVO_CHAVE_SALVA = 'chave_acesso.txt'

# ====================== FUNÇÕES ======================


def carregar_credenciais():
    if not os.path.exists(ARQUIVO_CREDENCIAIS):
        pyautogui.alert(
            f"Arquivo de credenciais '{ARQUIVO_CREDENCIAIS}' não encontrado.")
        return None
    try:
        creds = Credentials.from_service_account_file(ARQUIVO_CREDENCIAIS)
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
            print("Linha lida:", linha)
            if len(linha) >= 3:
                chave, status, data_expiracao = linha[0].strip(
                ), linha[1].strip().lower(), linha[2].strip()
                print(
                    f"Comparando chave {chave_usuario.strip()} com {chave} | Status: {status} | Expira: {data_expiracao}")

                if chave_usuario.strip() == chave and status == 'sim':
                    # Verifica validade da data
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
                            f"⚠️ Data inválida na planilha para a chave '{chave}'.")
                        return False

        return False
    except Exception as e:
        pyautogui.alert(f"Erro ao acessar a planilha:\n{e}")
        return False


def salvar_chave_local(chave):
    with open(ARQUIVO_CHAVE_SALVA, 'w') as f:
        f.write(chave)

# ====================== VERIFICAÇÃO ======================


chave_digitada = pyautogui.prompt("🔐 Digite sua chave de acesso:")

if not chave_digitada:
    pyautogui.alert("❌ Nenhuma chave foi digitada. Encerrando.")
    sys.exit()

if verificar_chave(chave_digitada):
    salvar_chave_local(chave_digitada)
    pyautogui.alert("✅ Chave válida! Bot liberado!")
    # Aqui você chama o seu bot
    # os.system("seu_bot.exe")
else:
    pyautogui.alert("❌ Chave inválida, inativa ou expirada. Bot bloqueado.")
    sys.exit()
'''


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

# === Suas funções existentes ===

def corteva():
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
        sleep(3)

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

    #Clicando em busca
    pyautogui.click(1254,251, duration=0.5)
    sleep(1)
    pyautogui.typewrite('REPORT_OPERACIONAL_CARREGAMENTO_STINE_A')
    sleep(1)
    pyautogui.click(438,353, duration=1)
    sleep(3)

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

def whatsapp():
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
    sleep(1)
    pyautogui.typewrite('[BOT] Report Enviado com Sucesso!')
    sleep(0.5)
    pyautogui.press('enter')
    sleep(1)
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

# Chama interface de seleção
escolher_opcoes()

# Verifica se o usuário escolheu algo
if not executar_corteva and not executar_stine:
    pyautogui.alert("Nenhuma opção foi selecionada. O programa será encerrado.", title="Aviso", button="OK")
    exit()

# Inicia a interface de parada em uma thread separada
threading.Thread(target=interface_parada, daemon=True).start()

# Loop principal
while not parar_execucao:
    pyautogui.alert("O REPORT SERÁ LANÇADO EM 5 MINUTOS!", title="Alerta", button="OK")
    sleep(7)

    if parar_execucao: break
    if executar_corteva:
        corteva()
        whatsapp()
        print('Report Corteva Enviado')
        sleep(0.3)

    if parar_execucao: break
    if executar_stine:
        Stine()
        whatsapp()
        print('Report Stine Enviado')
        sleep(0.3)

    if parar_execucao: break
    pyautogui.alert("O REPORT FOI LANÇADO COM SUCESSO!", title="Alerta", button="OK")

    # Espera 2 horas (6800 segundos)
    for _ in range(6800):
        if parar_execucao:
            break
        sleep(1)

    if parar_execucao: break

    print('Lembrando a Amanda...')
    pyautogui.alert("Lembrando a Amanda...", title="Alerta", button="OK")
    Lembrar_Amanda()
    print('Lembrei :)')

    for _ in range(400):
        if parar_execucao:
            break
        sleep(1)

pyautogui.alert("Execução finalizada manualmente.", title="Encerrado", button="OK")
print("Programa encerrado.")
