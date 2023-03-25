from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from colorama import init, Fore
import time, json

init()
print(Fore.LIGHTYELLOW_EX + "[·] Cargando..." + Fore.RESET)

# -------- Actividades -------- #
def Flower_Pawer(browser):
    browser.get("https://www.corazondemelon.es/s1/games/flower-pawer")
    try:
        time.sleep(1)
        browser.find_element(By.XPATH, '//*[contains(@id,"cdk-overlay")]/app-modal/div/div[2]/div/button').click()
        canvas = browser.find_element(By.XPATH, '//*[@id="pages"]/games/flower-pawer/page-sheet-container/div/stage/canvas')

        drawing = ActionChains(browser)\
            .move_to_element_with_offset(canvas, 0,0)\
            .release()
        drawing.perform()

        for x in range(20):
            drawing = ActionChains(browser)\
                .move_by_offset(x, x)\
                .click()\
                .release()
            drawing.perform()

        time.sleep(5)
        while True:
            try:
                msg = browser.find_element(By.XPATH, '//*[contains(@id,"cdk-overlay")]/game-gain/app-modal/div/div/div/i18n/span').text
                try: cant = browser.find_element(By.XPATH, '//*[contains(@id,"cdk-overlay")]/game-gain/app-modal/div/div/section/div/span').text
                except: cant = ""
                break
            except: continue

        print(Fore.LIGHTGREEN_EX + "[·] Actividad " + Fore.LIGHTYELLOW_EX + "[Flower Pawer]" + Fore.LIGHTGREEN_EX + " completada! - " + Fore.RESET + f"{msg} {cant}")

    except:
        print(Fore.LIGHTRED_EX + "[·] Actividad "  + Fore.LIGHTYELLOW_EX + "[Flower Pawer]" + Fore.LIGHTRED_EX + " ya completada." + Fore.RESET)

def Rasca_y_gana(browser):
    browser.get("https://www.corazondemelon.es/s2/games/cash")
    try:
        time.sleep(1)
        browser.find_element(By.XPATH, '//*[contains(@id,"cdk-overlay")]/app-modal/div/div[2]/div/button').click()
        canvas = browser.find_element(By.XPATH, '//*[@id="pages"]/games/cash/page-sheet-container/div/stage/canvas')
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

        time.sleep(1)
        msg = browser.find_element(By.XPATH, '//*[contains(@id,"cdk-overlay")]/game-gain/app-modal/div/div/div/i18n/span').text
        try: cant = browser.find_element(By.XPATH, '//*[contains(@id,"cdk-overlay")]/game-gain/app-modal/div/div/section/div/span').text
        except: cant = ""
        print(Fore.LIGHTGREEN_EX + "[·] Actividad " + Fore.LIGHTYELLOW_EX + "[Rasca y gana]" + Fore.LIGHTGREEN_EX + " completada! - " + Fore.RESET + f"{msg} {cant}")

    except:
        print(Fore.LIGHTRED_EX + "[·] Actividad "  + Fore.LIGHTYELLOW_EX + "[Rasca y gana]" + Fore.LIGHTRED_EX + " ya completada." + Fore.RESET)

# -------- Start -------- #
def start(browser, name):
    Rasca_y_gana(browser)
    time.sleep(2)
    Flower_Pawer(browser)
    print(Fore.GREEN + "[·] Actividades de la cuenta " + Fore.LIGHTWHITE_EX + f"[{name}]" + Fore.GREEN + " completadas." + Fore.RESET)
    
    browser.get("https://www.corazondemelon.es/s1/home")
    time.sleep(2)
    try: browser.find_element(By.XPATH, '//*[@id="panel-menu"]/a[4]/div').click()
    except: print(Fore.LIGHTRED_EX + "[·] Cierre de sesión fallido." + Fore.RESET)
    time.sleep(2)

def login(browser, name, user, pswd):
    print(Fore.LIGHTBLUE_EX + "\n# ======================================== #\n" + Fore.LIGHTCYAN_EX + "Name: " + Fore.LIGHTWHITE_EX + name + "\n" + Fore.LIGHTCYAN_EX + "Usuario: " + Fore.LIGHTWHITE_EX + user + "\n" + Fore.LIGHTCYAN_EX + "Contraseña: " + Fore.LIGHTWHITE_EX + "*" * len(pswd) + Fore.LIGHTBLUE_EX + "\n# ======================================== #" + Fore.RESET)
    browser.get("https://www.corazondemelon.es")

    time.sleep(2)

    check = True

    while check:
        try:
            browser.find_elements(By.CLASS_NAME, 'ng-pristine')[1].click()
            browser.find_elements(By.CLASS_NAME, 'ng-pristine')[1].send_keys(user)
            browser.find_elements(By.CLASS_NAME, 'ng-pristine')[0].click()
            browser.find_elements(By.CLASS_NAME, 'ng-pristine')[0].send_keys(pswd)
            browser.find_element(By.XPATH, '//*[@id="intro"]/form/input').click()
            time.sleep(2)

            check = False
        except: 
            browser.get("https://www.corazondemelon.es")
            time.sleep(2)

    try:
        browser.find_element(By.XPATH, '//*[@id="intro"]/form/input')
        print(Fore.RED + "[·] Cuenta no válida" + Fore.RESET)
        return
    except:
        start(browser, name)

def main():
    cuentas = json.loads(open("cuentas.json", "r", encoding="utf-8").read())
    acc_num = len(cuentas)
    for cuenta in cuentas:
        if cuenta == "null": acc_num = acc_num - 1

    if acc_num == 0: print(Fore.LIGHTRED_EX + "[·] No hay cuentas registradas..." + Fore.RESET)
    else:
        s = Service(ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_argument("--log-level=3")
        browser = webdriver.Chrome(service=s, options=options)
        print(Fore.LIGHTMAGENTA_EX + "[·] Cuentas registradas: " + Fore.LIGHTWHITE_EX + str(acc_num) + Fore.RESET)
        
        for cuenta in cuentas:
            if not cuenta == "null":
                login(browser, cuenta, cuentas[cuenta]["usuario"], cuentas[cuenta]["contraseña"])    
        browser.close()
        input(Fore.LIGHTMAGENTA_EX + "\nPresiona cualquier tecla para cerrar :3" + Fore.RESET)

if __name__ == "__main__": 
    main()