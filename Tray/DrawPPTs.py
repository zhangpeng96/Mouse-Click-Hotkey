import time
from pynput.mouse import Button, Controller, Listener
from pynput.mouse import Listener as MouseListener

mouse = Controller()
hanging = MouseListener()

# 禁用鼠标移动，防止切换工具时鼠标随意移动
def suppress_mouse(msg, data):
    if msg <= 512:
        hanging.suppress_event()

def actions(action=[], leap=0.2):
    initial_pos = mouse.position
    hanging = MouseListener(win32_event_filter=suppress_mouse)
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

def erase():
    actions( [ (241, 22), (374, 76) ] )
    print('Eraser')

def select():
    actions( [ (241, 22), (313, 76) ] )
    print('Selector')

def pen1():
    actions( [ (241, 22), (434, 76) ] )
    print('Pen1')

def pen2():
    actions( [ (241, 22), (495, 76) ] )
    print('Pen2')

def pen3():
    actions( [ (241, 22), (555, 76) ] )
    print('Pen3')
