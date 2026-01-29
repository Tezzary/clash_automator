import pyautogui
import pygetwindow as gw
import random
from time import sleep
import cv2
import numpy as np

OFFSET_X = 64
OFFSET_Y = 36
PLAY_WINDOW_SIZE_X = 1276
PLAY_WINDOW_SIZE_Y = 716


def get_window_pos(title="Clash of Clans") -> tuple[int, int]:
    #get window handle
    window = gw.getWindowsWithTitle(title)[0]
    #set window to foreground
    window.activate()

    if window:
        return window.left + OFFSET_X, window.top + OFFSET_Y
    raise Exception("No window found with title: " + title)

def get_screenshot(start_x=0, start_y=0, end_x=PLAY_WINDOW_SIZE_X, end_y=PLAY_WINDOW_SIZE_Y):
    x, y = get_window_pos()

    sleep(0.1)

    screenshot = pyautogui.screenshot(region=[x + start_x, y + start_y, end_x - start_x, end_y - start_y])
    return screenshot

def init_clash_window():
    try:
        get_window_pos()
    except Exception:
        pyautogui.press('win')
        sleep(0.2)
        pyautogui.write('Clash of Clans')
        sleep(0.2)
        pyautogui.press('enter')
        sleep(60)  # Wait for the game to open
        print("opened Clash of Clans")
    windows = gw.getWindowsWithTitle("Clash of Clans")

    if not windows:
        raise Exception("Clash of Clans window did not open in init_clash_window")
    
    window = windows[0]

    if window:
        window.activate()
        window.resizeTo(1280 + OFFSET_X, 720 + OFFSET_Y)
        sleep(0.1)

def click_on_screen(x, y, max_offset=5, min_press_time=0.05, max_press_time=0.25, max_delay=5):
    win_x, win_y = get_window_pos()
    x += win_x
    y += win_y

    offset_x = random.randint(-max_offset, max_offset)
    offset_y = random.randint(-max_offset, max_offset)

    pyautogui.moveTo(x + offset_x, y + offset_y)

    sleep(random.uniform(0, max_delay))

    pyautogui.mouseDown()
    sleep(random.uniform(min_press_time, max_press_time))
    pyautogui.mouseUp()

buttons = {
    "Attack!" : (71, 648, 10),
    "Find a Match" : (144, 503),
    "X Attack!" : (1083, 615),
    "End Battle" : (77, 566),
    "Next" : (1189, 551),
}

def normalize_camera():
    win_x, win_y = get_window_pos()
    center_x = win_x + PLAY_WINDOW_SIZE_X // 2
    center_y = win_y + PLAY_WINDOW_SIZE_Y // 2

    pyautogui.moveTo(center_x, center_y)
    sleep(0.1)

    for _ in range(20):
        pyautogui.scroll(-500)
        sleep(0.1)

    pyautogui.mouseDown()
    sleep(0.1)
    pyautogui.moveTo(center_x - 350, center_y - 350, duration=0.5)
    sleep(0.1)


    pyautogui.mouseUp()

def find_location_on_screen(image_path, threshold=0.5):
    screenshot = get_screenshot()
    cv_screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)
    template = cv2.imread(image_path, cv2.IMREAD_COLOR)
    result = cv2.matchTemplate(cv_screenshot, template, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(max_val)
    if max_val >= threshold:
        template_height, template_width = template.shape[:2]
        center_x = max_loc[0] + template_width // 2
        center_y = max_loc[1] + template_height // 2
        return center_x, center_y
    return None

if __name__ == "__main__":
    init_clash_window()

    

    normalize_camera()

    screenshot = get_screenshot()
    screenshot.save("screenshot.png")

    #click_on_screen(*buttons["Attack!"])