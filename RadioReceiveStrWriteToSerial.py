from microbit import *
from microbit import uart
import radio

radio.on()
radio.config(channel=5)

uart.init(115200, bits=8, parity=None, stop=1, tx=None, rx=None)

while True:
    msg = radio.receive()
    
    if msg:
        uart.write(msg)
        display.scroll(msg)