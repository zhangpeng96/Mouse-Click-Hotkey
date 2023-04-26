import time
from pynput.mouse import Button, Controller, Listener
from pynput.mouse import Listener as MouseListener

mouse = Controller()
hanging = MouseListener()

# 禁用鼠标移动，防止切换工具时鼠标随意移动
def suppress_mouse(msg, data):
    if msg <= 512:
        hanging.suppress_event()

def actions(action=[], leap=0.05):
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

def erase():
    actions( [ (308, 115) ] )
    print('Eraser')

def mark():
    actions( [ (83, 115) ] )
    print('Marker')

def pen():
    actions( [ (200, 115) ] )
    print('Pen')

def pen1():
    actions( [ (268, 115), (285, 210) ] )
    print('Pen1')

def pen2():
    actions( [ (268, 115), (285, 260) ] )
    print('Pen2')

def pen3():
    actions( [ (268, 115), (285, 360) ] )
    print('Pen2')

def pen4():
    actions( [ (268, 115), (385, 312) ] )
    print('Pen4')

def pen5():
    actions( [ (268, 115), (485, 312) ] )
    print('Pen5')
