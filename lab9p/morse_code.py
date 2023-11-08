from machine import Pin
from time import sleep

# pico gpio15
pico_sonar = Pin(15,Pin.OUT)
# pico_led2 = Pin(1,Pin.OUT)
# pico_led3 = Pin(2,Pin.OUT)
# pico_led4 = Pin(22,Pin.OUT)


def morse_code(n):
    morse_code_dict = {
    "A": "10",
    "B": "0111",
    "C": "0101",
    "D": "011",
    "E": "1",
    "F": "1101",
    "G": "001",
    "H": "1111",
    "I": "11",
    "J": "1000",
    "K": "010",
    "L": "1011",
    "M": "00",
    "N": "01",
    "O": "000",
    "P": "1001",
    "Q": "0010",
    "R": "010",
    "S": "111",
    "T": "0",
    "U": "110",
    "V": "1110",
    "W": "100",
    "X": "0110",
    "Y": "0100",
    "Z": "0011",
    "0": "00000",
    "1": "10000",
    "2": "11000",
    "3": "11100",
    "4": "11110",
    "5": "11111",
    "6": "01111",
    "7": "00111",
    "8": "00011",
    "9": "00001",
    " ": "0000"
    }
    for char in n:
        morse_code = int(morse_code_dict[char])
    for digit in morse_code:
        if digit == 1:
            pico_sonar.value(1)
            sleep(1)
            pico_sonar.value(0)
        else:
            pico_sonar.value(1)
            sleep(2)
            pico_sonar.value(0)


def main():
    n = input( "Enter only upper letter, number and space: ")
    morse_code(n)


def alloff():
    #this function set all the led light off
    # pico_led1.value(0)
    # pico_led2.value(0)
    # pico_led3.value(0)
    # pico_led4.value(0)
    pico_sonar.value(0)

main()


