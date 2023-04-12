import time
from pynput import keyboard

controller = keyboard.Controller()

def on_release(key):
    print(controller.ctrl_pressed)
    # print(key)

def on_press(key):
    print(controller.ctrl_pressed)
    # print(key)

with keyboard.Listener(
        on_release = on_release,
        on_press = on_press) as listener:
    listener.join()
