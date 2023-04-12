import time
from ctypes import *

windll.user32.BlockInput(True)
time.sleep(10)
windll.user32.BlockInput(False)
time.sleep(5)