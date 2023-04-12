# from pynput.keyboard import HotKey, Key, KeyCode, Listener
import time
import keyboard
from pynput.mouse import Button, Controller


mouse = Controller()

def common_action(action=[], leap=0.2):
    initial_pos = mouse.position
    for pos in action:
        mouse.position = pos
        time.sleep(leap)
        mouse.click(Button.left, 1)
        time.sleep(leap)
    mouse.position = (520, 20)
    mouse.click(Button.left, 1)
    mouse.position = initial_pos

def ppt_erase():
    common_action( [ (241, 22), (374, 76) ] )
    print('erase')

def ppt_select():
    common_action( [ (241, 22), (313, 76) ] )
    print('select')

def ppt_pen1():
    common_action( [ (241, 22), (434, 76) ] )
    print('pen1')

def ppt_pen2():
    common_action( [ (241, 22), (495, 76) ] )
    print('pen2')

def ppt_pen3():
    common_action( [ (241, 22), (555, 76) ] )
    print('pen3')

def esc():
    print('<esc> pressed')
    exit()
    return False


keyboard.add_hotkey('shift+1', ppt_erase)
keyboard.add_hotkey('shift+2', ppt_select)
keyboard.add_hotkey('shift+3', ppt_pen1)
keyboard.add_hotkey('shift+4', ppt_pen2)
keyboard.add_hotkey('shift+5', ppt_pen3)
keyboard.add_hotkey('shift+0', esc)
keyboard.wait('esc')
