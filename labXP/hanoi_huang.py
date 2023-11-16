"""
CS5001_5003 Fall 2023 SV
Lab XP
Ziyu Huang
"""


from machine import Pin
from time import sleep


rod_a_high = Pin(0, Pin.OUT)
rod_a_mid = Pin(1, Pin.OUT)
rod_a_low = Pin(2, Pin.OUT)
rod_a = []
rod_a_led = [rod_a_low, rod_a_mid, rod_a_high]


rod_b_high = Pin(3, Pin.OUT)
rod_b_mid = Pin(4, Pin.OUT)
rod_b_low = Pin(5, Pin.OUT)
rod_b = []
rod_b_led = [rod_b_low, rod_b_mid, rod_b_high]


rod_c_high = Pin(6, Pin.OUT)
rod_c_mid = Pin(7, Pin.OUT)
rod_c_low = Pin(8, Pin.OUT)
rod_c = []
rod_c_led = [rod_c_low, rod_c_mid, rod_c_high]


def update_led(rod, rod_led):
    for i in range(3):
        if i < len(rod):
            rod_led[i].value(1)
        else:
            rod_led[i].value(0)


def hanoi(n, src_rod, src_rod_led, aux_rod, aux_rod_led, des_rod, des_rod_led):
    """
    Honoi move for the n-th disk
    Parameters:
        src_rod: a starting disk
        where the n-th disk is placed under the (n-1) disks
        aux_rod: an empty rod
        des_rod: an empty rod, destination
    """
    if n > 1:
        hanoi(n - 1, src_rod, src_rod_led, des_rod, des_rod_led, aux_rod, aux_rod_led)
    # move the n-th disk to the des_rod
    # move out
    n_disk = src_rod.pop()
    update_led(src_rod, src_rod_led)

    # move in
    des_rod.append(n_disk)
    update_led(des_rod, des_rod_led)

    print('rod A:', rod_a, 'rod B:', rod_b, 'rod C:', rod_c)
    sleep(2)

    if n > 1:
        hanoi(n - 1, aux_rod, aux_rod_led, src_rod, src_rod_led, des_rod, des_rod_led)


def main():
    # initialization
    rod_a.append('Large')
    rod_a.append('Medium')
    rod_a.append('Small')
    update_led(rod_a, rod_a_led)
    print('rod A:', rod_a, 'rod B:', rod_b, 'rod C:', rod_c)
    sleep(2)

    hanoi(3, rod_a, rod_a_led, rod_b, rod_b_led, rod_c, rod_c_led)
    sleep(2)

    print("End")
    # close all lights
    for led in rod_a_led:
        led.value(0)
    for led in rod_b_led:
        led.value(0)
    for led in rod_c_led:
        led.value(0)


if __name__ == "__main__":
    main()
