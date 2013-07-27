import pyrobot
import termios, fcntl, sys, os
fd = sys.stdin.fileno()

oldterm = termios.tcgetattr(fd)
newattr = termios.tcgetattr(fd)
newattr[3] = newattr[3] & ~termios.ICANON & ~termios.ECHO
termios.tcsetattr(fd, termios.TCSANOW, newattr)

oldflags = fcntl.fcntl(fd, fcntl.F_GETFL)
fcntl.fcntl(fd, fcntl.F_SETFL, oldflags | os.O_NONBLOCK)



robot = pyrobot.Create("/dev/tty.USA19H142P1.1")

robot.Control()

# robot.DriveStraight(100)
# robot.SlowStop(5)

defaultSpeed = 100
currentSpeed = defaultSpeed
ratioChange = 1.5
previousState = 'z'

try:
    while 1:
        try:
            c = sys.stdin.read(1)
            if c == 'w':
            	if previousState == 'w':
            		currentSpeed = currentSpeed * ratioChange
            	else:
            		currentSpeed = defaultSpeed
            	robot.DriveStraight(currentSpeed)
            elif c == 'a':
            	robot.TurnInPlace(defaultSpeed, 'ccw')
            elif c == 's':
            	if previousState == 's':
            		currentSpeed = currentSpeed * ratioChange
            	else:
            		currentSpeed = defaultSpeed
            	robot.DriveStraight(-currentSpeed)
            elif c == 'd':
            	robot.TurnInPlace(defaultSpeed, 'cw')
            elif c == 'z':
            	robot.DriveStraight(0)

            previousState = c
        except IOError: pass
finally:
    termios.tcsetattr(fd, termios.TCSAFLUSH, oldterm)
    fcntl.fcntl(fd, fcntl.F_SETFL, oldflags)