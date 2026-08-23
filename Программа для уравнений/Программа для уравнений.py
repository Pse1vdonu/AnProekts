import math
print ("Программа для решения уравнений")
def l():
    print ("∙∙∙∙∙∙∙∙∙∙∙")
    print ("ax²+bx+c=0")
    a=float(input("a = "))
    def al():
        nonlocal a
        if (a==0):
            print ("a - не может принимать значение 0")
            a=int(input("a = "))
            al()
    al()
    b=float(input("b = "))
    c=float(input("c = "))
    d=b**2-4*a*c
    try:
        dr=math.sqrt(d)
    except ValueError:
        print ("D = ", d)
        print ("x = нет корней")
        print ("∙∙∙∙∙∙∙∙∙∙∙")
        ot()
    answer1=(-b+dr)/(2*a)
    answer2=(-b-dr)/(2*a)
    print ("D = ", d)
    print ("√D = ", dr)
    print ("x₁ = ", answer1)
    print ("x₂ = ", answer2)
    print ("∙∙∙∙∙∙∙∙∙∙∙")
    ot()
def p():
    print ("∙∙∙∙∙∙∙∙∙∙∙")
    print ("ax⁴+bx²+c=0")
    a=float(input("a = "))
    def ap():
        nonlocal a
        if (a==0):
            print ("a - не может принимать значение 0")
            a=float(input("a = "))
            ap()
    ap()
    b=float(input("b = "))
    c=float(input("c = "))
    d=b**2-4*a*c
    try:
        dr=math.sqrt(d)
    except ValueError:
        print ("D = ", d)
        print ("x = нет корней")
        ap()
    print ("t = x²")
    print ("D(t) = ", d)
    print ("√D(t) = ", dr)
    answer1=(-b+dr)/(2*a)
    answer2=(-b-dr)/(2*a)
    print ("t₁ = ", answer1)
    print ("t₂ = ", answer2)
    if (answer1<0):
        print ("t₁ - не удовлетворяет условию замены (t>0)")
    else:
        answer1p = math.sqrt(answer1)
        if (answer1p==0):
            print ("x₁ = ", answer1p)
            print ("x₂ = ", answer1p)
        else:
            print ("x₁ = ", answer1p)
            print ("x₂ = ", answer1p*-1)
    if (answer2<0):
        print ("t₂ - не удовлетворяет условию замены (t>0)")
        print ("∙∙∙∙∙∙∙∙∙∙∙")
        ot()
    else:
        answer2p = math.sqrt(answer2)
        if (answer2p==0):
            print ("x₃ = ", answer2p)
            print ("x₄ = ", answer2p)
            print ("∙∙∙∙∙∙∙∙∙∙∙")
            ot()
        else:
            print ("x₃ = ", answer2p)
            print ("x₄ = ", answer2p*-1)
            print ("∙∙∙∙∙∙∙∙∙∙∙")
            ot()
def ot():
    o=int(input("Вид уравнения:\n1)Квадратное\n2)Биквадратное\nВыбор: "))
    if (o==1):
        l()
    elif (o==2):
        p()
    else:
        print ("Вы должны выбрать один из предложенных вариантов")
        ot()
ot()
    


























    
    
