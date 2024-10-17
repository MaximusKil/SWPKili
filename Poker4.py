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

def nummer_ziehungen(draw=5):
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

def hand_check_value(pokerhand, ausgabe = 1):
    value = hand_value(pokerhand)
    checking = 0
    for _ in range(13):
        result = value.count(pokerdeck[checking])
        if result > 1 and ausgabe == 1:
            if result == 2:
                ausgabe = 2
                value.remove(pokerdeck[checking])
                value.remove(pokerdeck[checking])
                result2 = check_hand_fullhouse_twopair(value)
                if result2 == 2:
                    ausgabe = 6
                if result2 == 3:
                    ausgabe = 7
            elif result == 3:
                ausgabe = 3
                value.remove(pokerdeck[checking])
                value.remove(pokerdeck[checking])
                value.remove(pokerdeck[checking])
                result2 = check_hand_fullhouse_twopair(value)
                if result2 == 2:
                    ausgabe = 7
            elif result == 4:
                ausgabe = 4
        checking += 1
    if ausgabe == 1:
        ausgabe = check_hand_straight(value)
    return ausgabe

def check_hand_straight(pokerhand):
    value = hand_value(pokerhand)
    value = hand_sort(value)
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
    return 1

def check_hand_fullhouse_twopair(pokerhand):
    value = hand_value(pokerhand)
    checking = 0
    ausgabe = 1
    for _ in range(13):
        result = value.count(pokerdeck[checking])
        if result > 1:
            if result == 2:
                ausgabe = 2
            elif result == 3:
                ausgabe = 3
        checking += 1
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

def check_royal(pokerhand):
    value = hand_value(pokerhand)
    value = hand_sort(value)
    if value[-1] == "A" and value[-2] == "K":
        return "RoyalFlush"
    return "StraightFlush"

def playing_hand():
    pokerhand = nummer_ziehungen()
    valuehand = hand_name(hand_check_value(pokerhand))
    farbhand = hand_check_farbe(pokerhand)
    if farbhand == "Flush" and valuehand == "Straight":
        return check_royal(pokerhand)
    elif farbhand == "Flush":
        if valuehand != "Four" and valuehand != "FullHouse":
            return "Flush"
    return valuehand

def playing(number):
    for _ in range(number):
        pokercombinations[playing_hand()] += 1
    print(pokercombinations)

playing(1000000)