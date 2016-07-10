from matplotlib import pyplot
from numpy import arange
import bisect
import serial
from serial.tools import list_ports
import sys


def scatterplot(x,y):
    pyplot.plot(x,y,'b.')
    pyplot.xlim(min(x)-1,max(x)+1)
    pyplot.ylim(min(y)-1,max(y)+1)
    pyplot.show()
    
    
def main():
    print('Select the port:')
    ports = {}
    i = 0
    for port in list_ports.comports():
        ports[str(i)] = port
        
    [print('[' + i + '] ' + port.name) for (i,port) in ports.items()]
    
    port = input('> ')
    
    arduino = serial.Serial('/dev/' + ports[port].name, 9600)
    
    while True:
        print(arduino.readline())

main()
