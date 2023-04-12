from pynput import keyboard
from pynput.mouse import Button, Controller
import time

mouse = Controller()

def ppt_mark():
    initial_pos = mouse.position
    for pos in [ (241, 22), (374, 76) ]:
        mouse.position = pos
        time.sleep(0.1)
        mouse.click(Button.left, 1)
    mouse.position = initial_pos
    mouse.click(Button.right, 1)
    print('mark')

def ppt_erase():
    initial_pos = mouse.position
    for pos in [ (241, 22), (374, 76) ]:
        mouse.position = pos
        time.sleep(0.1)
        mouse.click(Button.left, 1)
    mouse.position = initial_pos
    mouse.click(Button.right, 1)
    print('erase')

def ppt_select():
    initial_pos = mouse.position
    for pos in [ (241, 22), (313, 76) ]:
        mouse.position = pos
        time.sleep(0.1)
        mouse.click(Button.left, 1)
    mouse.position = initial_pos
    mouse.click(Button.right, 1)
    print('select')

def ppt_pen1():
    initial_pos = mouse.position
    mouse.position = (241, 22)
    time.sleep(0.2)
    mouse.click(Button.left, 1)
    mouse.position = (434, 76)
    time.sleep(0.2)
    mouse.click(Button.left, 1)
    mouse.position = initial_pos
    mouse.click(Button.right, 1)
    print('pen1')

def ppt_pen2():
    initial_pos = mouse.position
    mouse.position = (241, 22)
    time.sleep(0.2)
    mouse.click(Button.left, 1)
    mouse.position = (495, 76)
    time.sleep(0.2)
    mouse.click(Button.left, 1)
    mouse.position = initial_pos
    mouse.click(Button.right, 1)
    print('pen2')

def ppt_pen3():
    initial_pos = mouse.position
    mouse.position = (241, 22)
    time.sleep(0.2)
    mouse.click(Button.left, 1)
    mouse.position = (555, 76)
    time.sleep(0.2)
    mouse.click(Button.left, 1)
    mouse.position = initial_pos
    mouse.click(Button.right, 1)
    print('pen3')

def esc():
    print('<esc> pressed')
    exit()
    return False

with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+1': ppt_erase,
        '<ctrl>+<alt>+2': ppt_select,
        '<ctrl>+<alt>+3': ppt_pen1,
        '<ctrl>+<alt>+4': ppt_pen2,
        '<ctrl>+<alt>+5': ppt_pen3,
        '<ctrl>+<alt>+0': esc }) as h:
    h.join()
