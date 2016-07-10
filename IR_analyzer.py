from matplotlib import pyplot
import serial
from serial.tools import list_ports
import sys
import multiprocessing


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
        burst = arduino.readline()
        print(burst)
        print()
        
        burst = burst.replace(b'\r', b'').replace(b'\n', b'')
        y = [abs(int(x)-49) for x in burst]
        print(y)
        x = range(0, len(y))
        Draw(x, y).start()

class Draw(multiprocessing.Process):
    def __init__(self, x, y):
        multiprocessing.Process.__init__(self)
        self.x = x
        self.y = y
        
    def run(self):
        pyplot.plot(self.x, self.y)
        pyplot.ylim(-1.5,1.5)
        pyplot.show()
        #scatterplot(self.x, self.y)
        
main()
