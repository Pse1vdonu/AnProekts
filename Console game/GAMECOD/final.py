import subprocess
import msvcrt
import sys

def final_menu():
    print('Нажмите Q, чтобы выйти, или W, чтобы продолжить.')

    while True:
        if msvcrt.kbhit():
            keyf = msvcrt.getch().decode('utf-8').lower()

            if keyf=='q' or keyf=='й':
                sys.exit()

            elif keyf=='w' or keyf=='ц':
                subprocess.run("cls", shell=True)
                break

            else:
                continue

    return True