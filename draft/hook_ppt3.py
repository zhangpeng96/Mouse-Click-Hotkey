from pynput.keyboard import HotKey, Key, KeyCode, Listener
from pynput.mouse import Button, Controller
import time


mouse = Controller()

def ppt_erase():
    initial_pos = mouse.position
    for pos in [ (241, 22), (374, 76) ]:
        mouse.position = pos
        time.sleep(0.25)
        mouse.click(Button.left, 1)
    mouse.position = initial_pos
    mouse.click(Button.right, 1)
    print('erase')

def ppt_select():
    initial_pos = mouse.position
    for pos in [ (241, 22), (313, 76) ]:
        mouse.position = pos
        time.sleep(0.2)
        mouse.click(Button.left, 1)
    mouse.position = initial_pos
    mouse.click(Button.right, 1)
    print('select')

def ppt_pen1():
    initial_pos = mouse.position
    mouse.position = (241, 22)
    time.sleep(0.2)
    mouse.click(Button.left, 1)
    time.sleep(0.2)
    mouse.position = (434, 76)
    time.sleep(0.2)
    mouse.click(Button.left, 1)
    time.sleep(0.2)
    mouse.position = initial_pos
    mouse.click(Button.right, 1)
    print('pen1')

def ppt_pen2():
    initial_pos = mouse.position
    mouse.position = (241, 22)
    time.sleep(0.25)
    mouse.click(Button.left, 1)
    mouse.position = (495, 76)
    time.sleep(0.25)
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

def function_1():
    print('Function 1 activated')

def function_2():
    print('Function 2 activated')

def function_3():
    print('Function 3 activated')
    exit()

hotkey1 = HotKey(
    [Key.alt, Key.ctrl, KeyCode(char='1')],
    ppt_erase
)

hotkey2 = HotKey(
    [Key.alt, Key.ctrl, KeyCode(char='2')],
    ppt_select
)

hotkey3 = HotKey(
    [Key.alt, Key.ctrl, KeyCode(char='3')],
    ppt_pen1
)

hotkey4 = HotKey(
    [Key.alt, Key.ctrl, KeyCode(char='4')],
    ppt_pen2
)

hotkey5 = HotKey(
    [Key.alt, Key.ctrl, KeyCode(char='5')],
    ppt_pen3
)

hotkey6 = HotKey(
    [Key.alt, Key.ctrl, KeyCode(char='0')],
    esc
)

hotkeys = [hotkey1, hotkey2, hotkey3, hotkey4, hotkey5, hotkey6]


def signal_press_to_hotkeys(key):
    for hotkey in hotkeys:
        hotkey.press(l.canonical(key))

def signal_release_to_hotkeys(key):
    for hotkey in hotkeys:
        hotkey.release(l.canonical(key))

with Listener(on_press=signal_press_to_hotkeys, on_release=signal_release_to_hotkeys) as l:
    l.join()