from promtools import Manipulator, ConveyerLineNamet #Импортируем
import time
manip=Manipulator('192.168.10.16',8888,'g')#создаем манипулятор
conv=ConveyerLineNamet('192.168.10.21',8888,'B')#Создаем конвеер
manip.toPoint(200,100,200,180,0)
conv.setSpeed(100)
time.sleep(5)
manip.toPoint(200,0,200,180,0)
conv.setSpeed(0)

