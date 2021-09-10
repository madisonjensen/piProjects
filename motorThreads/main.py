
from threading import Thread, Lock
from time import sleep
import keyboard
from adafruit_motorkit import Motorkit

kit = Motorkit
mutex = Lock


def upWait():
    while True:
        keyboard.wait('up')
        print("forward")
        mutex.acquire()
        kit.motor1.throttle = 1.0
        kit.motor2.throttle = -1.0
        sleep(0.1)
        kit.motor1.throttle = 0.0
        kit.motor2.throttle = 0.0
        mutex.release()


def rightWait():
    while True:
        keyboard.wait('right')
        print("right")
        mutex.acquire()
        kit.motor1.throttle = -1.0
        kit.motor2.throttle = -1.0
        sleep(0.1)
        kit.motor1.throttle = 0.0
        kit.motor2.throttle = 0.0
        mutex.release()


def downWait():
    while True:
        keyboard.wait('down')
        print("backwards")
        mutex.acquire()
        kit.motor1.throttle = -1.0
        kit.motor2.throttle = 1.0
        sleep(0.1)
        kit.motor1.throttle = 0.0
        kit.motor2.throttle = 0.0
        mutex.release()


def leftWait():
    while True:
        keyboard.wait('left')
        print("left")
        mutex.acquire()
        kit.motor1.throttle = 1.0
        kit.motor2.throttle = 1.0
        sleep(0.1)
        kit.motor1.throttle = 0.0
        kit.motor2.throttle = 0.0
        mutex.release()


upThread = Thread(target=upWait())
rightThread = Thread(target=rightWait())
downThread = Thread(target=downWait())
leftThread = Thread(target=leftWait())

upThread.start()
rightThread.start()
downThread.start()
leftThread.start()
