from microbit import *
import radio

radio.on()
radio.config(channel=5)

read = False

while True:
    if read == True:
        temp = temperature()
        print(str(temp))
        radio.send(str(temp))
        sleep(5000)
        
    if button_a.was_pressed():
        read = True
        display.scroll("BEGIN")
        
    elif button_b.was_pressed():
        read = False
        display.scroll("END")

    