import utils.loot_reader as loot_reader
import utils.utils as utils
from utils.village import village

def test_reading_loot():
    utils.init_clash_window()

    village.town_hall_level = 10
    
    gold = loot_reader.get_resource(loot_reader.ResourceType.HOME_GOLD)
    elixir = loot_reader.get_resource(loot_reader.ResourceType.HOME_ELIXIR)
    gems = loot_reader.get_resource(loot_reader.ResourceType.HOME_GEMS)

    print(f"Gold: {gold}, Elixir: {elixir}, Gems: {gems}")

def test_attack():
    import programs.attack as attack
    attack.attack()

def test_upgrade():
    import programs.upgrade as upgrade
    upgrade.upgrade()

if __name__ == "__main__":
    #test_attack()

    test_upgrade()

    screenshot = utils.get_screenshot()
    screenshot.save("screenshot.png")