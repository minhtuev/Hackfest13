import pyrobot, termios, fcntl, sys, os


class ClientMotion(object):

	def __init__(self):

		fd = sys.stdin.fileno()

		newattr = termios.tcgetattr(fd)
		newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
		termios.tcsetattr(fd, termios.TCSANOW, newattr)

		oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
		fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)

		# mac: tty.KeySerial1
		# roombda: /dev/ttyUSB0 

		self.robot = pyrobot.Create("/dev/tty.KeySerial1")
		self.robot.Control()
		self.defaultSpeed = 100
		self.currentSpeed = self.defaultSpeed
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


	def flush(self):
		termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
		fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)