import sys
import time
from pynput.mouse import Button, Controller

mouse = Controller()

def ppt_erase():
    initial_pos = mouse.position
    for pos in [ (241, 22), (374, 76) ]:
        mouse.position = pos
        time.sleep(0.2)
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
    mouse.click(Button.left, 1)
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


# ppt_pen3()
# arg = sys.argv[1]

if len(sys.argv) > 1:
	arg = sys.argv[1]
	if arg == 'erase':
		ppt_erase()
	elif arg == 'select':
		ppt_select()
	elif arg == 'pen1':
		ppt_pen1()
	elif arg == 'pen2':
		ppt_pen2()
	elif arg == 'pen3':
		ppt_pen3()
	else:
		pass
