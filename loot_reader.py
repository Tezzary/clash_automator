from utils import get_screenshot

def get_gold():
    screenshot = get_screenshot(1058, 25, 1217, 45)
    screenshot.save("gold.png")

def get_elixir():
    screenshot = get_screenshot(1058, 82, 1223, 102)
    screenshot.save("elixir.png")

def get_gems():
    screenshot = get_screenshot(1158, 137, 1217, 157)
    screenshot.save("gems.png")

if __name__ == "__main__":
    elixir = get_elixir()
    gold = get_gold()
    gems = get_gems()
    print(f"Gold: {gold}, Elixir: {elixir}, Gems: {gems}")