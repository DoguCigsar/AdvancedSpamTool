# Advanced Spam Tool v2.1 Made by DoguCigsar
# This tool works with any messaging app that uses the enter key as send

from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

print("<--Welcome to Advanced Spam Tool v2.1 Made by DoguCigsar-->")
print("<--This tool works with any messaging app that uses the enter key as send-->")

message = input("The message you want to spam (If left blank, the program will spam the letter A) (If you want to "
                "spam the amount of messages that are sent just type 'message amount'): ")
amount = input("Amount of messages to send (If left blank the program will send 1000 messages) : ")
delay = input("Delay between messages (If left blank the program will send messages with a delay of 0.1 seconds) : ")


def warningSequence():
    print("You have 10 seconds to select the messaging app!!! Also consider if you really want to do this!!!")
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


def main(delay, amount, message):
    x = 1

    if (amount == ""):
        amount = 1000
    else:
        amount = int(amount)
    if (delay == ""):
        delay = 0.1
    else:
        delay = float(delay)
    if (message == ""):
        message = "A"
        messageLen = len(message)
        numMode = False
    elif (message == "message amount"):
        numMode = True
        message = "message"
    else:
        messageLen = len(message)
        numMode = False
    warningSequence()
    while x <= amount:
        currentLetter = 0
        if (numMode == True):
            message = str(x)
            messageLen = len(message)
        while currentLetter <= messageLen - 1:
            keyboard.press(message[currentLetter])
            keyboard.release(message[currentLetter])
            currentLetter = currentLetter + 1
        keyboard.press(Key.enter)
        keyboard.release(Key.enter)
        x = x + 1
        print(x)
        time.sleep(delay)


main(delay, amount, message)
