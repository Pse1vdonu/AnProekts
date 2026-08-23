import msvcrt

def yprav_res():
    pos=0
    if msvcrt.kbhit():
        key = msvcrt.getch().decode('utf-8').lower()

        if key=='a' or key=='ф':
            pos=-1

        elif key=='d' or key=='в':
            pos=1

        else:
            pass

    return pos                    