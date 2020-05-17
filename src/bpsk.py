import math
import micropython
import pyb
from array import array
from pyb import DAC

#NOTE: For frequencies less than 100 change delay to 1000ms

#Buffer containing sine wave 
buf = array('H', 2048 + int(2047 * math.sin(2 * math.pi * i /256)) for i in range(256))

#Offset Sine wave for BPSK
buf2 = array('H', 2048 + int(2047 *(-1 * (math.sin(2 * math.pi * i /256)))) for i in range(256))


#X5 on Pyboard
dac = DAC(1, bits=12)

#Simulates a stream of Data
stream = (0,1,0,1,1,1)


def psk():
    dac.write_timed(buf, 100 * len(buf), mode=DAC.CIRCULAR)
    pyb.delay(60)
    return
    
while(1):
    for i in stream:
        if i == 0:
            #Logic 0 signal
            dac.write_timed(buf2, 100 * len(buf), mode=DAC.CIRCULAR)
            pyb.delay(60)
        else:  
            psk()





