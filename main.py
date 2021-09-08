import gc
import pycom
import time
from machine import SD
from LIS2HH12 import LIS2HH12
from LIS2HH12 import FULL_SCALE_2G

from pycoproc_1 import Pycoproc
import _thread

def foo(delay, id):
    while True:
        time.sleep(delay)
        print('Running thread %d' % id)

#no pybytes enabled because we run out of memory... needs investigation
pycom.heartbeat(False)
pycom.rgbled(0x000500) #green

#accelerometer
lis = LIS2HH12()
print("debug: Accelerometer object created")

#battery voltage access
py = Pycoproc(2)
print("debug: Pycoproc object created")

#SD card access
sd = SD()
print("debug: SD object created")
os.mount(sd, '/sd')


buf = []
for i in range(100):
    x,y,z = lis.acceleration()
    buf.append((x,y,z))

print("log complete. attempt to write to sd")
#f = open('/sd/log1.txt','w')
#for i in range(0, len(buf)):
#    f.write('{},{},{}'.format(buf[i][0], buf[i][1], buf[0][2]))
#f.close()
print("finished")

#t = _thread.start_new_thread(foo, (10,0))
