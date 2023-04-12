# from pynput.keyboard import HotKey, Key, KeyCode, Listener
import time
# import keyboard
from pynput import keyboard
from pynput.mouse import Button, Controller, Listener


def fts(msg, data):
    if msg <= 512:        
        hanging.suppress_event()
    print(msg, data)

mouse = Controller()
hanging = Listener()

def common_action(action=[], leap=0.2):
    initial_pos = mouse.position
    # global hanging
    hanging = Listener(win32_event_filter=fts)
    hanging.start()
    for pos in action:
        mouse.position = pos
        time.sleep(leap)
        mouse.click(Button.left, 1)
        time.sleep(leap)
    mouse.position = (520, 20)
    mouse.click(Button.left, 1)
    mouse.position = initial_pos
    hanging.stop()

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


def on_press(key):
    try:
        # print('alphanumeric key {0} pressed'.format(key.char))
        pass
    except AttributeError:
        pass
        # print('special key {0} pressed'.format(key))

def on_release(key):
    try:
        keycode = key.vk
    except AttributeError:
        keycode = key.value.vk

    if key == keyboard.Key.esc:
        exit()
        return False
    elif key == keyboard.KeyCode.from_char('1'):
        ppt_erase()
        print('1')
    elif key == keyboard.KeyCode.from_char('2'):
        ppt_select()
        print('2')
    elif key == keyboard.KeyCode.from_char('3'):
        ppt_pen1()
        print('3')
    elif key == keyboard.KeyCode.from_char('4'):
        ppt_pen2()
        print('4')
    elif key == keyboard.KeyCode.from_char('5'):
        ppt_pen3()
        print('5')


with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
