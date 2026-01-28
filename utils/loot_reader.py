from utils.utils import get_screenshot
import easyocr
import numpy as np
from PIL import Image, ImageFilter
from enum import Enum
from utils.village import village
import logging

class ResourceType(Enum):
    HOME_GOLD = "home_gold"
    HOME_ELIXIR = "home_elixir"
    HOME_DARK_ELIXIR = "home_dark_elixir"
    HOME_GEMS = "home_gems"

    ATTACK_GOLD = "attack_gold"
    ATTACK_ELIXIR = "attack_elixir"
    ATTACK_DARK_ELIXIR = "attack_dark_elixir"

_resource_type = {
    ResourceType.HOME_GOLD: (1058, 25, 1217, 45),
    ResourceType.HOME_ELIXIR: (1058, 82, 1223, 102),
    ResourceType.HOME_DARK_ELIXIR: (),
    ResourceType.HOME_GEMS: (),

    ResourceType.ATTACK_GOLD: (50, 84, 180, 105),
    ResourceType.ATTACK_ELIXIR: (50, 116, 180, 137),
    ResourceType.ATTACK_DARK_ELIXIR: (),
}

def get_resource(resource_type: ResourceType, debug = False) -> int:
    if village.town_hall_level < 7:
        # we DONT have DE yet
        if resource_type in [ResourceType.HOME_DARK_ELIXIR, ResourceType.ATTACK_DARK_ELIXIR]:
            logging.error("Tried getting dark elixar before th 7")
            return -1
        
        if resource_type == ResourceType.HOME_GEMS:
            screenshot = get_screenshot(1158, 137, 1217, 157)
            screenshot = _filter_image(screenshot)
            return _read_num_from_screenshot(screenshot)
    
    screenshot = get_screenshot(*_resource_type[resource_type])
    if debug:
        screenshot.save(f"debug_loot_{resource_type.value}.png")
    screenshot = _filter_image(screenshot)
    return _read_num_from_screenshot(screenshot)

_reader = easyocr.Reader(
    ['en'],
    gpu=False
)
def _read_num_from_screenshot(screenshot) -> int:
    result = _reader.readtext(
        np.array(screenshot),
        allowlist='0123456789lI|',
        detail=0,
    )
    if result:
        result = ''.join(result)
        result = result.replace('l', '1').replace('I', '1').replace('|', '1')

        num = int(result)
        logging.info("Read number from screenshot: %d", num)
        return num
    return -1

def _filter_image(screenshot: Image.Image) -> Image.Image:
    # make greyscale
    screenshot = screenshot.convert("L")

    def threshold(pixel):
        return 255 if pixel > 220 else 0

    screenshot = screenshot.point(threshold, mode='L')

    screenshot = screenshot.filter(ImageFilter.SMOOTH)
    screenshot = screenshot.filter(ImageFilter.SHARPEN)

    return screenshot