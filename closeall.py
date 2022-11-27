import pyautogui as auto


def CloseAll():
    auto.PAUSE = 1
    auto.FAILSAFE = True
    auto.hotkey("ctrl", "shift", "g")
    auto.moveTo(195, 125)
    auto.click()
    auto.typewrite("📈")
    auto.hotkey("ctrl", "enter")
    auto.hotkey("ctrl", "shift", "q")
    auto.moveTo(1885, 20)
    for i in range(10):
        auto.click()
    auto.press("win")
    auto.moveTo(25, 995)
    auto.click()
    auto.moveTo(60, 880)
    auto.click()
