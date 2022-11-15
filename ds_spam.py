import pyautogui, time
import config

print("""             _ _  _                     _            
 _   _ _ __ (_) || |   ___  _ __     __| | _____   __
| | | | '_ \| | || |_ / _ \| '_ \   / _` |/ _ \ \ / /
| |_| | | | | |__   _| (_) | | | | | (_| |  __/\ V / 
 \__,_|_| |_|_|  |_|  \___/|_| |_|  \__,_|\___| \_/  
                                                    \n""")

if config.config_on == "false":
    kd1 = input("select speed for send message -")
    kd2 = input("select time of minipause -")
    kd3 = input("select number of while -")
    kd4 = input("select messages of one while -")
elif config.config_on == "true":
    kd1 = config.kd1
    kd2 = config.kd2
    kd3 = config.kd3
    kd4 = config.kd4
    print("settings loaded from config")


pyautogui.alert("start spam")


time.sleep(3)
for y in range(int(kd3)):
    for i in range(int(kd4)):
        pyautogui.hotkey("ctrl", "v")
        pyautogui.press("enter")
        time.sleep(float(kd1))
    time.sleep(float(kd2))
    pyautogui.press("enter")
    pyautogui.click()
    pyautogui.hotkey("ctrl", "a")
    pyautogui.press("backspase")
pyautogui.alert("well done :)")