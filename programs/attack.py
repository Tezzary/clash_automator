import time
import utils.utils as utils
import utils.loot_reader as loot_reader
from utils.village import village
import logging

# town hall : total weighted loot
loot_threshold = {
    1 : 10_000,
    2 : 10_000,
    3 : 10_000,
    4 : 50_000,
    5 : 100_000,
    6 : 100_000,
    7 : 100_000,
    8 : 100_000,
    9 : 100_000,
    10 : 500_000,
    11 : 1_000_000,
    12 : 1_000_000,
    13 : 1_000_000,
    14 : 1_000_000,
    15 : 2_000_000,
    16 : 2_000_000,
    17 : 2_000_000,
    18 : 2_000_000
}

def _start_attack():
    utils.click_on_screen(*utils.buttons["Attack!"])
    utils.click_on_screen(*utils.buttons["Find a Match"])
    utils.click_on_screen(*utils.buttons["X Attack!"])

def attack():
    utils.init_clash_window()

    logging.info("Starting attack ")
    _start_attack()

    found_base = False
    while not found_base:
        # chill a lil bit
        time.sleep(3)

        # read loot
        gold = loot_reader.get_resource(loot_reader.ResourceType.ATTACK_GOLD)
        elixir = loot_reader.get_resource(loot_reader.ResourceType.ATTACK_ELIXIR)
        dark_elixar = 0
        
        if village.town_hall_level >= 7:
            dark_elixar = loot_reader.get_resource(loot_reader.ResourceType.ATTACK_DARK_ELIXIR)

        if gold == -1 or elixir == -1 or dark_elixar == -1:
            # clouds in the way or something
            continue

        gold_weight = 1
        elixir_weight = 1
        dark_elixir_weight = 10

        total_weighted_loot = gold_weight * gold + elixir_weight * elixir + dark_elixir_weight * dark_elixar

        if total_weighted_loot > loot_threshold[village.town_hall_level]:
            found_base = True
        else:
            utils.click_on_screen(*utils.buttons["Next"])