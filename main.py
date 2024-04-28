#---------IMPORTS--------
import network
import urequests 
import utime
import ujson
from random import randint
from picozero import RGBLED
from machine import Pin, Timer, PWM
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

#---------PINS--------
rgb = RGBLED(red = 18, green = 17, blue = 16)
i2c=I2C(0,scl=Pin(1),sda=Pin(0),freq=200000)
oled = SSD1306_I2C(128,64,i2c)

#---------CONNECTION--------
wlan = network.WLAN(network.STA_IF)
wlan.active(True)

ssid = 'IIM_Private'
password = 'Creatvive_Lab_2023'
wlan.connect(ssid, password)
url = "https://hp-api.lainocs.fr/characters/"

while not wlan.isconnected():
    print("pas connecté au wifi")
    utime.sleep(1)
    
#---------TABLE-----------    
name = ["harry-potter","Cho-Chang","Cedric-Diggory","Vincent-Crabbe"]

#---------PROGRAM--------
while(True) :
    try:
        PrsRandom = randint(0,3)
        print("GET")
        request = urequests.get(url + name[PrsRandom])
        
        resultat = request.json()
        house = resultat['house']
        named = resultat['name']
        print(house)
        print(named)

        oled.fill(0)
        oled.text(house, 32, 0)
        oled.text(named, 0, 40)
        oled.show()
        
        if house == 'Gryffindor' :
            rgb.color=(255,0,0)
        elif house == 'Ravenclaw' :
            rgb.color=(0,0,255)
        elif house == 'Hufflepuff' :
            rgb.color=(255,255,0)
        elif house == 'Slytherin':
            rgb.color=(0,255,0)
        elif house == '' :
            rgb.color = (255,255,255)

        request.close()
        
        utime.sleep(1)

    except Exception as e:
        print(e)