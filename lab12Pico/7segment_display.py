from machine import Pin
from time import sleep
import json

#led light
pico_A = Pin(0,Pin.OUT)
pico_B = Pin(1,Pin.OUT)
pico_C = Pin(2,Pin.OUT)
pico_D = Pin(3,Pin.OUT)
pico_E = Pin(4,Pin.OUT)
pico_F = Pin(5,Pin.OUT)
pico_G = Pin(6,Pin.OUT)



def seven_segment_display():
    user_input = input("please input a number or a letter: ")
    with open("data.json", "r") as f:
        data = json.load(f)
        for key, value in data.items():
            if key == user_input:
                result = value
                for i, item in enumerate(result):
                    index = i
                    onff = item
                    Pin(index, Pin.OUT).value(onff)
        
                    
                
            
    

def allon():
    #this function set all the led light on
    pico_A.value(1)
    pico_B.value(1)
    pico_C.value(1)
    pico_D.value(1)
    pico_E.value(1)
    pico_F.value(1)
    pico_G.value(1)

def alloff():
    #this function set all the led light off
    pico_A.value(0)
    pico_B.value(0)
    pico_C.value(0)
    pico_D.value(0)
    pico_E.value(0)
    pico_F.value(0)
    pico_G.value(0)
    
    
seven_segment_display()