from random import randint as r
from copy import copy as c

class Cell:

    Max_Name=0

    def __init__(self):        
        self.Name=0
        self.color={'r': 255, 'g': 255, 'b': 255, 'p': '\033[0m'}

    def Neighbours(self, cells, y, x):
        y_max, x_max = cells.shape
        
        y1=max(0, y - 1)
        y2=min(y_max, y + 2)
        
        x1=max(0, x - 1)
        x2=min(x_max, x + 2)

        matrix=[]

        for y_ob in range(y1, y2):
            for x_ob in range(x1, x2):
                if y_ob == y and x_ob == x:
                    continue              
                matrix.append((cells[y_ob, x_ob], y_ob, x_ob)) 

        return matrix

    def Luck(self):
        self.Luck_move=r(0, 20) #<--Значениe можно поменять (30)
        self.Luck_death=r(0, 30) #<--Значениe можно поменять (20)
        self.Power=r(10, 30) #<--Значениe можно поменять ()
    
    def Try_live(self):
        if r(0, 10000)<25 and Cell.Max_Name<9: #<--Значения можно поменять ((0, 10000)<25), (9)
            Cell.Max_Name+=1
            self.Name=Cell.Max_Name 
            self.color={'r': r(50, 255), 'g': r(50, 255), 'b': r(50, 255), 'p': '\033[0m'}
            return True

    def Try_death(self, cells, y, x):
        if r(0, 100)<self.Luck_death:
             
            cells[y, x]=Cell()

    def Try_Move(self, cells, y, x):
        for ob, y_ob, x_ob in self.Neighbours(cells, y, x):
            if ob.Name==0 and r(0, 100)<self.Luck_move:
                cells[y_ob, x_ob]=c(self)
            elif ob.Name!=self.Name and ob.Name!=0 and r(0, 100)<50+(self.Power-ob.Power):
                cells[y_ob, x_ob]=c(self)
            else:
                continue