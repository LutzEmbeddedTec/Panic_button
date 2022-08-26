import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode

import board
import digitalio
import time

kbd = Keyboard(usb_hid.devices)

button = digitalio.DigitalInOut(board.GP13)
button.switch_to_input(pull=digitalio.Pull.DOWN)

while True:
    if button.value:
        kbd.send(Keycode.ALT,Keycode.F4)
        time.sleep(0.5)
        kbd.send(Keycode.ALT, Keycode.CONTROL,Keycode.H)
    time.sleep(0.2)
