from machine import Pin
from time import sleep

# GP28 pins that connects the led
pico_led = Pin(28,Pin.OUT)

def main():
    print('Begin')
    blinks = 25
    while blinks > 0:
        print('Blinks =', blinks)
        pico_led.value(1)
        sleep(1)
        pico_led.value(0)
        sleep(1)
        blinks = blinks - 1
    print('End')
    
main()
