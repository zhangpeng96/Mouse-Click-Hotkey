from pynput import keyboard

def on_activate_a():
    print('<ctrl>+<alt>+a pressed')

def on_activate_s():
    print('<ctrl>+<alt>+s pressed')

def on_activate_d():
    print('<ctrl>+<alt>+d pressed')

def esc():
    print('<esc> pressed')
    exit()
    return False

def esc_shift():
    print('<esc>+<shift> pressed')
    raise Exception

with keyboard.GlobalHotKeys({
        '<ctrl>+<alt>+a': on_activate_a,
        '<ctrl>+<alt>+s': on_activate_s,
        '<ctrl>+<alt>+d': on_activate_d,
        '<ctrl>+<alt>+x': esc }) as h:
    h.join()
