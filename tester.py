import pyrobot
import termios, fcntl, sys, os
fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)



robot = pyrobot.Create("/dev/ttyUSB0")

robot.Control()

# robot.DriveStraight(100)
# robot.SlowStop(5)

defaultSpeed = 100
currentSpeed = defaultSpeed
ratioChange = 1.5
previousState = 'z'

class ClientMotion(object):

	robot
	defaultSpeed
	currentSpeed
	ratioChange 
	previousState

	def __init__(self):
		self.robot = pyrobot.Create("/dev/ttyUSB0")
		self.robot.Control()
		self.defaultSpeed = 100
		self.currentSpeed = defaultSpeed
		self.ratioChange = 1.5
		self.previousState = 'z'


	def move(self, command):
	    c = command
	    if c == 'w':
	    	if self.previousState == 'w':
	    		self.currentSpeed = self.currentSpeed * self.ratioChange
	    	else:
	    		self.currentSpeed = self.defaultSpeed
	    	self.robot.DriveStraight(self.currentSpeed)
	    elif c == 'a':
	    	self.robot.TurnInPlace(self.defaultSpeed, 'ccw')
	    elif c == 's':
	    	if self.previousState == 's':
	    		self.currentSpeed = self.currentSpeed * self.ratioChange
	    	else:
	    		self.currentSpeed = self.defaultSpeed
	    	self.robot.DriveStraight(-self.currentSpeed)
	    elif c == 'd':
	    	self.robot.TurnInPlace(self.defaultSpeed, 'cw')
	    elif c == 'm':
	    	self.robot.Sing('C2')
	    elif c == 'n':
	    	self.robot.Sing('C#2')
	    elif c == 'z':
	    	self.robot.DriveStraight(0)

	   	self.previousState = c