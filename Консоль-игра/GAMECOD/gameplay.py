from .map_go import go
import time as t
import subprocess
from . import statys as st
from .final import final_menu
import sys
import os


def start():
    while st.live:
        print(st.points)
        go()
        t.sleep(1)
        subprocess.run("cls", shell=True)
        st.points+=1

    print(f'You lose! ({st.points})')

    fin=final_menu()
    if fin:
        os.execv(sys.executable, [sys.executable, *sys.argv])