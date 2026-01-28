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

UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
SPECIAL = "!?@#$%&*"

def generate_account_credentials():
    name = get_random_name()
    email = f"{name.lower()}@gmail.com"
    password = random.randint(10**15, 10**16 - 1)
    password = str(password)

    # get random indexes for password character replacement
    password_rand_indxes = [i for i in range(16)]
    random.shuffle(password_rand_indxes)
    password_rand_indxes = password_rand_indxes[:8]

    password = list(password)

    password[password_rand_indxes[0]] = random.choice(UPPERCASE)
    password[password_rand_indxes[1]] = random.choice(LOWERCASE)
    password[password_rand_indxes[2]] = random.choice(SPECIAL)
    password[password_rand_indxes[3]] = random.choice(UPPERCASE)
    password[password_rand_indxes[4]] = random.choice(LOWERCASE)
    password[password_rand_indxes[5]] = random.choice(SPECIAL)
    password[password_rand_indxes[6]] = random.choice(UPPERCASE)
    password[password_rand_indxes[7]] = random.choice(SPECIAL)

    password = ''.join(password)

    return name, email, password

if __name__ == "__main__":
    temp = []
    for _ in range(5):
        name, email, password = generate_account_credentials()
        temp.append((name, email, password))
    
    # print all names
    for name, _, _ in temp:
        print(f"{name}")
    
    print("---------------")

    # print all emails
    for _, email, _ in temp:
        print(f"{email}")
    
    print("---------------")

    # print all passwords
    for _, _, password in temp:
        print(f"{password}")
