from machine import Pin
from time import sleep

# from top to low
pico_led1 = Pin(28,Pin.OUT)
pico_led2 = Pin(27,Pin.OUT)
pico_led3 = Pin(26,Pin.OUT)
pico_led4 = Pin(22,Pin.OUT)

def read_binary_string(string):
    # this function add "0" following '0b' , making the string length to be 6
    if len(string) < 6:
        diff = 6 - len(string)
        new_string = string[:2] + "0" * diff + string[2:]
    else:
        new_string = string[:6]
    return new_string

def main():
    print('Begin')
    blinks = 0
    while blinks <= 15:
        print('Blinks =', blinks)
        binary_number = str(bin(blinks))
        four_digit_binary = read_binary_string(binary_number)
        # print out the 6 digit binary string
        print(four_digit_binary)
        # print out the last 4 digit (exclude "0b")
        print(four_digit_binary[5])
        print(four_digit_binary[4])
        print(four_digit_binary[3])
        print(four_digit_binary[2])
        pico_led1.value(int(four_digit_binary[5]))
        pico_led2.value(int(four_digit_binary[4]))
        pico_led3.value(int(four_digit_binary[3]))
        pico_led4.value(int(four_digit_binary[2]))
        sleep(1)
        pico_led1.value(0)
        pico_led2.value(0)
        pico_led3.value(0)
        pico_led4.value(0)
        sleep(1)
        blinks = blinks + 1
    print('End')
    
def alloff():
    #this function set all the led light off
    pico_led1.value(0)
    pico_led2.value(0)
    pico_led3.value(0)
    pico_led4.value(0)

main()

