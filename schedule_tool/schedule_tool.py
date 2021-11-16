import sys
import eel
import pyautogui

eel.init('web')
ctrl = None


@eel.expose
def main(sleep_min, x, y):
    sleep_min = int(float(sleep_min)*60)
    global ctrl
    ctrl = True
    do_something(sleep_min, int(x), int(y))


@eel.expose
def exit_():
    global ctrl
    ctrl = False


def do_something(sleep_min, x, y):
    while ctrl:
        eel.sleep(sleep_min)
        pyautogui.click(x=x, y=y, clicks=1, button='left')


eel.start('index.html', size=(800, 800), port=8080)
