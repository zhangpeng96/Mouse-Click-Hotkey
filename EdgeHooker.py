import time
from pynput.mouse import Button, Controller, Listener
from pynput.mouse import Listener as MouseListener
from pynput.keyboard import Key, KeyCode, Listener


# 禁用鼠标移动，防止切换工具时鼠标随意移动
def suppress_mouse(msg, data):
    if msg <= 512:
        hanging.suppress_event()

def common_action(action=[], leap=0.05):
    initial_pos = mouse.position
    hanging = MouseListener(win32_event_filter=suppress_mouse)
    hanging.start()
    for pos in action:
        mouse.position = pos
        time.sleep(leap)
        mouse.click(Button.left, 1)
        time.sleep(leap)
    mouse.position = (580, 111)
    mouse.click(Button.left, 1)
    mouse.position = initial_pos
    hanging.stop()

def ppt_erase():
    common_action( [ (308, 115) ] )
    print('Eraser')

def ppt_mark():
    common_action( [ (83, 115) ] )
    print('Marker')

def ppt_pen():
    common_action( [ (200, 115) ] )
    print('Pen')

def ppt_pen1():
    common_action( [ (268, 115), (285, 210) ] )
    print('Pen1')

def ppt_pen2():
    common_action( [ (268, 115), (285, 260) ] )
    print('Pen2')

def ppt_pen3():
    common_action( [ (268, 115), (285, 360) ] )
    print('Pen2')

def ppt_pen4():
    common_action( [ (268, 115), (385, 312) ] )
    print('Pen4')

def ppt_pen5():
    common_action( [ (268, 115), (485, 312) ] )
    print('Pen5')

def esc():
    print('Quit')
    exit()


def on_release(key):
    if key == Key.esc:
        exit()
    elif key == KeyCode.from_char('1'):
        ppt_erase()
    elif key == KeyCode.from_char('2'):
        ppt_mark()
    elif key == KeyCode.from_char('3'):
        ppt_pen1()
    elif key == KeyCode.from_char('4'):
        ppt_pen2()
    elif key == KeyCode.from_char('5'):
        ppt_pen3()
    elif key == KeyCode.from_char('6'):
        ppt_pen4()
    elif key == KeyCode.from_char('7'):
        ppt_pen5()
    elif key == KeyCode.from_char('8'):
        ppt_pen()


mouse = Controller()
hanging = MouseListener()

with Listener(on_release=on_release) as listener:
    listener.join()
