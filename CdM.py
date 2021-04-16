# Requirements = [ pip install colorama selenium ]

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from colorama import init, Fore
import time

init()
print(Fore.LIGHTYELLOW_EX + "[·] Cargando..." + Fore.RESET)

# -------- Actividades -------- #
def Flower_Pawer():
    browser.get("https://www.corazondemelon.es/s1/games/flower-pawer")
    try:
        browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/app-modal/div/div[2]/div/button").click()
        canvas = browser.find_element_by_xpath("/html/body/app-amoursucre/index/app-connected-page/div/div[3]/div[1]/games/flower-pawer/page-sheet-container/div/stage/canvas")

        drawing = ActionChains(browser)\
            .move_to_element_with_offset(canvas, 0,0)\
            .release()
        drawing.perform()

        for x in range(29):
            drawing = ActionChains(browser)\
                .move_by_offset(x, x)\
                .click()\
                .release()
            drawing.perform()

        time.sleep(5)
        check = True

        print(Fore.LIGHTYELLOW_EX + "\t↳ Waiting..." + Fore.RESET)
        while check == True:
            try:
                browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/game-gain/app-modal/div/div/button").click()
                #print("\t↳" + Fore.LIGHTMAGENTA_EX + browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/game-gain/app-modal/div/div/div/i18n/span").text)
                check = False
            except:
                None
        print(Fore.LIGHTGREEN_EX + "[·] Actividad " + Fore.LIGHTYELLOW_EX + "[Flower Pawer]" + Fore.LIGHTGREEN_EX + " completada!" + Fore.RESET)

    except:
        print(Fore.LIGHTRED_EX + "[·] Actividad "  + Fore.LIGHTYELLOW_EX + "[Flower Pawer]" + Fore.LIGHTRED_EX + " ya completada." + Fore.RESET)

def Rasca_y_gana():
    browser.get("https://www.corazondemelon.es/s2/games/cash")
    try:
        browser.find_element_by_xpath("/html/body/div[2]/div[2]/div/app-modal/div/div[2]/div/button").click()
        canvas = browser.find_element_by_xpath("/html/body/app-amoursucre/index/app-connected-page/div/div[3]/div[1]/games/cash/page-sheet-container/div/stage/canvas")
        drawing = ActionChains(browser)\
            .move_to_element_with_offset(canvas, 0,0)\
            .click_and_hold(canvas)\
            .move_by_offset(-50, -50)\
            .move_by_offset(0, 140)\
            .move_by_offset(100, 0)\
            .move_by_offset(0, -160)\
            .move_by_offset(-90, 0)\
            .move_by_offset(0, 140)\
            .move_by_offset(90, 0)\
            .move_by_offset(0, -90)\
            .move_by_offset(-70, 0)\
            .move_by_offset(0, 120)\
            .release()
        drawing.perform()
        print(Fore.LIGHTGREEN_EX + "[·] Actividad " + Fore.LIGHTYELLOW_EX + "[Rasca y gana]" + Fore.LIGHTGREEN_EX + " completada!" + Fore.RESET)

    except:
        print(Fore.LIGHTRED_EX + "[·] Actividad "  + Fore.LIGHTYELLOW_EX + "[Rasca y gana]" + Fore.LIGHTRED_EX + " ya completada." + Fore.RESET)

# -------- Start -------- #
def start(name):
    Rasca_y_gana()
    Flower_Pawer()
    print(Fore.GREEN + "[·] Actividades de la cuenta " + Fore.LIGHTWHITE_EX + f"[{name}]" + Fore.GREEN + " completadas." + Fore.RESET)
    
    browser.get("https://www.corazondemelon.es/s1/home")
    try: browser.find_element_by_xpath("/html/body/app-amoursucre/index/app-connected-page/div/div[1]/panel-connected/div/div[4]/a[4]/div").click()
    except: print(Fore.LIGHTRED_EX + "[·] Cierre de sesión fallido." + Fore.RESET)
    time.sleep(2)

# -------- Login -------- #
cuentas = {
        "null": {
            "usuario": "",
            "contraseña": ""
    },
        "null": {
            "usuario": "",
            "contraseña": ""
    },
        "null": {
            "usuario": "",
            "contraseña": ""
    },
        "null": {
            "usuario": "",
            "contraseña": ""
    },
        "null": {
            "usuario": "",
            "contraseña": ""
    },
        "null": {
            "usuario": "",
            "contraseña": ""
    }
 }

def login(name, user, pswd):
    print(Fore.LIGHTBLUE_EX + "\n# ======================================== #\n" + Fore.LIGHTCYAN_EX + "Name: " + Fore.LIGHTWHITE_EX + name + "\n" + Fore.LIGHTCYAN_EX + "Usuario: " + Fore.LIGHTWHITE_EX + user + "\n" + Fore.LIGHTCYAN_EX + "Contraseña: " + Fore.LIGHTWHITE_EX + pswd + Fore.LIGHTBLUE_EX + "\n# ======================================== #" + Fore.RESET)
    browser.get("https://www.corazondemelon.es")
    time.sleep(1)
    browser.find_element_by_xpath('/html/body/app-amoursucre/index/app-disconnected-page/connection-bar/form/label/input').send_keys(user)
    browser.find_element_by_xpath('/html/body/app-amoursucre/index/app-disconnected-page/connection-bar/form/span/input').send_keys(pswd)
    browser.find_element_by_xpath("/html/body/app-amoursucre/index/app-disconnected-page/connection-bar/form/input").click()
    time.sleep(2)

    try:
        browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/app-modal-error/app-modal/div/div[1]")
        print(Fore.RED + "[·] Cuenta no válida" + Fore.RESET)
        return
    except:
        start(name)

acc_num = len(cuentas)

for cuenta in cuentas:
    if cuenta == "null": acc_num = acc_num -1

if acc_num == 0:
    print(Fore.LIGHTRED_EX + "[·] No hay cuentas registradas..." + Fore.RESET)
else:
    browser = webdriver.Chrome(executable_path='./chromedriver')
    print(Fore.LIGHTMAGENTA_EX + "[·] Cuentas registradas: " + Fore.LIGHTWHITE_EX + str(acc_num) + Fore.RESET)
    for cuenta in cuentas:
        if not cuenta == "null":
            login(cuenta, cuentas[cuenta]["usuario"], cuentas[cuenta]["contraseña"])    
    browser.close()
    input(Fore.LIGHTMAGENTA_EX + "\nPresiona cualquier tecla para cerrar :3" + Fore.RESET)
