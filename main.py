import pyautogui as auto
from closeall import CloseAll

# auto.PAUSE = 0
# auto.FAILSAFE = True


# keys = auto.KEYBOARD_KEYS


def LaunchSpotify():
    auto.PAUSE = 1.5
    auto.hotkey("win", "4")
    auto.press(" ")
    auto.PAUSE = 0
    auto.hotkey("alt", "tab")


# LaunchSpotify()

CloseAll()