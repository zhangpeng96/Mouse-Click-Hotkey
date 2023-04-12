import time
from pynput import keyboard

def on_release(key):
    try:
        keycode = key.vk
    except AttributeError:
        keycode = key.value.vk
    print('Release\t', key)

def on_press(key):
    try:
        keycode = key.vk
    except AttributeError:
        keycode = key.value.vk
    print('Press\t', key)

with keyboard.Listener(
        on_release = on_release,
        on_press = on_press) as listener:
    listener.join()
