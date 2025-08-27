import pyautogui
import time
import threading



def alerta_com_fechamento():
    def fechar_depois():
        time.sleep(5)
        pyautogui.press('enter')

    threading.Thread(target=fechar_depois).start()
    pyautogui.alert("O REPORT SERÁ LANÇADO AGORA!", title="Alerta", button="OK")



threading.Thread(target=alerta_com_fechamento).start()
