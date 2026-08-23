from random import randint
from .color import q, w, e
from .yprav import yprav_res
from . import statys as st
from . import strok as s

def move_up():

    kol=randint(1, 2)
    i_kol=[randint(0, 5), randint(0, 5)]

    pos=yprav_res()
    i_player=s.strok6.index(e)
    new_i_player=i_player+pos

    if w in s.strok6:
        blocks=[i for i in range(len(s.strok6)) if s.strok6[i]==w]
    else:
        blocks=[]
    
    if new_i_player in blocks:
        st.live=False

    if new_i_player!=i_player:
        s.strok6[i_player]=q
        s.strok6[new_i_player]=e

    if w in s.strok5:
        blocks=[i for i in range(len(s.strok5)) if s.strok5[i]==w]
    else:
        blocks=[]

    s.strok7, s.strok6, s.strok5, s.strok4, s.strok3, s.strok2 = s.strok6.copy(), s.strok5.copy(), s.strok4.copy(), s.strok3.copy(), s.strok2.copy(), s.strok1.copy()
    
    if new_i_player in blocks:
        st.live=False
    
    s.strok1=[q, q, q, q, q, q]
    for i in range (kol):
        s.strok1[i_kol[i]]=w

    s.strok6[new_i_player]=e

    s.strok7[new_i_player]=q

    map=[s.strok1, s.strok2, s.strok3, s.strok4, s.strok5, s.strok6, s.strok7]

    return map