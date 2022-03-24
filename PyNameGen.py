import random
print("PyNameGen - RPG Character Name Generator v1.0")
print("(c) 2022 by Jacqueline Daugherty")
print("---------------------------------------------")
# All these lists contain the name chunks that the random name generator uses. Don't put anything besides name chunks
# in them or shit might get weird.
human_name_beginning = ["Jo", "Ka", "Bo", "Sil", "Ro", "Ma", "Til", "Kro", "Rada", "Har", "Masa", "Kei", "Raj", "A", "Fara"]
human_name_ending = ["dulf", "sephus", "rt", "ld", "tar", "ra", "rine", "wyn", "keld", "deep", "haru", "ko", "mina", "ji"]
human_surname_beginning = ["Stone", "Tor", "Alt", "Gold", "Karst", "Galdr", "Black", "Sin", "Ka", "Mori", "Sha"]
human_surname_ending = ["smith", "berg", "sson", "sdottir", "ton", "man", "heim", "er", "stone", "y", "gh", "ur", "moto"]
elf_name_beginning = ["Eli", "Na", "Mae", "Mer", "Rue", "Ara", "Eyn", "Lys", "Maer"]
elf_name_ending = ["issa", "yae", "eilla", "dir", "tir", "ith", "los"]
elf_surname_beginning = ["Green", "Shimmer", "Dew", "Eng", "Arn", "Fayn", "Caen", "Saer", "Os"]
elf_surname_ending = ["wood", "thorn", "glade", "dale", "las", "cayn", "iel", "ona", "or", "eth", "thalla"]
dwarf_name_beginning = ["Dura", "Bali", "Gi", "Duma", "Mora", "Thon", "Dona", "Thora", "Kor"]
dwarf_name_ending = ["nin", "mli", "thoin", "din", "nir", "mil", "var", "lil"]
dwarf_surname_beginning = ["Stone", "Iron", "Deep", "Golden", "Flint", "Steel", "Bronze", "Shatter"]
dwarf_surname_ending = ["mountain", "fist", "cavern", "hammer", "carver", "maul", "axe", "belt", "shield"]
orc_name_beginning = ["Or", "Kr", "Ghor", "Gruz", "Khul", "Tamh", "Khar", "Grog"]
orc_name_ending = ["ogh", "olak", "nash", "gruk", "ukh", "ub", "uz", "nak"]
orc_surname_prefix = ["Gor'", "Khr'", "Sul-", "Ghar-", "Takh-"]
gnome_name_beginning = ["Gim", "Jink", "Tass", "Tadd", "Reev", "Mag"]
gnome_name_ending = ["geeble", "sley", "a", "ey", "illi"]
gnome_surname_beginning = ["Dimble", "Thistle", "Wander", "Gibl", "Gomber" ]
gnome_surname_ending = ["wick", "fern", "field", "boodle", "snive", "grass"]
halfling_name_beginning = ["Meria", "Pere", "Jixi", "Nixi", "Ros", "Miri", "Fenna"]
halfling_name_ending = ["doc", "grin", "dae", "ri", "ey", "la"]
halfling_surname_beginning = ["Brandy", "Proud", "Strong", "Green", "Small", "Cloud", "Long"]
halfling_surname_ending = ["buck", "foot", "heart", "belly", "hill", "river", "leaf"]
goblin_name_beginning = ["Gr", "Sreb", "Thrag", "Mok", "Kha", "Tab", "Fo"]
goblin_name_ending = ["uzz", "utat", "nar", "kk", "meeka", "ub", "zzik"]
catfolk_name_beginning = ["J'", "Kha", "M'", "Bez", "Q'", "Khoun"]
catfolk_name_middle = ["zar", "tas", "ath", "ska", "jh", "rem"]
catfolk_name_ending = ["go", "ar", "ra", "ur", "as", "ad", "kym"]

# These variables are here to make the "while" loops work correctly.
loopvar = "y"
loopvar2 = "y"

while loopvar == "y":

    player_race = input("Please enter your character's race (i.e. elf, dwarf, human, etc.):")

    if player_race == "human":
        print(random.choice(human_name_beginning) + random.choice(human_name_ending) +
        " " + random.choice(human_surname_beginning) + random.choice(human_surname_ending))

    elif player_race == "elf":
        print(random.choice(elf_name_beginning) + random.choice(elf_name_ending) +
        " " + random.choice(elf_surname_beginning) + random.choice(elf_surname_ending))

    elif player_race == "half-elf":
        coinflip = random.randrange(0, 2)
        if coinflip == 0:
            print(random.choice(human_name_beginning) + random.choice(human_name_ending) +
            " " + random.choice(elf_surname_beginning) + random.choice(elf_surname_ending))
        else:
            print(random.choice(elf_name_beginning) + random.choice(elf_name_ending) +
            " " + random.choice(human_surname_beginning) + random.choice(human_surname_ending))

    elif player_race == "dwarf":
        print(random.choice(dwarf_name_beginning) + random.choice(dwarf_name_ending) +
              " " + random.choice(dwarf_surname_beginning) + random.choice(dwarf_surname_ending))

    elif player_race == "orc":
        print(random.choice(orc_name_beginning) + random.choice(orc_name_ending) + " " +
        random.choice(orc_surname_prefix) + random.choice(orc_name_beginning) + random.choice(orc_name_ending))

    elif player_race == "half-orc":
        coinflip = random.randrange(0, 2)
        if coinflip == 0:
            print(random.choice(human_name_beginning) + random.choice(human_name_ending) +
                  " " + random.choice(orc_surname_prefix) + random.choice(orc_name_beginning) +
                  random.choice(orc_name_ending))
        else:
            print(random.choice(orc_name_beginning) + random.choice(orc_name_ending) +
                  " " + random.choice(human_surname_beginning) + random.choice(human_surname_ending))

    elif player_race == "gnome":
        print(random.choice(gnome_name_beginning) + random.choice(gnome_name_ending) +
              " " + random.choice(gnome_surname_beginning) + random.choice(gnome_surname_ending))

    elif player_race == "halfling":
        print(random.choice(halfling_name_beginning) + random.choice(halfling_name_ending) +
              " " + random.choice(halfling_surname_beginning) + random.choice(halfling_surname_ending))

    elif player_race == "goblin":
        print(random.choice(goblin_name_beginning) + random.choice(goblin_name_ending))

    elif player_race == "catfolk":
        print(random.choice(catfolk_name_beginning) + random.choice(catfolk_name_middle) + random.choice(catfolk_name_ending))

    elif player_race == "list":
        print("human, elf, half-elf, dwarf, orc, half-orc, gnome, halfling, goblin, catfolk")

    else:
        print("I'm sorry, I don't know what "+player_race+" is. Type 'list' for a list of possible choices.")

    # This loop is here to make sure the "Do you want to generate another name?" bit works correctly.
    while loopvar2 != "n" :
        loopvar2 = input("Do you want to generate another name (y/n)?")

        if  loopvar2 == "y" :
            break

        elif loopvar2 == "n" :
             loopvar = "n"

        else :
            print("Please type 'y' or 'n'.")
    else :
        print("...")
else:
    print("Thank you for using PyNameGen. Goodbye!")
