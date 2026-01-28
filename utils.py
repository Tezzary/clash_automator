import pyautogui
import pygetwindow as gw
import random
from time import sleep

OFFSET_X = 64
OFFSET_Y = 36
PLAY_WINDOW_SIZE_X = 1276
PLAY_WINDOW_SIZE_Y = 716


def get_window_pos(title="Clash of Clans"):
    #get window handle
    window = gw.getWindowsWithTitle(title)[0]
    #set window to foreground
    window.activate()

    if window:
        return window.left + OFFSET_X, window.top + OFFSET_Y
    return None

def get_screenshot(start_x=0, start_y=0, end_x=PLAY_WINDOW_SIZE_X, end_y=PLAY_WINDOW_SIZE_Y):
    x, y = get_window_pos()

    sleep(0.1)

    screenshot = pyautogui.screenshot(region=[x + start_x, y + start_y, end_x - start_x, end_y - start_y])
    return screenshot

def open_clash_window():
    if not get_window_pos():
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
        window.resizeTo(1280 + OFFSET_X, 720 + OFFSET_Y)
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