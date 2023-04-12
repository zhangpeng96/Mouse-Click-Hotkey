import time
from pynput import keyboard

# keyboard = Controller()
cache = set()

def on_release(key):
    try:
        keycode = key.vk
    except AttributeError:
        keycode = key.value.vk
    print('Release\t', key)    
    if keycode == keyboard.KeyCode.from_char('1'):
        if keyboard.Key.ctrl_l in cache:
            print('1')

def on_press(key):
    try:
        keycode = key.vk
    except AttributeError:
        keycode = key.value.vk
    print(listener.alt_pressed)
    print('Press\t', key)
    if key == keyboard.Key.ctrl_l:
        cache.add(key)
        print(cache)
    elif key == keyboard.Key.alt_l:
        if keyboard.Key.ctrl_l in cache:
            cache.add(key)
            print(cache)
    elif key == keyboard.KeyCode.from_char('1'):
        if keyboard.Key.alt_l in cache:
            cache.add(key)
            print(cache)

with keyboard.Listener(
        on_release = on_release,
        on_press = on_press) as listener:
    listener.join()
