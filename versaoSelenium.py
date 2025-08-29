import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options
from PIL import Image

# === CONFIGURAÇÕES ===
CAMINHO_PRINT = "excel_area.png"
# Coloque o link da sua planilha
LINK_PLANILHA = "https://docs.google.com/spreadsheets/d/1M-VbVx94Y86uNnBUXDjPoEk1VB4kF6YyIQ8n9nkad2k/edit?gid=0#gid=0"
NOME_GRUPO = "GrupoTest"  # Nome do grupo exatamente como aparece no WhatsApp
MENSAGEM = "Segue o print atualizado [gráfico]"

# === CONFIGURAÇÃO DO EDGE COM PERFIL REAL ===
# caminho do EdgeDriver
EDGE_DRIVER_PATH = r"C:\Program Files (x86)\edgedriver_win32\msedgedriver.exe"
service = EdgeService(executable_path=EDGE_DRIVER_PATH)

edge_options = Options()
# Caminho do seu perfil real do Edge
edge_options.add_argument(
    r"user-data-dir=C:\Users\SeuUsuario\AppData\Local\Microsoft\Edge\User Data")
# substitua se usar outro perfil
edge_options.add_argument(r'--profile-directory=Default')
edge_options.add_argument("--start-maximized")
edge_options.add_argument("--lang=pt-BR")

# Inicializar driver
driver = webdriver.Edge(service=service, options=edge_options)

# 1. Abrir planilha e tirar print
driver.get(LINK_PLANILHA)
time.sleep(5)  # tempo para a planilha carregar

driver.save_screenshot("tela.png")

# Coordenadas do recorte (ajuste conforme necessário)
x, y, largura, altura = 200, 150, 700, 400
img = Image.open("tela.png")
crop = img.crop((x, y, x + largura, y + altura))
crop.save(CAMINHO_PRINT)

# 2. Abrir WhatsApp Web (já logado pelo perfil)
driver.get("https://web.whatsapp.com")
print("✅ Abrindo WhatsApp Web com seu perfil...")
time.sleep(30)  # tempo para carregar

# 3. Buscar o grupo pelo nome
caixa_pesquisa = driver.find_element(
    By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='3']")
caixa_pesquisa.send_keys(NOME_GRUPO)
time.sleep(2)

grupo = driver.find_element(By.XPATH, f"//span[@title='{NOME_GRUPO}']")
grupo.click()
time.sleep(2)

# 4. Enviar mensagem de texto
caixa_texto = driver.find_element(
    By.CSS_SELECTOR, "div[contenteditable='true'][data-tab='10']")
caixa_texto.send_keys(MENSAGEM)
time.sleep(1)

# 5. Anexar o arquivo
anexo = driver.find_element(
    By.XPATH, '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[1]/button/span')
anexo.click()
time.sleep(1)

upload = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
upload.send_keys(os.path.abspath(CAMINHO_PRINT))
time.sleep(2)

# 6. Enviar
send_button = driver.find_element(
    By.XPATH, '//*[@id="app"]/div[1]/div[3]/div/div[2]/div[2]/span/div/div/div/div[2]/div/div[2]/div[2]/div/div/span')
send_button.click()
time.sleep(3)

# 7. Apagar o arquivo local
if os.path.exists(CAMINHO_PRINT):
    os.remove(CAMINHO_PRINT)
    print("✅ Print enviado ao grupo e deletado do PC!")

driver.quit()
