from utils import get_screenshot
import easyocr
import numpy as np

reader = easyocr.Reader(
    ['en'],
    gpu=False
)
def read_num_from_screenshot(screenshot):
    result = reader.readtext(
        np.array(screenshot),
        allowlist='0123456789',
        detail=0,
    )
    if result:
        num = int(result[0])
        return num

def get_gold():
    screenshot = get_screenshot(1058, 25, 1217, 45)
    screenshot.save("gold.png")
    return read_num_from_screenshot(screenshot)
    

def get_elixir():
    screenshot = get_screenshot(1058, 82, 1223, 102)
    screenshot.save("elixir.png")
    return read_num_from_screenshot(screenshot)

def get_gems():
    screenshot = get_screenshot(1158, 137, 1217, 157)
    screenshot.save("gems.png")
    return read_num_from_screenshot(screenshot)

if __name__ == "__main__":
    elixir = get_elixir()
    gold = get_gold()
    gems = get_gems()
    print(f"Gold: {gold}, Elixir: {elixir}, Gems: {gems}")