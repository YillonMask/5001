"""
CS5001_5003 Fall 2023 SV
Lab XP
Xinrui Yi
"""


from machine import Pin
from time import sleep


led_A1 = Pin(0,Pin.OUT)
led_A2 = Pin(1,Pin.OUT)
led_A3 = Pin(2,Pin.OUT)
led_B1 = Pin(3,Pin.OUT)
led_B2 = Pin(4,Pin.OUT)
led_B3 = Pin(5,Pin.OUT)
led_C1 = Pin(6,Pin.OUT)
led_C2 = Pin(7,Pin.OUT)
led_C3 = Pin(8,Pin.OUT)


def tower_of_hanoi(num_disks, from_rod, to_rod):
    '''
    function: tower_of_hanoi, the starting point for our program
    params:   num_disks to be moved
              from_rod, the starting rod for the disks
              to_rod, the target to move the disks to
    '''           
    move_stack(num_disks, from_rod, to_rod)


def find_spare_rod(from_rod, to_rod):
    '''
    function: find_spare_rod
    params:   from_rod & to_rod, the rods that are already in use
    return:   the spare rod
    '''
    return 6 - (from_rod + to_rod)


def move_stack(num_disks, from_rod, to_rod):
    '''
    function: move_stack, recursive function
    params:   num_disks to be moved
              from_rod, the starting rod for the disks
              to_rod, the target to move the disks to
    '''
    if num_disks == 1:
        move_one_disk(1, from_rod, to_rod)
    else:
        spare_rod = find_spare_rod(from_rod, to_rod)
        move_stack(num_disks - 1, from_rod, spare_rod)
        move_one_disk(num_disks, from_rod, to_rod)
        move_stack(num_disks - 1, spare_rod, to_rod)


def move_one_disk(disk, from_rod, to_rod):
    '''
    function: move_one_disk
    params:   disk to be moved
              from_rod, the starting rod for the disks
              to_rod, the target to move the disks to
    '''
    if from_rod == 1:
        if num_disks == 1:
            led_A1.value(1)
            sleep(1)
            led_A1.value(0)
            sleep(1)
        elif num_disks == 2:
            led_A1.value(1)
            led_A2.value(1)
            sleep(1)
            led_A1.value(0)
            led_A2.value(0)
            sleep(1)
        else :
            led_A1.value(1)
            led_A2.value(1)
            led_A3.value(1)
            sleep(1)
            led_A1.value(0)
            led_A2.value(0)
            led_A3.value(0)
            sleep(1)
    
    if to_rod == 1:
        if num_disks == 1:
            led_A1.value(1)
            sleep(1)
            led_A1.value(0)
            sleep(1)
        elif num_disks == 2:
            led_A1.value(1)
            led_A2.value(1)
            sleep(1)
            led_A1.value(0)
            led_A2.value(0)
            sleep(1)
        else :
            led_A1.value(1)
            led_A2.value(1)
            led_A3.value(1)
            sleep(1)
            led_A1.value(0)
            led_A2.value(0)
            led_A3.value(0)
            sleep(1)
            
    if to_rod == 3:
        if num_disks == 1:
            led_C1.value(1)
            sleep(1)
            led_C1.value(0)
            sleep(1)
        elif num_disks == 2:
            led_C1.value(1)
            led_C2.value(1)
            sleep(1)
            led_C1.value(0)
            led_C2.value(0)
            sleep(1)
        else :
            led_C1.value(1)
            led_C2.value(1)
            led_C3.value(1)
            sleep(1)
            led_C1.value(0)
            led_C2.value(0)
            led_C3.value(0)
            sleep(1)
    
    if from_rod == 3:
        if num_disks == 1:
            led_C1.value(1)
            sleep(1)
            led_C1.value(0)
            sleep(1)
        elif num_disks == 2:
            led_C1.value(1)
            led_C2.value(1)
            sleep(1)
            led_C1.value(0)
            led_C2.value(0)
            sleep(1)
        else :
            led_C1.value(1)
            led_C2.value(1)
            led_C3.value(1)
            sleep(1)
            led_C1.value(0)
            led_C2.value(0)
            led_C3.value(0)
            sleep(1)
            
    if to_rod == 2:
        if num_disks == 1:
            led_B1.value(1)
            sleep(1)
            led_B1.value(0)
            sleep(1)
        elif num_disks == 2:
            led_B1.value(1)
            led_B2.value(1)
            sleep(1)
            led_B1.value(0)
            led_B2.value(0)
            sleep(1)
        else :
            led_B1.value(1)
            led_B2.value(1)
            led_B3.value(1)
            sleep(1)
            led_B1.value(0)
            led_B2.value(0)
            led_B3.value(0)
            sleep(1)
    
    if from_rod == 2:
        if num_disks == 1:
            led_B1.value(1)
            sleep(1)
            led_B1.value(0)
            sleep(1)
        elif num_disks == 2:
            led_B1.value(1)
            led_B2.value(1)
            sleep(1)
            led_B1.value(0)
            led_B2.value(0)
            sleep(1)
        else :
            led_B1.value(1)
            led_B2.value(1)
            led_B3.value(1)
            sleep(1)
            led_B1.value(0)
            led_B2.value(0)
            led_B3.value(0)
            sleep(1)
    print("Moving disk#", disk, "from rod", from_rod, "to", to_rod)



tower_of_hanoi(3, 1, 3)
    


def allon():
    #this function set all the led light on
    led_A1.value(1)
    led_A2.value(1)
    led_A3.value(1)
    led_B1.value(1)
    led_B2.value(1)
    led_B3.value(1)
    led_C1.value(1)
    led_C2.value(1)
    led_C3.value(1)

    
def alloff():
    #this function set all the led light off
    led_A1.value(0)
    led_A2.value(0)
    led_A3.value(0)
    led_B1.value(0)
    led_B2.value(0)
    led_B3.value(0)
    led_C1.value(0)
    led_C2.value(0)
    led_C3.value(0)