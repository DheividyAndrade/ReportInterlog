import pyautogui
import time
import threading


def alerta():
    pyautogui.alert("Nenhuma opção foi selecionada. O programa será encerrado.", title="Aviso", button="OK")

def fechar_alerta():
    time.sleep(5)
    pyautogui.press('enter')
    exit()




# Inicia as threads
threading.Thread(target=alerta).start()
threading.Thread(target=fechar_alerta).start()

