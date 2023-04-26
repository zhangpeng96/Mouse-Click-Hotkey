import pystray
import threading
from PIL import Image
from pystray import MenuItem, Menu
from pynput.keyboard import Key, KeyCode, Listener

import DrawEdge
import DrawPPTs


state = 0

def on_exit(icon):
    icon.stop()
    listener.stop()

def set_state(v):
    def inner(icon, item):
        global state
        state = v
        if state == 1:
            print('----------------\nSwitch to Edge Mode\n')
        elif state == 2:
            print('----------------\nSwitch to PowerPoint Mode\n')
        elif state == 0:
            print('----------------\nSwitch to Silent Mode\n')
    return inner

def get_state(v):
    def inner(item):
        return state == v
    return inner


menu = (
    MenuItem('Edge', set_state(1), checked=get_state(1), radio=True),
    MenuItem('PowerPoint', set_state(2), checked=get_state(2), radio=True),
    Menu.SEPARATOR,
    MenuItem('静默', set_state(0), checked=get_state(0), radio=True),
    Menu.SEPARATOR,
    MenuItem('退出', on_exit)
)
image = Image.open("icon.png")
icon = pystray.Icon("icon", image, "Mouse Click Hotkey Tray", menu)


threading.Thread(target=icon.run, daemon=True).start()


def on_release(key):
    if key == Key.esc:
        pass
    elif key == KeyCode.from_char('1'):
        if state == 1:
            DrawEdge.erase()
        elif state == 2:
            DrawPPTs.erase()
    elif key == KeyCode.from_char('2'):
        if state == 1:
            DrawEdge.mark()
        elif state == 2:
            DrawPPTs.select()
    elif key == KeyCode.from_char('3'):
        if state == 1:
            DrawEdge.pen1()
        elif state == 2:
            DrawPPTs.pen1()
    elif key == KeyCode.from_char('4'):
        if state == 1:
            DrawEdge.pen2()
        elif state == 2:
            DrawPPTs.pen2()
    elif key == KeyCode.from_char('5'):
        if state == 1:
            DrawEdge.pen3()
        elif state == 2:
            DrawPPTs.pen3()
    elif key == KeyCode.from_char('6'):
        if state == 1:
            DrawEdge.pen4()
    elif key == KeyCode.from_char('7'):
        if state == 1:
            DrawEdge.pen5()
    elif key == KeyCode.from_char('8'):
        if state == 1:
            DrawEdge.pen()


print('Mouse Click Hotkey Tray')
with Listener(on_release=on_release) as listener:
    listener.join()
