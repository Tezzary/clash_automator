import pyautogui
import pygetwindow
from time import sleep

OFFSET_X = 64
OFFSET_Y = 36

def get_screenshot():
    #get window handle
    window = pygetwindow.getWindowsWithTitle("Clash of Clans")[0]
    #set window to foreground
    window.activate()

    sleep(0.1)

    if window:
        x, y = window.left + OFFSET_X, window.top + OFFSET_Y

        screenshot = pyautogui.screenshot(region=[x, y, window.width - OFFSET_X, window.height - OFFSET_Y])
    return screenshot

if __name__ == "__main__":
    screenshot = get_screenshot()
    screenshot.save("screenshot.png")