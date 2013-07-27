import pyrobot

robot = pyrobot.Create("/dev/tty.USA19H142P1.1")

robot.Control()

robot.TurnInPlace(0, 'ccw')
# robot.DriveStraight(100)
# robot.SlowStop(5)

