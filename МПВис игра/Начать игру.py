#Импорт нужных модулей
from pathlib import Path
from ast import literal_eval as le
import builtins
import time
import os

#Получение пути к файлу
pyt=Path(__file__).resolve().parent
pytnew=pyt/'Данные'/'Информация прогресса'
pytosob=pyt/'Данные'/'Переменные'

#Запись переменных в фаил
osob={'kol': None, 'hearts': None, 'itog1': None, 'itog2': None}
def fosob(key, zn):
    global osob
    with open(pytosob, mode='r', encoding='utf-8') as file:
        content = file.read().strip()
        if content:
            osob = le(content)  
    osob[key]=zn   
    with open(pytosob, mode='w', encoding='utf-8') as file:
        file.write(str(osob)+'\n')
        
#Загрузка переменных из файла
def losob():
    global kol, hearts, itog1, itog2, osob
    if pytosob.exists():
        with open(pytosob, mode='r', encoding='utf-8') as file:
            content = file.read().strip()
            if content:
                osob = le(content)
                    
                kol = osob.get('kol', 0)
                hearts = osob.get('hearts', 0)
                itog1 = osob.get('itog1', 0)
                itog2 = osob.get('itog2', 0)
    
#Функция для очистки консоли
def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

#Секретные команды (теперь в каждом input доп проверка)
oldinput=builtins.input
def newinput(txt=''):
    while True:
        res=oldinput(txt)
        if res=='':
            print('Поле не должно быть пустым!')
        elif res=='*exit':
            with open(pytnew, mode='w'):
                pass
            with open(pytosob, mode='w'):
                pass
            exit()
        elif res=='*pashalka':
            print('♥ 350 ♥')
            input()
            with open(pytnew, mode='w'):
                pass
            with open(pytosob, mode='w'):
                pass
            exit()
        elif res=='*vin1':
            itog1=99
            fosob('itog1', itog1)
        elif res=='*vin2':
            itog2=99
            fosob('itog2', itog2)
        else:
            return res 
builtins.input=newinput

#Запускается при старте игры
def start_game():
    print('Добро пожаловать в игру!')
    print('Для создания игры скажите, из скольки слов\nбудут состоять испытания: ', end='')

    #Две переменные отвечающие за игровой процесс
    global kol
    global hearts
    kol=int(input())
    hearts=int(input('количество жизней: '))
    
    #Запись в фаил
    fosob('kol', kol)
    fosob('hearts', hearts)
    clear_console()

#Регистрация игроков______________________
def regplayer():

    print(txtp)

    #Логин
    log=input('Логин: ')

    #Проверка на уникальность логина
    with open(pytnew, mode='r', encoding='utf-8') as file:
        prowlog=file.readline().strip()
    while prowlog == log:
        print ('Пользователь с таким именем уже существует.')
        log=input('Логин: ')

    #Пароль
    password=input('Пароль: ')

    #Создается список составленных слов
    global words
    words=[]
    i=1
    while i<=kol:
        proword=input('Слово '+str(i)+': ')
        if proword in words:
            print('Данное слово уже используеться!')
        else:
            words.append(proword)
            i+=1
    clear_console()

    #Запись информации
    with open(pytnew, mode='a', encoding='utf-8') as file:
        file.write(log+'\n'+password+'\n'+str(words)+'\n')

#Шаблон регистрации для 1 игрока    
def regp1():
    global txtp
    txtp='Игрок P1'
    regplayer()

#Шаблон регистрации для 2 игрока
def regp2():
    global txtp
    txtp='Игрок P2'
    regplayer()

#Геймплей_________________________________

#Цвета
RED='\033[31m'
GREEN='\033[32m'
YELLOW='\033[33m'
RESET='\033[0m'

#Итоги
itog1=-1
itog2=-1
def itogres():
    with open(pytnew, mode='r', encoding='utf-8') as file:
        fullsp=file.readlines()
    print('Подведем итоги:')
    
    if itog1>itog2:
        print('Победил ', fullsp[0].strip(), '! ( ', itog1, ' : ', itog2, ' )', sep='')
    elif itog2>itog1:
        print('Победил ', fullsp[3].strip(), '! ( ', itog1, ' : ', itog2, ' )', sep='')
    else:
        print('Победила дружба! ( ', itog1, ' : ', itog2, ' )', sep='')

    ywed=input('Игроки, поставьте "+", если все увидели результат: ')
    while ywed!='+':
        ywed=input('Поставьте "+", если увидели результат:')
    with open(pytnew, mode='w'):
        pass
    with open(pytosob, mode='w'):
        pass

#Онализирует попытку
def onalisator(a):
    global ygad
    ygad=0
    if a==spslov[i]:
        ygad=1
    a=list(a)
    orslovo=list(spslov[i])

    #Указывает цветом на буквы
    for w in range (kolbykv[i]):
        if a[w] == orslovo[w]:
            a[w]=GREEN+a[w]+RESET
        elif a[w] in orslovo:
            a[w]=YELLOW+a[w]+RESET
        else:
            a[w]=RED+a[w]+RESET
    global resylt
    resylt=''.join(a)

#Основная оболочка
def gameplay():

    #Количество букв и список слов
    global kolbykv
    global spslov
    spslov=le(fullsp[n].strip())
    kolbykv=[len(sl) for sl in spslov]

    #Угадывание слов (их перебор)
    global i
    for i in range (kol):
        print(i+1, 'слово', kolbykv[i], 'букв')

        #Угадывание букв (перебор жизней/попыток)
        global heartsr
        heartsr=hearts
        while heartsr !=0:            
            onalis=input(str(heartsr)+' | ')
            
            #Проверка на количество букв
            while kolbykv[i]!=len(onalis):
                print('Введите слово строго из', kolbykv[i], 'букв!')
                onalis=input(str(heartsr)+' | ')
                
            onalisator(onalis)
            print(resylt)

            #Проверка угадано ли слово (если нет -жизнь)
            if ygad==1:
                spslov[i]=1 #Если угадано то 1
                break
            else:
                heartsr-=1
        if heartsr==0:
            spslov[i]=0 #Если не угадано то 0

    #Время посмотерь на последний резельтат
    print('Ожидайте результата...')
    time.sleep(3)
    clear_console()

#Шаблон для 1 игрока
def startgp1():
    global n
    global name
    n=5
    name=fullsp[3].strip()
    print('Испытание от игрока', name)
    gameplay()
    global itog1
    itog1=0
    for podit in spslov:
        itog1+=int(podit)
    fosob('itog1', itog1)

#Шаблон для 2 игрока
def startgp2():
    global n
    global name
    n=2
    name=fullsp[0].strip()
    print('Испытание от игрока', name)
    gameplay()
    global itog2
    itog2=0
    for podit in spslov:
        itog2+=int(podit)
    fosob('itog2', itog2)

#Аунтетификация пользователя______________
def aynt():
    
    print('Да начнем игру!')

    #Создание списка из полученного файла
    with open(pytnew, mode='r', encoding='utf-8') as file:
        global fullsp
        fullsp=file.readlines()

    #Запись существующих логинов        
    prowerka1=fullsp[0].strip()
    prowerka2=fullsp[3].strip()
        
    #Проверка логина
    prowlog=input('Логин: ')
    while prowlog not in (prowerka1, prowerka2):
        print('Пользователь с таким именем не найден.')
        prowlog=input('Логин: ')
    
    #Опроделение индекса пароля
    if prowlog==prowerka1:
        index=1
    else:
        index=4
    
    #Запись пароля
    prowerka=fullsp[index].strip()
    
    #Проверка пароля
    prowpas=input('Пароль: ')
    while prowpas!=prowerka:
        print('Неверный пароль.')
        prowpas=input('Пароль: ')

    #Запуск игры (для 1 и 2 игрока отдельно)
    if index==1:
        startgp1()
    else:
        startgp2()

#Код воединое_____________________________
        
#Чтоб всегда был цветной текст        
if os.name=='nt':
    os.system('')

#Загрузка данных    
losob()

#Количество строк в файле для проверки
celikom=0
with open(pytnew, 'r', encoding='utf-8') as file:
    celikom=len(file.readlines())

#Запуск для разных ситуаций    
if celikom==0 and osob['hearts']==None:
    start_game()
    regp1()
    regp2()
    aynt()
    aynt()
    losob()
    itogres()
        
elif celikom==0:
    regp1()
    regp2()
    aynt()
    aynt()
    losob()
    itogres()

elif celikom==3:
    regp2()
    aynt()
    aynt()
    losob()
    itogres()
        
elif itog1==None and itog2==None:
    aynt()
    aynt()
    losob()
    itogres()
        
elif (itog1!=None and itog2==None) or (itog1==None and itog2!=None):
    aynt()
    losob()
    itogres()
        
else:
    itogres()
