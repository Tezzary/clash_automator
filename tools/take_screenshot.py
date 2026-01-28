# cahnge program path to be 1 file up
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))


from utils.utils import get_screenshot

def take_screenshot(path: str) -> None:
    screenshot = get_screenshot()
    screenshot.save(path)

take_screenshot("screenshot.png")