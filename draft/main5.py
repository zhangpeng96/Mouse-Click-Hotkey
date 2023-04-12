from pynput import keyboard
from pynput.mouse import Button, Controller
import time

click_position = (0, 0)

class Pos():
    def __init__(self, x, y, click=1):
        self.position = (x, y)
        self.click = click
    def __call__(self):
        time.sleep(0.2)
        mouse.position = self.position
        if self.click:
            mouse.click(Button.left, 1)
        else:
            pass


class Action():
    def __init__(self, actions=[]):
        self.initial_pos = (0, 0)
        self.actions = actions
    def __call__(self):
        self.initial_pos = mouse.position
        print(self.actions)
        for action in self.actions:
            Pos(*action)()
        time.sleep(0.21)
        mouse.position = self.initial_pos



mouse = Controller()
print(mouse.position)
# mouse.position = click_position


# actions = [ Pos(1917, 1054) ]
time.sleep(3)

# actions = [ Pos(220, 24), Pos(375, 75) ]
# edge_erase = Action( [ (308, 115) ] )
# edge_mark = Action( [ (82, 115) ] )
# edge_pen1 = Action( [ (226, 115), (285, 210) ] )
# edge_pen2 = Action( [ (226, 115), (285, 260) ] )
# edge_pen3 = Action( [ (226, 115), (285, 360) ] )


def edge_erase():
    initial_pos = mouse.position
    for pos in [ (308, 115) ]:
        mouse.position = pos
        time.sleep(0.05)
        mouse.click(Button.left, 1)
    # time.sleep(0.1)
    mouse.position = initial_pos
    print('erase')

def edge_mark():
    initial_pos = mouse.position
    for pos in [ (83, 115) ]:
        mouse.position = pos
        time.sleep(0.05)
        mouse.click(Button.left, 1)
    # time.sleep(0.1)
    mouse.position = initial_pos
    print('mark')

def edge_pen1():
    initial_pos = mouse.position
    for pos in [ (268, 115), (285, 210) ]:
        mouse.position = pos
        time.sleep(0.05)
        mouse.click(Button.left, 1)
    time.sleep(0.05)
    mouse.position = initial_pos
    mouse.click(Button.right, 1)
    print('pen1')

def edge_pen2():
    initial_pos = mouse.position
    for pos in [ (268, 115), (285, 260) ]:
        mouse.position = pos
        time.sleep(0.05)
        mouse.click(Button.left, 1)
    time.sleep(0.05)
    mouse.position = initial_pos
    mouse.click(Button.right, 1)
    print('pen2')

def edge_pen3():
    initial_pos = mouse.position
    for pos in [ (268, 115), (285, 360) ]:
        mouse.position = pos
        time.sleep(0.05)
        mouse.click(Button.left, 1)
    time.sleep(0.05)
    mouse.position = initial_pos
    mouse.click(Button.right, 1)
    print('pen3')

def edge_pen4():
    initial_pos = mouse.position
    for pos in [ (268, 115), (385, 312) ]:
        mouse.position = pos
        time.sleep(0.05)
        mouse.click(Button.left, 1)
    time.sleep(0.05)
    mouse.position = initial_pos
    mouse.click(Button.right, 1)
    print('pen4')

def edge_pen5():
    initial_pos = mouse.position
    for pos in [ (268, 115), (485, 312) ]:
        mouse.position = pos
        time.sleep(0.05)
        mouse.click(Button.left, 1)
    time.sleep(0.05)
    mouse.position = initial_pos
    mouse.click(Button.right, 1)
    print('pen5')

# def edge_mark():
#     Action( [ (82, 115) ] )()
#     print('edge_mark')
# def edge_pen1():
#     Action( [ (82, 215) ] )()
#     print('edge_pen1')
# def edge_pen2():
#     print('edge_pen2')
# def edge_pen3():
#     print('edge_pen3')



def esc():
    print('<esc> pressed')
    exit()
    return False

with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+1': edge_erase,
        '<ctrl>+<alt>+2': edge_mark,
        '<ctrl>+<alt>+3': edge_pen1,
        '<ctrl>+<alt>+4': edge_pen2,
        '<ctrl>+<alt>+5': edge_pen3,
        '<ctrl>+<alt>+6': edge_pen4,
        '<ctrl>+<alt>+7': edge_pen5,
        '<ctrl>+<alt>+0': esc }) as h:
    h.join()
