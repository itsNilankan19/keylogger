# After installing pynput you will be able to-
# i. control your mouse
# ii. listen to your mouse
# iii. control your keyboard
# iv. listen to keyboard

from pynput.mouse import Controller
from pynput.keyboard import Controller

def controlMouse():
    mouse = Controller()
    mouse.position = (1600,500)

def controlKeyboard():
    keyboard = Controller()
    keyboard.type("This is my security program..")
    
controlKeyboard()















