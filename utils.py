import pyautogui
import pygetwindow as gw
import random
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

def click_on_screen(x, y, max_offset=5, min_time=0.05, max_time=0.25, max_delay=0.5):
    offset_x = random.randint(-max_offset, max_offset)
    offset_y = random.randint(-max_offset, max_offset)

    pyautogui.moveTo(x + offset_x, y + offset_y, duration=random.uniform(min_time, max_time))

    sleep(random.uniform(0, max_delay))

    pyautogui.mouseDown()
    sleep(random.uniform(0.05, 0.2))
    pyautogui.mouseUp()

buttons = {
    
}

if __name__ == "__main__":
    #open_clash_window()

    screenshot = get_screenshot()
    screenshot.save("screenshot.png")