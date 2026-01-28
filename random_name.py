import random

clash_names = [
    "BarbaricKing",
    "NightRaider",
    "ClanCrusher",
    "FireWarden",
    "StoneHammer",
    "DarkElixirX",
    "WarHogz",
    "ShadowChief",
    "IronVillage",
    "FrostGiant",
    "SkullBreaker",
    "RageSpell",
    "SavageBase",
    "EagleStrike",
    "BattleSmith",
    "InfernoLord",
    "GoldRush",
    "WarMachineX",
    "RoyalRaider",
    "ClashMaster",
    "SilentPekka",
    "DragonFury",
    "TribeSlayer",
    "StormVillage",
    "GrimBarbarian",
    "Warborn",
    "LightningClan",
    "HeroicChief",
    "SavageKnight",
    "BaseDestroyer",
    "DarkHammer",
    "PhoenixRise",
    "IronClasher",
    "VoidRaider",
    "AncientWar",
    "BattleHaven",
    "FeralKing",
    "RogueVillage",
    "FireClan",
    "SteelWarden",
    "MythicRaid",
    "ThunderBase",
    "BloodElixir",
    "WarpathX",
    "ClashForge",
    "ShadowVillage",
    "BruteForce",
    "NightClasher"
]

def get_random_name():
    return random.choice(clash_names) + str(random.randint(1, 99999))

if __name__ == "__main__":
    name = get_random_name()
    email = f"{name.lower()}@gmail.com"
    password = str(abs(hash(name)) % (10 ** 12))

    print("Name:", name)
    print("Email:", email)
    print("Password:", password)