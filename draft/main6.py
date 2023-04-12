from pynput.keyboard import HotKey, Key, KeyCode, Listener


def function_1():
    print('Function 1 activated')

def function_2():
    print('Function 2 activated')

def function_3():
    print('Function 3 activated')
    exit()

hotkey1 = HotKey(
    [Key.alt, Key.ctrl, KeyCode(char='1')],
    function_1
)

hotkey2 = HotKey(
    [Key.alt, Key.ctrl, KeyCode(char='2')],
    function_2
)

hotkey3 = HotKey(
    [Key.alt, Key.ctrl, KeyCode(char='3')],
    function_3
)

hotkeys = [hotkey1, hotkey2, hotkey3]


def signal_press_to_hotkeys(key):
    for hotkey in hotkeys:
        hotkey.press(l.canonical(key))

def signal_release_to_hotkeys(key):
    for hotkey in hotkeys:
        hotkey.release(l.canonical(key))

with Listener(on_press=signal_press_to_hotkeys, on_release=signal_release_to_hotkeys) as l:
    l.join()