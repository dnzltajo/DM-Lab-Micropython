#-----------------------------------------------------------------------
#This is free and unencumbered software released into the public domain.
#Released under the Unlicense License (Unlicense)
#(C) 2020 Denzel Tajo
#-----------------------------------------------------------------------
from math import sin, pi
from array import array
from pyb import DAC, delay


class Dmodulate(object):
    
    def __init__(self, dac):
        self.dac=dac    
        
    def ask(self, amp, freq, stream):
        buf = array('H', 2048 + int(2047 * sin(2 * pi * i /256)) for i in range(256))
        buf2 = array('H', 2048 + int(2047 * (amp*(sin(2 * pi * i /256)))) for i in range(256))
        while(1):
            for i in stream:
                if i == 0:
                    #Logic 0 signal
                    self.dac.write_timed(buf2, freq * len(buf2), mode=DAC.CIRCULAR)
                    delay(60)
                else:
                    #Logic 1 signal
                    self.dac.write_timed(buf, freq * len(buf), mode=DAC.CIRCULAR)
                    delay(60)
                    
        
    def fsk(self,freq_s, freq_m, stream):
        buf = array('H', 2048 + int(2047 * sin(2 * pi * i /256)) for i in range(256))
        while(1):   
            for i in stream:
                if i == 0:
                    #Space Frequency (Fs), Logic 0
                    self.dac.write_timed(buf, freq_s * len(buf), mode=DAC.CIRCULAR)
                    delay(60)
                else:
                    #Mark Frequency (Fm), Logic 1
                    self.dac.write_timed(buf, freq_m * len(buf), mode=DAC.CIRCULAR)
                    delay(60)
                    
    def psk(self, offset, freq, stream):
        buf = array('H', 2048 + int(2047 * sin(2 * pi * i /256)) for i in range(256))
        buf2 = array('H', 2048 + int(2047 *(offset * (sin(2 * pi * i /256)))) for i in range(256))
        while(1):
            for i in stream:
                if i == 0:
                    #Logic 0 signal
                    self.dac.write_timed(buf2, freq * len(buf2), mode=DAC.CIRCULAR)
                    delay(60)
                else:
                    #Logic 1 signal
                    self.dac.write_timed(buf, freq * len(buf), mode=DAC.CIRCULAR)
                    delay(60)
