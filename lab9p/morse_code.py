from machine import Pin
from time import sleep
from machine import PWM

# sonar gpio15, led gpio2
pico_led = Pin(2,Pin.OUT)
pico_sonar = PWM(Pin(15))
# setting the buzzer frequency to be 1000 (higher the number higher the pitch
pico_sonar.freq(1000)


'''
space between dit or dah: is followed by a short silence, equal to the dit duration.
space between letters of a word: are separated by a space equal to three dits (one dah).
space between words: are separated by a space equal to seven dits.
'''


def morse_code(n):
    morse_code_dict = {
        'A': '.-',   'N': '-.',   '0': '-----',
        'B': '-...', 'O': '---',  '1': '.----',
        'C': '-.-.', 'P': '.--.', '2': '..---',
        'D': '-..',  'Q': '--.-', '3': '...--',
        'E': '.',    'R': '.-.',  '4': '....-',
        'F': '..-.', 'S': '...',  '5': '.....',
        'G': '--.',  'T': '-',    '6': '-....',
        'H': '....', 'U': '..-',  '7': '--...',
        'I': '..',   'V': '...-', '8': '---..',
        'J': '.---', 'W': '.--',  '9': '----.',
        'K': '-.-',  'X': '-..-', 
        'L': '.-..', 'Y': '-.--', 
        'M': '--',   'Z': '--..', ' ':',,'
    }
    
    result = []
    for char in n.upper():
        morse_code = (morse_code_dict[char])
        result.append(morse_code)
    # space between letters of word are separated by space equal to three dits
    # I only put two commas (silience seperator) here, because there is one behind each dits and dahs
    interpret = ',,'.join(result)
    print(interpret)
    for digit in interpret:
        print(digit)
        # for dits
        if digit == '.':
            pico_sonar.duty_u16(1000)
            pico_led.value(1)
            # duration of dits is 0.2s
            sleep(0.2)
            pico_sonar.duty_u16(0)
            pico_led.value(0.2)
            # duration between each dit or dah within a encoded character
            # is equal to dit duration
            sleep(1)
        # for dahs
        elif digit == '-':
            pico_sonar.duty_u16(1000)
            pico_led.value(1)
            sleep(0.6)
            pico_sonar.duty_u16(0)
            pico_led.value(0)
            sleep(0.6)
        # each dit or dah within an encoded character is followed by
        # a period of signal absence called space, equal to the dit.
        else:
            pico_sonar.duty_u16(0)
            pico_led.value(0)
            sleep(0.2)


def main():
    n = input( "Enter only upper letters, numbers and spaces: ")
    morse_code(n)


def alloff():
    #this function set all the led light off and sonar off
    pico_led.value(0)
    # pico_led2.value(1)
    # pico_led3.value(0)
    # pico_led4.value(0)
    pico_sonar.value(0)

main()


