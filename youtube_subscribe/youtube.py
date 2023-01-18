import pyautogui
import keyboard
import time

# def cautare_google():
#     if pyautogui.locateOnScreen(r'C:\Users\Cosmin\Desktop\iac\11_04\searchbar.png', confidence=0.7) != None:
#         camp_google = pyautogui.locateOnScreen(r'C:\Users\Cosmin\Desktop\iac\11_04\searchbar.png', confidence=0.7)
#         pyautogui.click(camp_google)
#         time.sleep(3)
#         pyautogui.write("https://youtube.com")
#         pyautogui.press('enter')
#         print("IMAGINEA SE AFLA PE ECRAN")
#     else:
#         print("IMAGINEA NU SE AFLA PE ECRAN")

# def cautare_youtube():
#     if pyautogui.locateOnScreen(r'C:\Users\Cosmin\Desktop\iac\11_04\yt_searchbar.png', confidence=0.7) != None:
#         camp_yt = pyautogui.locateOnScreen(r'C:\Users\Cosmin\Desktop\iac\11_04\yt_searchbar.png', confidence=0.7)
#         pyautogui.click(camp_yt)
#         time.sleep(3)
#         pyautogui.write("zona it")
#         pyautogui.press('enter')

# def sub_youtube():
#     if pyautogui.locateOnScreen(r'C:\Users\Cosmin\Desktop\iac\11_04\subscribe.png', confidence=0.7) != None:
#         sub_yt = pyautogui.locateOnScreen(r'C:\Users\Cosmin\Desktop\iac\11_04\subscribe.png', confidence=0.7)
#         pyautogui.click(sub_yt)
#         time.sleep(3)

def coordonate():
    print(pyautogui.position())
    
time.sleep(2)
#coordonate()

# time.sleep(2)
# cautare_google()
# time.sleep(2)
# cautare_youtube()
# time.sleep(2)
# sub_youtube()

time.sleep(1)
pyautogui.click(311,498)
time.sleep(3)
pyautogui.click(811,146)
pyautogui.write('Zona it')
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(481,391)
time.sleep(3)
pyautogui.click(615,683)

time.sleep(3)
pyautogui.click(224,916)
time.sleep(10)
pyautogui.click(32,75)
time.sleep(3)
pyautogui.click(630,916)
time.sleep(10)
pyautogui.click(32,75)
time.sleep(3)