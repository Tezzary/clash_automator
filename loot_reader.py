from utils import get_screenshot
import easyocr
import numpy as np
from PIL import Image, ImageFilter

reader = easyocr.Reader(
    ['en'],
    gpu=False
)
def read_num_from_screenshot(screenshot):
    result = reader.readtext(
        np.array(screenshot),
        allowlist='0123456789lI|',
        detail=0,
    )
    if result:
        result = ''.join(result)
        result = result.replace('l', '1').replace('I', '1').replace('|', '1')

        num = int(result)
        return num

def filter_image(screenshot: Image.Image) -> Image.Image:
    # make greyscale
    screenshot = screenshot.convert("L")

    def threshold(pixel):
        return 255 if pixel > 245 else 0

    screenshot = screenshot.point(threshold, mode='L')

    screenshot = screenshot.filter(ImageFilter.SMOOTH)
    screenshot = screenshot.filter(ImageFilter.SHARPEN)

    return screenshot

def get_gold():
    screenshot = get_screenshot(1058, 25, 1217, 45)
    screenshot = filter_image(screenshot)
    screenshot.save("gold.png")
    return read_num_from_screenshot(screenshot)
    

def get_elixir():
    screenshot = get_screenshot(1058, 82, 1223, 102)
    screenshot = filter_image(screenshot)
    screenshot.save("elixir.png")
    return read_num_from_screenshot(screenshot)

def get_gems():
    screenshot = get_screenshot(1158, 137, 1217, 157)
    screenshot = filter_image(screenshot)
    screenshot.save("gems.png")
    return read_num_from_screenshot(screenshot)

if __name__ == "__main__":
    import utils
    utils.init_clash_window()
    elixir = get_elixir()
    gold = get_gold()
    gems = get_gems()
    print(f"Gold: {gold}, Elixir: {elixir}, Gems: {gems}")