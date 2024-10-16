import random
pokerdeck = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "B", "Q", "K", "A"]
pokerdeck += pokerdeck
pokerdeck += pokerdeck
pokercombinations = {"HighCard": 0 , "Pair": 0 , "TwoPair": 0, "Three": 0, "Straight": 0 , "Flush": 0, "FullHouse": 0, "Four": 0, "StraightFlush": 0, "RoyalFlush": 0}

def handziehen(draw=5):
    pokerhand = []
    pokerdeck2 = pokerdeck[:]
    kreuz = 13
    pik = 25
    herz = 37
    max = len(pokerdeck2)-1
    for _ in range(draw):
        a = random.randint(0,max)
        if a < kreuz:
            pokerhand.append(pokerdeck2[a]+"♣")
            kreuz -= 1
            pik -= 1
            herz -= 1
        elif kreuz <= a < pik:
            pokerhand.append(pokerdeck2[a] + "♠")
            pik -= 1
            herz -= 1
        elif pik <= a < herz:
            pokerhand.append(pokerdeck2[a] + "♥")
            herz -= 1
        elif a >= herz:
            pokerhand.append(pokerdeck2[a] + "♦")
        draw -= 1
        pokerdeck2.pop(a)
        max -= 1
    return pokerhand

def nummer_ziehungen(number = 1,draw=5):
    for _ in range(number):
        pokerhand = handziehen(draw)
    return pokerhand

def hand_value(pokerhand):
    pokerhandwert = []
    position = 0
    for _ in range(len(pokerhand)):
        pokerhandwert1 = [number for number in pokerhand[position] if number not in "♣♠♥♦"]
        pokerhandwertstr = "".join(pokerhandwert1)
        pokerhandwert.append(pokerhandwertstr)
        position += 1
    return pokerhandwert

def hand_farbe(pokerhand):
    pokerhandfarbe = []
    position = 0
    for _ in range(len(pokerhand)):
        pokerhandfarbe1 = [number for number in pokerhand[position] if number in "♣♠♥♦"]
        pokerhandfarbestr = "".join(pokerhandfarbe1)
        pokerhandfarbe.append(pokerhandfarbestr)
        position += 1
    return pokerhandfarbe

def hand_check_value(pokerhand, first = 0, second = 1, ausgabe = 1):
    value = hand_value(pokerhand)
    firstval = ""
    secondval = ""
    for _ in range(len(value)-1-first):
        for _ in range(len(value)-1-first):
            if second < len(value):
                if value[first] == value[second]:
                    ausgabe += 1
                    secondval = value[second]
                second += 1
        if ausgabe == 1:
            first += 1
            second = first+1
    if ausgabe == 2 or ausgabe == 3:
        firstval = value[first]
        value.remove(firstval)
        value.remove(secondval)
        ausgabe2 = check_hand_fullhouse_twopair(value)
        if ausgabe2 == 3:
            ausgabe = 7
        if ausgabe2 == 2:
            ausgabe = 6
    if ausgabe == 1:
        value = hand_sort(value)
        ausgabe = check_hand_straight(value)
    return ausgabe

def check_hand_straight(pokerhand):
    value = hand_value(pokerhand)
    straight = 12
    for _ in range(12):
        if value == pokerdeck[straight:straight+5]:
            return 8
        straight += 1
    straight = 12
    value[0], value[1], value[2], value[3], value[4] = value[4], value[0], value[1], value[2], value[3]
    for _ in range(12):
        if value == pokerdeck[straight:straight+5]:
            return 8
        straight += 1
    return 0

def check_hand_fullhouse_twopair(pokerhand):
    value = hand_value(pokerhand)
    first = 0
    second = 1
    ausgabe = 1
    for _ in range(len(value)-1-first):
        for _ in range(len(value)-1-first):
            if second < len(value):
                if value[first] == value[second]:
                    ausgabe += 1
                second += 1
            if ausgabe == 1:
                first += 1
                second = first + 1
    return ausgabe

def hand_check_farbe(pokerhand):
    ausgabe = "n"
    farbe = hand_farbe(pokerhand)
    if farbe[0] == farbe[1] == farbe[2] == farbe[3] == farbe[4]:
        ausgabe = "Flush"
    return ausgabe

def hand_sort(pokerhand):
    value = hand_value(pokerhand)
    value2 = []
    pos = 0
    posval = 0
    for _ in range(13):
        for _ in range(5):
            if pokerdeck[pos] == value[posval]:
                value2.append(value[posval])
            posval += 1
            if posval == 5:
                posval = 0
        pos += 1
    return value2

def hand_name(value : int):
    if value == 1: return "HighCard"
    elif value == 2: return "Pair"
    elif value == 3: return "Three"
    elif value == 4: return "Four"
    elif value == 6: return "TwoPair"
    elif value == 7: return "FullHouse"
    elif value == 8: return "Straight"
    return "no"

pokerhandrig = ["2♣", "3♣", "2♣", "3♣", "3♣"]
pokerhandrigvalue = hand_check_value(pokerhandrig)
pokerhandrigfarbe = hand_check_farbe(pokerhandrig)
pokerhandrig = hand_sort(pokerhandrig)
print(pokerhandrig)
pokerhandrigvalue = hand_name(pokerhandrigvalue)
print(pokerhandrigvalue)
print(pokerhandrigfarbe)