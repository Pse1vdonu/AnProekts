from .Class import Cell
import numpy as np
import subprocess
from time import sleep as sl
from .Status import Stop_menu
from .Text import set_small_font
import ctypes

set_small_font()
ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11), 7)

cells=np.array([[Cell() for i in range(100)] for i in range(50)], dtype=object) #<--Значения можно поменять (100), (50)

while True:
    Stop_menu()
    for  y, strok in enumerate(cells):
        for x, el in enumerate(strok):
            if el.Name!=0:
                el.Try_Move(cells, y, x)
                el.Try_death(cells, y, x)
            else:
                if el.Try_live():
                    el.Luck()
            pict=f"\033[38;2;{el.color['r']};{el.color['g']};{el.color['b']}m{el.Name}{el.color['p']}"
            print(pict, end=' ')
        print()
    sl(0.25) #<--Значение можно поменять (0.25)
    subprocess.run("cls", shell=True)