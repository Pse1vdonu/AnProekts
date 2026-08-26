from .move import move_up

def go():
    for i in move_up():
        print(''.join(i))