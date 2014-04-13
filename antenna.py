import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

ControlPin = [7,11,13,15]

for pin in ControlPin:
  GPIO.setup(pin, GPIO.OUT)
  GPIO.output(pin,0)

def set(property, value):
	try:
		f = open("/sys/class/rpi-pwm/pwm0/" + property, 'w')
		f.write(value)
		f.close()
	except:
		print("Error writing to: " + property + " value: " + value)


def elevation(angle):
	set("servo", str(angle))


set("delayed", "0")
set("mode", "servo")
set("servo_max", "180")
set("active", "1")

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