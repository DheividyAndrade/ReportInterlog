import os
import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
from PIL import Image

# === CONFIGURAÇÕES ===
CAMINHO_PRINT = "tela.png"
EDGE_DRIVER_PATH = r"C:\Users\Interlog 02\Downloads\edgedriver_win32\msedgedriver.exe"

# Links das planilhas
LINK_PLANILHA_corteva = "https://1drv.ms/x/s!AnZ-H05hJV88gZaIPO1dc7p8zIjTPpk?e=MrmXz7"
LINK_PLANILHA_stine = "https://1drv.ms/x/s!AnZ-H05hJV88gZaIRR1yeNXrHIYyhck?e=wgd25M"
LINK_PLANILHA_LP = "https://1drv.ms/x/s!AnZ-H05hJV88gZaIPO1dc7p8zIjTPpk?e=hwZMtN"

NOME_GRUPO = "GrupoTest"
MENSAGEM = "Segue o print atualizado [gráfico]"

# === CONFIGURAÇÃO DO EDGE COM PERFIL REAL ===
edge_options = Options()
edge_options.add_argument(r"user-data-dir=C:\Users\Interlog 02\AppData\Local\Microsoft\Edge\User Data")
edge_options.add_argument(r"--profile-directory=Default")
edge_options.add_argument("--start-maximized")
edge_options.add_argument("--lang=pt-BR")

service = EdgeService(executable_path=EDGE_DRIVER_PATH)
driver = webdriver.Edge(service=service, options=edge_options)

def tirar_print(link):
    driver.get(link)
    time.sleep(5)  # Tempo para carregar a planilha

    driver.save_screenshot("tela.png")

    # Coordenadas do recorte (ajuste conforme necessário)
    x, y, largura, altura = 150, 150, 1300, 450
    img = Image.open("tela.png")
    crop = img.crop((x, y, x + largura, y + altura))
    crop.save(CAMINHO_PRINT)

def whatsapp_selenium():
    driver.get("https://web.whatsapp.com")
    print("✅ Abrindo WhatsApp Web com seu perfil...")
    time.sleep(30)  # Tempo para carregar e autenticar

    caixa_pesquisa = driver.find_element(By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='3']")
    caixa_pesquisa.send_keys(NOME_GRUPO)
    time.sleep(2)

    grupo = driver.find_element(By.XPATH, f"//span[@title='{NOME_GRUPO}']")
    grupo.click()
    time.sleep(2)

    caixa_texto = driver.find_element(By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='10']")
    caixa_texto.send_keys(MENSAGEM)
    time.sleep(1)

    anexo = driver.find_element(
        By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[1]/button/span')
    anexo.click()
    time.sleep(1)

    upload = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    upload.send_keys(os.path.abspath(CAMINHO_PRINT))
    time.sleep(2)

    send_button = driver.find_element(
        By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div/span')
    send_button.click()
    time.sleep(3)

def apagar_local():
    if os.path.exists(CAMINHO_PRINT):
        os.remove(CAMINHO_PRINT)
        print("✅ Print enviado ao grupo e deletado do PC!")

# === EXECUÇÃO PRINCIPAL ===
tirar_print(LINK_PLANILHA_corteva)
whatsapp_selenium()
apagar_local()
'''
tirar_print(LINK_PLANILHA_stine)
whatsapp_selenium()
apagar_local()

tirar_print(LINK_PLANILHA_LP)
whatsapp_selenium()
apagar_local()
'''
driver.quit()
