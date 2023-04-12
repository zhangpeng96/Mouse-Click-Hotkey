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
ppt_select = Action( [ (220, 24), (314, 75) ] )
ppt_erase = Action( [ (220, 24), (375, 75) ] )
ppt_pen1 = Action( [ (220, 24), (435, 75) ] )
ppt_pen2 = Action( [ (220, 24), (495, 75) ] )
ppt_pen3 = Action( [ (220, 24), (555, 75) ] )
# for action in actions:
#     action()
action_map = {
    '<cmd>+1': ppt_select,
    '<cmd>+2': ppt_erase,
    '<cmd>+3': ppt_pen1,
    # '<shift>+<alt>+4': ppt_pen2,
    # '<shift>+<alt>+5': ppt_pen3,
    '<cmd>+0': exit,
}


def __win32_event_filter__(msg, data):
    print(data, data.vkCode)
    if data.vkCode == 91:
        h.suppress_event()

with keyboard.GlobalHotKeys(action_map, win32_event_filter = __win32_event_filter__) as h:
    h.join()

# with keyboard.GlobalHotKeys(action_map) as h:
#     h.join()







# def __win32_event_filter__(msg, data):
#     global listener
#     suppress_map = { 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 107, 110 }
#     if data.vkCode in suppress_map and msg == 256:
#         h.suppress_event()

# with keyboard.GlobalHotKeys(action_map, win32_event_filter = __win32_event_filter__) as h:
#     h.join()
