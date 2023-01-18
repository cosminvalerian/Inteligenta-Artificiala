import requests
import json
import cv2
import numpy as np
import pytesseract as pt
import imutils

API_KEY = "40af8eb797b82b3e61432a4238dd4e1a"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"



city=input("Introdu numele orasului: ")
request_url= f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code==200:
    data=response.json()
    #print(data)
    vreme=data['weather'][0]['description']
    temperature=round(data["main"]["temp"]-273.15,2)
    viteza_vant= data["wind"]["speed"]
    umiditate=data["main"]["humidity"]
    print("Vremea: ",vreme)
    print("Temperatura: ",temperature)
    print("Vant: ",viteza_vant)
    print("Umiditatea: ",umiditate)
    f = open('date_vreme.txt', 'w')
    f.write("Vremea: "+str(vreme)+"\n")
    f.write("Temperatura: "+str(temperature)+"\n")
    f.write("Vant: "+str(viteza_vant)+"\n")
    f.write("Umiditate: "+str(umiditate)+"\n")
else:
    print("Am intampinat o eroare")