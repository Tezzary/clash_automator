import pyautogui
import pygetwindow as gw
from time import sleep

OFFSET_X = 64
OFFSET_Y = 36

def get_screenshot():
    #get window handle
    window = gw.getWindowsWithTitle("Clash of Clans")[0]
    #set window to foreground
    window.activate()

    sleep(0.1)

    if window:
        x, y = window.left + OFFSET_X, window.top + OFFSET_Y

        screenshot = pyautogui.screenshot(region=[x, y, window.width - OFFSET_X, window.height - OFFSET_Y])
    return screenshot

def open_clash_window():
    pyautogui.press('win')
    sleep(0.2)
    pyautogui.write('Clash of Clans')
    sleep(0.2)
    pyautogui.press('enter')
    sleep(15)  # Wait for the game to open

    windows = gw.getWindowsWithTitle("Clash of Clans")

    if not windows:
        raise Exception("Clash of Clans window did not open in open_clash_window")
    
    window = windows[0]

    if window:
        window.activate()
        window.resizeTo(1280, 720)
        sleep(0.1)

if __name__ == "__main__":
    open_clash_window()

    screenshot = get_screenshot()
    screenshot.save("screenshot.png")