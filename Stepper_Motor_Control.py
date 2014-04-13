import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ControlPin = [7,11,13,15]

for pin in ControlPin:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin,0)

def clockwise(steps):

    fwd_seq= [
        [1,0,0,0],
        [1,1,0,0],
        [0,1,0,0],
        [0,1,1,0],
        [0,0,1,0],
        [0,0,1,1],
        [0,0,0,1],
        [1,0,0,1] ]

    for i in range(steps):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(ControlPin[pin], fwd_seq[halfstep] [pin])
            time.sleep(0.001)

    GPIO.cleanup 
    

def counter_clockwise(steps):

    fwd_seq= [
        [1,0,0,1],
        [0,0,0,1],
        [0,0,1,1],
        [0,0,1,0],
        [0,1,1,0],
        [0,1,0,0],
        [1,1,0,0],
        [1,0,0,0] ]

    for i in range(steps):
        for halfstep in range(8):
            for pin in range(4):
                GPIO.output(ControlPin[pin], fwd_seq[halfstep] [pin])
            time.sleep(0.001)

    GPIO.cleanup    

clockwise(1024)

time.sleep(3)

counter_clockwise(1024)
        
    


        
    
