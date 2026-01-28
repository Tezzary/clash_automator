import pyautogui
import pygetwindow as gw
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

if __name__ == "__main__":
    open_clash_window()

    screenshot = get_screenshot()
    screenshot.save("screenshot.png")