from utils.utils import normalize_camera, find_location_on_screen, click_on_screen
import pyautogui
from time import sleep
import cv2

def upgrade():
    normalize_camera()

    click_on_screen(615, 210, max_offset=1, min_press_time=0.2, max_press_time=0.4)
    sleep(2)

    pos_x, pos_y = find_location_on_screen("resources/upgrade_button.png")
    print(pos_x, pos_y)
    if pos_x and pos_y:
        click_on_screen(pos_x, pos_y)
        sleep(2)



if __name__ == "__main__":
    upgrade()
    