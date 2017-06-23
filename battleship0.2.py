import random
import os
import pygame
import time

# Tables for storing the steps of the game, like placement of ships and resutls of rounds.
player1 = [["A", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["B", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["C", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["D", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["E", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["F", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["G", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["H", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["I", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["J", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

player2 = [["A", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["B", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["C", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["D", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["E", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["F", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["G", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["H", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["I", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
           ["J", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

player1a = [["A", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["B", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["C", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["D", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["E", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["F", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["G", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["H", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["I", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["J", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

player2a = [["A", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["B", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["C", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["D", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["E", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["F", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["G", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["H", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["I", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."],
            ["J", ".", ".", ".", ".", ".", ".", ".", ".", ".", "."]]

# Global table to be used by all functions.
letter_list = ["R", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
ship_list = ["X", "@", "%", "¤", "$"]
ship_list2 = ["X+", "@+", "%+", "¤+", "$+", "K+"]
p1_points = []
p2_points = []
kraken_death = []


# colorPrints:
def print_red(prt): print("\033[91m {}\033[00m" .format(prt))


def print_green(prt): print("\033[92m {}\033[00m" .format(prt))


def print_yellow(prt): print("\033[93m {}\033[00m" .format(prt))


def print_lightpurple(prt): print("\033[94m {}\033[00m" .format(prt))


def print_purple(prt): print("\033[95m {}\033[00m" .format(prt))


def print_cyan(prt): print("\033[96m {}\033[00m" .format(prt))


def print_lightgray(prt): print("\033[97m {}\033[00m" .format(prt))


def print_black(prt): print("\033[98m {}\033[00m" .format(prt))


# Prints the table in the correct format.
def print_table(table):
    num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("  " + " ".join(map(str, num)))
    for i in table:
        print(i[0], " ".join(map(str, i[1:])))


# Placement of the ships on the battlefield for the user.
def set_ship(ship_length, board, ship):
    question = "Choose where to put your ship ("+str(ship_length) + " long):"
    while True:
        try:
            counter = 0
            ship_place = input(question)
            if ship_place == "q":
                quit()
            horizontal_or_vertical = input("Horizontal(H) or vertical(V)?:")
            os.system('clear')
            y = ship_place[:1].upper()
            x = ship_place[1:]
            if horizontal_or_vertical.upper() == "V":
                for i in range(ship_length):
                    if board[letter_list.index(y)-1+i][int(x)] in ship_list:
                        print_red("Ship already in the way!")
                        print_table(board)
                        counter = 1
                        break
                if counter == 1:
                    continue
                for i in range(ship_length):
                    board[letter_list.index(y)-1+i][int(x)] = ship
            elif horizontal_or_vertical.upper() == "H":
                for i in range(ship_length):
                    if board[letter_list.index(y)-1][int(x)+i] in ship_list:
                        print_red("Ship already in the way!")
                        print_table(board)
                        counter = 1
                        break
                if counter == 1:
                    continue
                for i in range(ship_length):
                    board[letter_list.index(y)-1][int(x)+i] = ship
            else:
                raise(ValueError)
            print_table(board)
            break
        except ValueError:
            print_red("Oopsy Daisy, invalid input, try again!")
            print_table(board)
            continue
        except IndexError:
            print_red("Not enough space for ship!")
            print_table(board)
            continue


# Placement of the Kraken on the battlefield.
def place_kraken(player1, player2):
    while True:
        try:
            krakenplace = random.randrange(0, 10, 1)
            krakenplace2 = random.randrange(1, 11, 1)
            if player1[krakenplace][krakenplace2] == "." and player2[krakenplace][krakenplace2] == ".":
                player1[krakenplace][krakenplace2] = "K"
                player2[krakenplace][krakenplace2] = "K"
                break
            else:
                raise(ValueError)
        except ValueError:
            continue


# Placement of the ships on the battlefield for the computer.
def set_ship_ai(ship_length, board, ship):
    while True:
        try:
            counter = 0
            ship_place = random.randrange(0, 10, 1)
            ship_place2 = random.randrange(1, 11, 1)
            horizontal_or_vertical = random.randrange(1, 3, 1)
            y = ship_place
            x = ship_place2
            for i in range(ship_length):
                if board[y+i][x] in ship_list:
                    counter = 1
                    break
                if board[y][x+i] in ship_list:
                    counter = 1
                    break
            if counter == 1:
                continue
            if horizontal_or_vertical == 1:
                for i in range(ship_length):
                    if board[y+i][x] in ship_list:
                        counter = 1
                        break
                if counter == 1:
                    continue
                for i in range(ship_length):
                    board[y+i][x] = ship
            elif horizontal_or_vertical == 2:
                for i in range(ship_length):
                    if board[y][x+i] in ship_list:
                        counter = 1
                        break
                if counter == 1:
                    continue
                for i in range(ship_length):
                    board[y][x+i] = ship
            else:
                raise(ValueError)
            break
        except ValueError:
            continue
        except IndexError:
            continue


# Checks if the succesful attack did sink a ship or not.
def check_if_ship_sunk(ship, ship2, ship_sunk, shipsize, defend, y, x):
    if defend[letter_list.index(y)-1][int(x)] == ship:
        defend[letter_list.index(y)-1][int(x)] = ship2
        k = 0
        for i in range(10):
            j = defend[i].count(ship2)
            k = j+k
            if k == shipsize:
                print_red(ship_sunk)
                break


# Generating the events of the Kraken.
def random_events(attack, defend, points2):
    if kraken_death == []:
        event = random.randint(1, 11)
        kraken_counter = 0
        if event == 10:
                for i in attack:
                    if i.count("$") > 0:
                        for k in i:
                            if k == "$":
                                defend[attack.index(i)][i.index(k)] = "#"
                                attack[attack.index(i)][i.index(k)] = "$+"
                                points2.append(1)
                        kraken_counter = 1
                if kraken_counter == 1:
                    print_red("The Kraken ate your smallest ship. OMG")
        elif event == 5:
                for i in attack:
                    if i.count("¤") > 0:
                        for k in i:
                            if k == "¤":
                                defend[attack.index(i)][i.index(k)] = "#"
                                attack[attack.index(i)][i.index(k)] = "¤+"
                                points2.append(1)
                        kraken_counter = 1
                if kraken_counter == 1:
                    print_red("The Kraken ate one of your 3long ship. No survivers.")
        elif event == 3:
                for i in attack:
                    if i.count("%") > 0:
                        for k in i:
                            if k == "%":
                                defend[attack.index(i)][i.index(k)] = "#"
                                attack[attack.index(i)][i.index(k)] = "%+"
                                points2.append(1)
                        kraken_counter = 1
                if kraken_counter == 1:
                    print_red("The Kraken ate one of your 3long ship.Damn it, Kraken!")
        elif event == 2:
            print_lightpurple("The Kraken tried to eat your largest ship, but he couldn't swallow it. Poor hungry Kraken!")
        elif event == 1:
            print_lightpurple("The Kraken is closer than you think! Prepare yourself!")
        elif event == 8:
            print_lightpurple("The Kraken can see you, but you won't see him!")


# Shooting round for the players, Kraken activities triggered here as well.
def round(attack, defend, points, points2, name, attack1, defend2):
    who_is_next = name[:8] + "'s round!"
    who_wins = name[:8] + " wins!"
    print_yellow(who_is_next)
    random_events(attack1, defend2, points2)
    if points.count(1) == 17:
        print_red(who_wins)
        winmusic = pygame.mixer.Sound("Drama_Button.wav")
        winmusic.play()
        time.sleep(5)
        quit()
    while True:
        try:
            print_table(attack)
            fire = input("Where to shoot?:")
            if fire == "q":
                quit()
            y = fire[:1].upper()
            x = fire[1:]
            os.system('clear')
            if defend[letter_list.index(y)-1][int(float(x))] != ".":
                if defend[letter_list.index(y)-1][int(x)] in ship_list2:
                    raise(RuntimeError)
                if defend[letter_list.index(y)-1][int(float(x))] == "K":
                    defend[letter_list.index(y)-1][int(float(x))] = "K+"
                    attack1[letter_list.index(y)-1][int(float(x))] = "K+"
                    attack[letter_list.index(y)-1][int(x)] = "#"
                    defend2[letter_list.index(y)-1][int(x)] = "#"
                    kraken_death.append(1)
                    print_cyan("You killed the Kraken, no more fun!:...(")
                else:
                    print_green("Successful attack, hurray, you can shoot again!!!")
                check_if_ship_sunk("X", "X+", "Ship sunk!", 5, defend, y, x)
                check_if_ship_sunk("@", "@+", "Ship sunk!", 4, defend, y, x)
                check_if_ship_sunk("%", "%+", "Ship sunk!", 3, defend, y, x)
                check_if_ship_sunk("¤", "¤+", "Ship sunk!", 3, defend, y, x)
                check_if_ship_sunk("$", "$+", "Ship sunk!", 2, defend, y, x)
                attack[letter_list.index(y)-1][int(x)] = "#"
                points.append(1)
                if points.count(1) == 17:
                    print_red(who_wins)
                    winmusic = pygame.mixer.Sound("Drama_Button.wav")
                    winmusic.play()
                    time.sleep(5)
                    quit()
                continue
            else:
                attack[letter_list.index(y)-1][int(x)] = "/"
                print_lightpurple("Missed it, you noob!")
                break
        except SystemExit:
            quit()
        except RuntimeError:
            print_lightpurple("Why on earth would you shoot the same part of a ship twice?! Try again!")
            continue
        except (ValueError, IndexError):
            print_lightpurple("How hard it is to insert a valid input, come on?!")
            continue


# Shooting round for the computer, Kraken activities triggered here as well.
def round_ai(attack, defend, points, points2, name, attack1, defend2):
    who_is_next = name + "'s round!"
    who_wins = name + " wins!"
    print_yellow(who_is_next)
    random_events(attack1, defend2, points2)
    if points.count(1) == 17:
        print_red(who_wins)
        winmusic = pygame.mixer.Sound("Drama_Button.wav")
        winmusic.play()
        time.sleep(5)
        quit()
    while True:
        try:
            fire = random.randrange(0, 10, 1)
            fire2 = random.randrange(1, 11, 1)
            y = fire
            x = fire2
            if defend[y][x] != ".":
                if defend[y][x] in ship_list2:
                    raise(RuntimeError)
                if defend[y][x] == "K":
                    defend[y][x] = "K+"
                    attack1[y][x] = "K+"
                    attack[y][x] = "#"
                    defend2[y][x] = "#"
                    kraken_death.append(1)
                    print_cyan("Computer killed the Kraken, no more fun!:...(")
                check_if_ship_sunk("X", "X+", "Your ship sunk, OMG!", 5, defend, y, x)
                check_if_ship_sunk("@", "@+", "Your ship sunk, OMG!", 4, defend, y, x)
                check_if_ship_sunk("%", "%+", "Your ship sunk, OMG!", 3, defend, y, x)
                check_if_ship_sunk("¤", "¤+", "Your ship sunk, OMG!", 3, defend, y, x)
                check_if_ship_sunk("$", "$+", "Your ship sunk, OMG!", 2, defend, y, x)
                attack[y][x] = "#"
                points.append(1)
                if points.count(1) == 17:
                    print_red(who_wins)
                    winmusic = pygame.mixer.Sound("Drama_Button.wav")
                    winmusic.play()
                    time.sleep(5)
                    quit()
                continue
            else:
                attack[y][x] = "/"
                print_table(attack)
                break
        except SystemExit:
            quit()
        except RuntimeError:
            continue
        except:
            continue


# The game itself.
def main():
    os.system('clear')
    print_red('''

    ▄▄▄▄    ▄▄▄      ▄▄▄█████▓▄▄▄█████▓ ██▓    ▓█████   ██████  ██░ ██  ██▓ ██▓███
    ▓█████▄ ▒████▄    ▓  ██▒ ▓▒▓  ██▒ ▓▒▓██▒    ▓█   ▀ ▒██    ▒ ▓██░ ██▒▓██▒▓██░  ██▒
    ▒██▒ ▄██▒██  ▀█▄  ▒ ▓██░ ▒░▒ ▓██░ ▒░▒██░    ▒███   ░ ▓██▄   ▒██▀▀██░▒██▒▓██░ ██▓▒
    ▒██░█▀  ░██▄▄▄▄██ ░ ▓██▓ ░ ░ ▓██▓ ░ ▒██░    ▒▓█  ▄   ▒   ██▒░▓█ ░██ ░██░▒██▄█▓▒ ▒
    ░▓█  ▀█▓ ▓█   ▓██▒  ▒██▒ ░   ▒██▒ ░ ░██████▒░▒████▒▒██████▒▒░▓█▒░██▓░██░▒██▒ ░  ░
    ░▒▓███▀▒ ▒▒   ▓▒█░  ▒ ░░     ▒ ░░   ░ ▒░▓  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒░▓  ▒▓▒░ ░  ░
    ▒░▒   ░   ▒   ▒▒ ░    ░        ░    ░ ░ ▒  ░ ░ ░  ░░ ░▒  ░ ░ ▒ ░▒░ ░ ▒ ░░▒ ░
    ░    ░   ░   ▒     ░        ░        ░ ░      ░   ░  ░  ░   ░  ░░ ░ ▒ ░░░
    ░            ░  ░                      ░  ░   ░  ░      ░   ░  ░  ░ ░
        ░

    ''')
    print_yellow('''
  _______ _            _  __          _                ______    _ _ _   _
 |__   __| |          | |/ /         | |              |  ____|  | (_) | (_)
    | |  | |__   ___  | ' / _ __ __ _| | _____ _ __   | |__   __| |_| |_ _  ___  _ __
    | |  | '_ \ / _ \ |  < | '__/ _` | |/ / _ \ '_ \  |  __| / _` | | __| |/ _ \| '_ \'
    | |  | | | |  __/ | . \| | | (_| |   <  __/ | | | | |___| (_| | | |_| | (_) | | | |
    |_|  |_| |_|\___| |_|\_\_|  \__,_|_|\_\___|_| |_| |______\__,_|_|\__|_|\___/|_| |_|
''')
    print("Battleship 0.4.7 copyright by Codecool & Co.")
    pygame.init()
    music = pygame.mixer.Sound("Battleship.wav")
    music.play()
    try:
        input("Are you ready to destroy your enemy? If yes, insert any keys to go on:")
        while True:
            ai = input("Are you gonna play alone?(Y/N):")
            if ai.upper() != "Y" and ai.upper() != "N":
                print_red("Was not a proper answer!")
                continue
            break
        if ai.upper() == "Y":
            print_cyan("Don't you have any friends?")
        # Player 1 round for placing ships
        print_purple("Player 1, place your ships!")
        print_table(player1)
        set_ship(5, player1, "X")
        set_ship(4, player1, "@")
        set_ship(3, player1, "%")
        set_ship(3, player1, "¤")
        set_ship(2, player1, "$")
        input("If You are ready, insert anything to continue:")
        os.system('clear')
        # Player 2 round for placing ships
        if ai.upper() == "N":
            print_purple("Player 2, place your ships!")
            print_table(player2)
            set_ship(5, player2, "X")
            set_ship(4, player2, "@")
            set_ship(3, player2, "%")
            set_ship(3, player2, "¤")
            set_ship(2, player2, "$")
            input("Ships set for both player!!! Insert anything to continue:")
            os.system('clear')
        else:
            set_ship_ai(5, player2, "X")
            set_ship_ai(4, player2, "@")
            set_ship_ai(3, player2, "%")
            set_ship_ai(3, player2, "¤")
            set_ship_ai(2, player2, "$")
        place_kraken(player1, player2)

        # Battle
        print_red("Battle!!!")
        if ai.upper() == "N":
            while True:
                round(player1a, player2, p1_points, p2_points, "Player 1", player1, player2a)
                round(player2a, player1, p2_points, p1_points, "Player 2", player2, player1a)
        else:
            while True:
                round(player1a, player2, p1_points, p2_points, "Player 1", player1, player2a)
                round_ai(player2a, player1, p2_points, p1_points, "Computer", player2, player1a)
    except (KeyboardInterrupt, SystemExit):
        print_cyan("Bye,bye!")
        quit()


main()
