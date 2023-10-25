from machine import Pin
from time import sleep

# from top to low
pico_led1 = Pin(0,Pin.OUT)
pico_led2 = Pin(1,Pin.OUT)
pico_led3 = Pin(2,Pin.OUT)
# pico_led4 = Pin(22,Pin.OUT)


def do_something(n):
    if n > 0:
        do_something(n - 1)
        print(n, end="")
        if n == 1:
            pico_led1.value(1)
            sleep(1)
            pico_led1.value(0)
            sleep(1)
        elif n == 2:
            pico_led2.value(1)
            sleep(1)
            pico_led2.value(0)
            sleep(1)
        else:
            pico_led3.value(1)
            sleep(1)
            pico_led3.value(0)
            sleep(1)
        do_something(n - 1)


def main():
    n = int(input("Please enter an integer between 1 and 3 exclusive: "))
    do_something(n)


def alloff():
    #this function set all the led light off
    pico_led1.value(0)
    pico_led2.value(0)
    pico_led3.value(0)
    # pico_led4.value(0)

main()

