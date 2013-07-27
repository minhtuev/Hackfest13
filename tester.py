import pyrobot

robot = pyrobot.Create("/dev/tty.USA19H142P1.1")

robot.Control()

robot.DriveStraight(100)

