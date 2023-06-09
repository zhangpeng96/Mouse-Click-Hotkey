from pynput import keyboard

# The key combination to check
COMBINATIONS = [
    # {keyboard.Key.shift, keyboard.KeyCode(char='a')}, # Shift + a
    # {keyboard.Key.shift, keyboard.KeyCode(char='A')}, # Shift + A
    # {keyboard.Key.scroll_lock}, # Scroll lock
    # {keyboard.KeyCode(char='q')}, # q
    # {keyboard.KeyCode(char='Q')}, # Q
    # {keyboard.Key.shift, keyboard.Key.insert, keyboard.Key.ctrl} # Shift + Insert + Ctrl    
    {keyboard.Key.ctrl, keyboard.Key.alt}
]

# The currently active modifiers
current = set()

def execute():
    print ("Do Something")

def on_press(key):
    # print(current)
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.add(key)
        if any(all(k in current for k in COMBO) for COMBO in COMBINATIONS):
            execute()

def on_release(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        current.remove(key)

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
