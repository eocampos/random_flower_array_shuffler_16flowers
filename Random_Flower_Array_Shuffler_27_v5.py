# Written for Python 2.7
import random
ArrayFlowers01 = ["curved_1", "curved_2", "curved_3", "curved_4", "curved_5", "curved_6", "curved_7", "curved_8", "flat___1", "flat___2", "flat___3", "flat___4", "flat___5", "flat___6", "flat___7", "flat___8"]
ArrayFlowers02 = ["curved_1", "curved_2", "curved_3", "curved_4", "curved_5", "curved_6", "curved_7", "curved_8", "flat___1", "flat___2", "flat___3", "flat___4", "flat___5", "flat___6", "flat___7", "flat___8"]
ArrayFlowers03 = ["curved_1", "curved_2", "curved_3", "curved_4", "curved_5", "curved_6", "curved_7", "curved_8", "flat___1", "flat___2", "flat___3", "flat___4", "flat___5", "flat___6", "flat___7", "flat___8"]
ArrayFlowers04 = ["curved_1", "curved_2", "curved_3", "curved_4", "curved_5", "curved_6", "curved_7", "curved_8", "flat___1", "flat___2", "flat___3", "flat___4", "flat___5", "flat___6", "flat___7", "flat___8"]
ArrayFlowers05 = ["curved_1", "curved_2", "curved_3", "curved_4", "curved_5", "curved_6", "curved_7", "curved_8", "flat___1", "flat___2", "flat___3", "flat___4", "flat___5", "flat___6", "flat___7", "flat___8"]
ArrayFlowers06 = ["curved_1", "curved_2", "curved_3", "curved_4", "curved_5", "curved_6", "curved_7", "curved_8", "flat___1", "flat___2", "flat___3", "flat___4", "flat___5", "flat___6", "flat___7", "flat___8"]
ArrayFlowers07 = ["curved_1", "curved_2", "curved_3", "curved_4", "curved_5", "curved_6", "curved_7", "curved_8", "flat___1", "flat___2", "flat___3", "flat___4", "flat___5", "flat___6", "flat___7", "flat___8"]
ArrayFlowers08 = ["curved_1", "curved_2", "curved_3", "curved_4", "curved_5", "curved_6", "curved_7", "curved_8", "flat___1", "flat___2", "flat___3", "flat___4", "flat___5", "flat___6", "flat___7", "flat___8"]
ArrayFlowers09 = ["curved_1", "curved_2", "curved_3", "curved_4", "curved_5", "curved_6", "curved_7", "curved_8", "flat___1", "flat___2", "flat___3", "flat___4", "flat___5", "flat___6", "flat___7", "flat___8"]
ArrayFlowers10 = ["curved_1", "curved_2", "curved_3", "curved_4", "curved_5", "curved_6", "curved_7", "curved_8", "flat___1", "flat___2", "flat___3", "flat___4", "flat___5", "flat___6", "flat___7", "flat___8"]

random.shuffle(ArrayFlowers01)
random.shuffle(ArrayFlowers02)
random.shuffle(ArrayFlowers03)
random.shuffle(ArrayFlowers04)
random.shuffle(ArrayFlowers05)
random.shuffle(ArrayFlowers06)
random.shuffle(ArrayFlowers07)
random.shuffle(ArrayFlowers08)
random.shuffle(ArrayFlowers09)
random.shuffle(ArrayFlowers10)

print
print "A1"
for shape in ArrayFlowers01:
    if ArrayFlowers01.index(shape) + 1 < 10:
        print "", ArrayFlowers01.index(shape) + 1, shape
    else:
        print ArrayFlowers01.index(shape) + 1, shape

print
print "A2"
for shape in ArrayFlowers02:
    if ArrayFlowers02.index(shape) + 1 < 10:
        print "", ArrayFlowers02.index(shape) + 1, shape
    else:
        print ArrayFlowers02.index(shape) + 1, shape
        
print
print "A3"
for shape in ArrayFlowers03:
    if ArrayFlowers03.index(shape) + 1 < 10:
        print "", ArrayFlowers03.index(shape) + 1, shape
    else:
        print ArrayFlowers03.index(shape) + 1, shape
        
print
print "A4"
for shape in ArrayFlowers04:
    if ArrayFlowers04.index(shape) + 1 < 10:
        print "", ArrayFlowers04.index(shape) + 1, shape
    else:
        print ArrayFlowers04.index(shape) + 1, shape
        
print
print "A5"
for shape in ArrayFlowers05:
    if ArrayFlowers05.index(shape) + 1 < 10:
        print "", ArrayFlowers05.index(shape) + 1, shape
    else:
        print ArrayFlowers05.index(shape) + 1, shape
        
print
print "A6"
for shape in ArrayFlowers06:
    if ArrayFlowers06.index(shape) + 1 < 10:
        print "", ArrayFlowers06.index(shape) + 1, shape
    else:
        print ArrayFlowers06.index(shape) + 1, shape
        
print
print "A7"
for shape in ArrayFlowers07:
    if ArrayFlowers07.index(shape) + 1 < 10:
        print "", ArrayFlowers07.index(shape) + 1, shape
    else:
        print ArrayFlowers07.index(shape) + 1, shape
        
print
print "A8"
for shape in ArrayFlowers08:
    if ArrayFlowers08.index(shape) + 1 < 10:
        print "", ArrayFlowers08.index(shape) + 1, shape
    else:
        print ArrayFlowers08.index(shape) + 1, shape
        
print
print "A9"
for shape in ArrayFlowers09:
    if ArrayFlowers09.index(shape) + 1 < 10:
        print "", ArrayFlowers09.index(shape) + 1, shape
    else:
        print ArrayFlowers09.index(shape) + 1, shape
        
print
print "A10"
for shape in ArrayFlowers10:
    if ArrayFlowers10.index(shape) + 1 < 10:
        print "", ArrayFlowers10.index(shape) + 1, shape
    else:
        print ArrayFlowers10.index(shape) + 1, shape
# balls