from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

text = input("What do you want to spam? ")
num = input("How many times? ")
wait = input("How much time do you want to wait between each turn?")

print("You have five seconds to go to the place where you want to start typing.\n You can quit by pressing Ctrl + C in the terminal.")

time.sleep(5)
for i in range(num):
    keyboard.type(text)
    keyboard.press(Key.enter)
    time.sleep(time)