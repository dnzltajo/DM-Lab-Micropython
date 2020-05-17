import math
import pyb
from array import array
from pyb import DAC, Switch

#NOTE: For frequencies less than 100Hz change delay to 1000ms

#USR Switch on Pyboard
sw = Switch()

#Buffer containing sine wave 
buf = array('H', 2048 + int(2047 * math.sin(2 * math.pi * i /256)) for i in range(256))

#X5 on Pyboard
dac = DAC(1, bits=12)

def fsk():
    #Mark Frequency (Fm), Logic 1
    dac.write_timed(buf, 500 * len(buf), mode=DAC.CIRCULAR)
    pyb.delay(60)
    return


while(1):
    #Logic 0
    dac.write_timed(buf, 100 * len(buf), mode=DAC.CIRCULAR)    
    pyb.delay(60)
    #Callback to fsk for Logic 1
    sw.callback(fsk)






