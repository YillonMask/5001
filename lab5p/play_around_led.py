from machine import Pin
from time import sleep

# from top to low
buildin_led1 = Pin(28,Pin.OUT)
buildin_led2 = Pin(27,Pin.OUT)
buildin_led3 = Pin(26,Pin.OUT)
buildin_led4 = Pin(22,Pin.OUT)

def read_binary_string(string):
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
        print(four_digit_binary)
        print(four_digit_binary[5])
        print(four_digit_binary[4])
        print(four_digit_binary[3])
        print(four_digit_binary[2])
        buildin_led1.value(int(four_digit_binary[5]))
        buildin_led2.value(int(four_digit_binary[4]))
        buildin_led3.value(int(four_digit_binary[3]))
        buildin_led4.value(int(four_digit_binary[2]))
        sleep(1)
        buildin_led1.value(0)
        buildin_led2.value(0)
        buildin_led3.value(0)
        buildin_led4.value(0)
        sleep(1)
        blinks = blinks + 1
    print('End')
    
def alloff():
    buildin_led1.value(0)
    buildin_led2.value(0)
    buildin_led3.value(0)
    buildin_led4.value(0)

main()

