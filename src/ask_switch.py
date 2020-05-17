import math
import pyb
from array import array
from pyb import DAC, Switch

#NOTE: For frequencies less than 100Hz change delay to 1000ms

#USR Switch on Pyboard
sw = Switch()

#Buffer containing sine wave 
buf = array('H', 2048 + int(2047 * math.sin(2 * math.pi * i /256)) for i in range(256))

#Amplitude shift, Change '0.25'
#Range from 0 to 1
buf2 = array('H', 2048 + int(2047 * (0.25*(math.sin(2 * math.pi * i /256)))) for i in range(256))

#X5 on Pyboard
dac = DAC(1, bits=12)

def ask():
    #Logic 1 signal
    dac.write_timed(buf, 100 * len(buf), mode=DAC.CIRCULAR)
    pyb.delay(60)
    return

while(1):
    #Logic 0 signal
    dac.write_timed(buf2, 100 * len(buf2), mode=DAC.CIRCULAR)
    pyb.delay(60)
    #Callback to ask for Logic 1
    sw.callback(ask)





