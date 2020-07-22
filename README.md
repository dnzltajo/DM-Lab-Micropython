# Digital Modulation on Pyboard 
[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)

Experimental simulations of Digital Modulation using the Pyboard's DAC

## Library Usage
```python
import digimod
from pyb import DAC

#Data Values
stream = (0,1,1,0,1)
#Assign DAC pin X5
dac = DAC(1, bits=12) 

dmod = digimod.Dmodulate(dac)

#Amplitude shift keying
dmod.ask(0.6, 100, stream) #Amplitude(range of 0 - 1), Frequency, Data stream

#Frequency shift keying
dmod.fsk(100, 200, stream) #Space, Mark, Data stream   

#Phase shift keying
dmod.psk(-1, 100, stream) #Offset(BPSK), Frequency, Data stream
```

## Frequency Shift Keying

<p align="center">
  <img width="900" height="500" src="https://raw.githubusercontent.com/dnzltajo/DM-Lab-Micropython/master/images/Screenshot%20from%202020-05-15%2017-52-03.png">
</p> 

## Amplitude Shift Keying

<p align="center">
  <img width="900" height="500" src="https://raw.githubusercontent.com/dnzltajo/DM-Lab-Micropython/master/images/Screenshot%20from%202020-05-17%2010-46-21.png">
</p> 

## Phase Shift Keying

<p align="center">
  <img width="900" height="500" src="https://raw.githubusercontent.com/dnzltajo/DM-Lab-Micropython/master/images/Screenshot%20from%202020-05-17%2010-54-58.png">
</p> 

## References

* [Micropython DAC Class](http://docs.micropython.org/en/v1.9.3/pyboard/library/pyb.DAC.html)

* [Advanced Electronic Communications Systems by Wayne Tomasi](https://gradeup-question-images.grdp.co/liveData/f/2017/12/Advanced_Electronic_Communications_Systems_0130453501.pdf-86.pdf)


