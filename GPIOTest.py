from time import sleep
import RPi.GPIO as GPIO

# to use Raspberry Pi BCM pin numbers
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel
GPIO.setup(20, GPIO.OUT) #LED1
GPIO.setup(21, GPIO.OUT) #LED2
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #
GPIO.setup(16, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #
GPIO.setup(13, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #
GPIO.setup(6, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #
GPIO.setup(12, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #
GPIO.setup(5, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #
#GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Chip Select 1
#GPIO.setup(8, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Chip Select 0
#GPIO.setup(11, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # MISO
#GPIO.setup(9, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # MOSI
#GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # SCLK
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #
GPIO.setup(15, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #
GPIO.setup(14, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #
GPIO.setup(0, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #
GPIO.setup(1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) #






while 1:
    # ##LED Test
    # GPIO.output(20, GPIO.HIGH)
    # sleep(1)
    # GPIO.output(20, GPIO.LOW)
    # sleep(1)
    # GPIO.output(20, GPIO.HIGH)
    # sleep(1)
    # GPIO.output(20, GPIO.LOW)
    # sleep(1)
    # GPIO.output(20, GPIO.HIGH)
    # sleep(1)
    #
    # GPIO.output(21, GPIO.HIGH)
    # sleep(1)
    # GPIO.output(21, GPIO.LOW)
    # sleep(1)
    # GPIO.output(21, GPIO.HIGH)
    # sleep(1)
    # GPIO.output(21, GPIO.LOW)
    # sleep(1)
    # GPIO.output(21, GPIO.HIGH)
    # sleep(1)

    if GPIO.input(26):
        print("Port 26 is 1/HIGH/True - LED ON")
    if GPIO.input(16):
        print("Port 16 is 1/HIGH/True - LED ON")
    if GPIO.input(13):
        print("Port 13 is 1/HIGH/True - LED ON")
    if GPIO.input(6):
        print("Port 6 is 1/HIGH/True - LED ON")
    if GPIO.input(12):
        print("Port 12 is 1/HIGH/True - LED ON")
    if GPIO.input(5):
        print("Port 5 is 1/HIGH/True - LED ON")
    if GPIO.input(22):
        print("Port 22 is 1/HIGH/True - LED ON")
    if GPIO.input(23):
        print("Port 23 is 1/HIGH/True - LED ON")
    if GPIO.input(27):
        print("Port 27 is 1/HIGH/True - LED ON")
    if GPIO.input(17):
        print("Port 17 is 1/HIGH/True - LED ON")
    if GPIO.input(18):
        print("Port 18 is 1/HIGH/True - LED ON")
    if GPIO.input(15):
        print("Port 15 is 1/HIGH/True - LED ON")
    if GPIO.input(4):
        print("Port 4 is 1/HIGH/True - LED ON")
    if GPIO.input(14):
        print("Port 14 is 1/HIGH/True - LED ON")
    if GPIO.input(0):
        print("Port 0 is 1/HIGH/True - LED ON")
    if GPIO.input(1):
        print("Port 1 is 1/HIGH/True - LED ON")
    sleep(0.1)
