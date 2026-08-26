import subprocess
import msvcrt
import sys

def Stop_menu():

    if msvcrt.kbhit():
        key = msvcrt.getch().decode('cp866', errors='ignore').lower()

        if key=='s' or key=='ы':
            print('Пауза! Нажмите Enter, чтобы продолжить, или Q, чтобы выйти.')
            input()
            subprocess.run("cls", shell=True)

        elif key=='q' or key=='й':
            sys.exit()