import random

# BLACK JACK

player = []
computer = []
deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_over = False
shuffle = True


def shuffle_cards():
    if shuffle:
        _ = deck.copy()
        random.shuffle(_)
        return _ 
    else:
        return deck


def deal_cards():
    if len(player) != 2 and len(computer) != 2:
        for _ in range(2):
            player.append(random.choice(shuffle_cards()))
            computer.append(random.choice(shuffle_cards()))
    else:
        player.append(random.choice(shuffle_cards()))
        computer.append(random.choice(shuffle_cards()))


def convert_11_to_1(array):
    if 11 in array:
        # print('11 in obj')
        array.remove(11)
        array.append(1)
    return array


def dealer(obj):
    if sum(obj) < 21:
        # print('checking for 11......')
        convert_11_to_1(obj)
    obj.append(random.choice(shuffle_cards()))
    return obj


def check_blackjack():
    if sum(player) == 21 and len(player) == 2:
        print("Blackjack for palyer....")
    elif sum(computer) == 21 and len(computer) == 2:
        print("Blackjack for Computer....")
    else:
        print("Nobody got the Blackjack the game continues....")
        return sum(player), sum(computer)


def check_score():
    if sum(player) < 21 and sum(computer) < 21:
        return sum(player), sum(computer)
    else:
        if sum(player) > 21:
            print("You lost")
        elif sum(computer) > 21:
            print("Computer lost")
        else:
            return


def reveal_cards():
    hidden = computer.copy()
    hidden[0] = "*"
    return {"player cards": player, "computer cards": hidden}


def play():
    pass
