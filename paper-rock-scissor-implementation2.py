from microbit import *
from radio import *
import random

on()
config(group=1, length=251)
result = {
        'papir': {
                'papir': 'DRAW',
                'saks': 'LOSE',
                'stein': 'WIN'
        },
        'saks': {
                'papir': 'WIN',
                'saks': 'DRAW',
                'stein': 'LOSE'
        },
        'stein': {
                'papir': 'LOSE',
                'saks': 'WIN',
                'stein': 'DRAW'
        }
}

convert_to_string = ['papir', 'saks', 'stein']

display.scroll('shake')

while True:
    shake = ''
    if accelerometer.was_gesture("shake"):
        shake = random.choice(convert_to_string)
        display.scroll(shake)
    
        sleep(5000)
    
        # wait for result
        data = None
        send(shake)
        while data is None:
            data = receive()
            sleep(500)
    
        if data not in convert_to_string:
            display.scroll("FAIL")
            sleep(10000)
            continue
        
        display.scroll(result[shake][data])
        sleep(5000)
        display.clear()
