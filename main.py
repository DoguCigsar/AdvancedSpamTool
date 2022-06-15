from pynput.keyboard import Key, Controller
import time
from numpy import nan as NaN

keyboard = Controller()
key = "A"

amount = input("Amount of messages to send (If left blank the program will send 1000 messages) : ")
delay = input("Delay between messages (If left blank the program will send messages with a delay of 0.1 seconds) : ")

def warningSequence():
    print("You have 10 seconds to select the messaging app!!! Also to consider if you really want to do this!!!")
    print("10")
    time.sleep(1)
    print("9")
    time.sleep(1)
    print("8")
    time.sleep(1)
    print("7")
    time.sleep(1)
    print("6")
    time.sleep(1)
    print("5")
    time.sleep(1)
    print("4")
    time.sleep(1)
    print("3")
    time.sleep(1)
    print("2")
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("GO!")
def main(delay, amount):
    x = 0
    if (amount == ""):
        amount = 1000
    else:
        amount = int(amount)
    if (delay == ""):
        delay = 0.1
    else:
        delay = float(delay)
    warningSequence()
    while x < amount:
             keyboard.press(key)
             keyboard.release(key)
             keyboard.press(Key.enter)
             keyboard.release(Key.enter)
             x = x + 1
             print(x)
             time.sleep(delay)
main(delay, amount)
