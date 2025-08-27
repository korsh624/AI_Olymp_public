from promtools import Manipulator, ConveyerLineNamet #Импортируем
import time
manip=Manipulator('192.168.10.18',8888,'g')#создаем манипулятор
conv=ConveyerLineNamet('192.168.10.21',8888,'B')#Создаем конвеер
# time.sleep(5)
manip.toPoint(200,0,30,180,0)
# time.sleep(2)
# manip.toPoint(200,70,30,180,0)
# time.sleep(1)
# manip.toPoint(200,-70,50,180,0)
# time.sleep(1)
# manip.toPoint(200,0,50,180,0)
# time.sleep(1)
# manip.toPoint(200,70,50,180,0)
# time.sleep(1)
# manip.toPoint(200,-70,80,180,0)
# time.sleep(1)
# manip.toPoint(200,0,80,180,0)
# time.sleep(1)
# manip.toPoint(200,70,80,180,0)
# time.sleep(1)
# manip.toPoint(200,-70,80,180,0)
# time.sleep(1)



