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
    password_rand_indxes = [random.randint(0, len(password)-1) for _ in range(3)]
    password = list(password)
    password[password_rand_indxes[0]] = chr(random.randint(65, 90))  # Uppercase
    password[password_rand_indxes[1]] = chr(random.randint(97, 122)) # Lowercase
    password[password_rand_indxes[2]] = chr(random.randint(33, 47))  # Special character
    password = ''.join(password)


    print("Name:", name)
    print("Email:", email)
    print("Password:", password)
    
    print(f"{name} {email} {password}")