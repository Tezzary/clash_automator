import pyautogui

def get_screenshot():
    screenshot = pyautogui.screenshot()
    return screenshot

if __name__ == "__main__":
    screenshot = get_screenshot()
    screenshot.show()