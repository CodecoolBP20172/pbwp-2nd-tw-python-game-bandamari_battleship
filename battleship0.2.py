import random
import os

player1 = [["A", ".", ".", ".",".",".",".",".",".",".","."],
            ["B",".",".",".",".",".",".",".",".",".","."],
            ["C",".",".",".",".",".",".",".",".",".","."],
            ["D",".",".",".",".",".",".",".",".",".","."],
            ["E",".",".",".",".",".",".",".",".",".","."],
            ["F",".",".",".",".",".",".",".",".",".","."],
            ["G",".",".",".",".",".",".",".",".",".","."],
            ["H",".",".",".",".",".",".",".",".",".","."],
            ["I",".",".",".",".",".",".",".",".",".","."],
            ["J",".",".",".",".",".",".",".",".",".","."]]

player2 = [["A",".",".",".",".",".",".",".",".",".","."],
            ["B",".",".",".",".",".",".",".",".",".","."],
            ["C",".",".",".",".",".",".",".",".",".","."],
            ["D",".",".",".",".",".",".",".",".",".","."],
            ["E",".",".",".",".",".",".",".",".",".","."],
            ["F",".",".",".",".",".",".",".",".",".","."],
            ["G",".",".",".",".",".",".",".",".",".","."],
            ["H",".",".",".",".",".",".",".",".",".","."],
            ["I",".",".",".",".",".",".",".",".",".","."],
            ["J",".",".",".",".",".",".",".",".",".","."]]

player1a = [["A",".",".",".",".",".",".",".",".",".","."],
            ["B",".",".",".",".",".",".",".",".",".","."],
            ["C",".",".",".",".",".",".",".",".",".","."],
            ["D",".",".",".",".",".",".",".",".",".","."],
            ["E",".",".",".",".",".",".",".",".",".","."],
            ["F",".",".",".",".",".",".",".",".",".","."],
            ["G",".",".",".",".",".",".",".",".",".","."],
            ["H",".",".",".",".",".",".",".",".",".","."],
            ["I",".",".",".",".",".",".",".",".",".","."],
            ["J",".",".",".",".",".",".",".",".",".","."]]

player2a = [["A",".",".",".",".",".",".",".",".",".","."],
            ["B",".",".",".",".",".",".",".",".",".","."],
            ["C",".",".",".",".",".",".",".",".",".","."],
            ["D",".",".",".",".",".",".",".",".",".","."],
            ["E",".",".",".",".",".",".",".",".",".","."],
            ["F",".",".",".",".",".",".",".",".",".","."],
            ["G",".",".",".",".",".",".",".",".",".","."],
            ["H",".",".",".",".",".",".",".",".",".","."],
            ["I",".",".",".",".",".",".",".",".",".","."],
            ["J",".",".",".",".",".",".",".",".",".","."]]

l = ["R","A","B","C","D","E","F","G","H","I","J"]
shiplist = ["X","@","%","¤","$"]
shiplist2 = ["X+","@+","%+","¤+","$+","K+"]
p1points = [] 
p2points = []
Krakendeath = []

#colorPrints:
def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))

#Prints the table in the correct format.
def printTable(a):
    num  = [1,2,3,4,5,6,7,8,9,10]
    print("  "+ " ".join(map(str,num)) )
    for i in a:
        print( i[0], " ".join(map(str,i[1:])))
        
def setship(r,board,ship):
    question = "Choose where to put your ship ("+str(r)+ " long):"
    while True:
        try:
            g = 0
            shipplace = input(question)
            if shipplace == "q":
                quit()
            horizontal_or_vertical = input("Horizontal(H) or vertical(V)?:")
            os.system('clear')
            y = shipplace[:1].upper()
            x = shipplace[1:]
            if horizontal_or_vertical.upper() == "V":
                for i in range(r):
                    if board[l.index(y)-1+i][int(x)] in shiplist:
                        print("Ship already in the way!")
                        printTable(board)
                        g = 1
                        break
                if g == 1:
                    continue
                for i in range(r):
                    board[l.index(y)-1+i][int(x)] = ship
            elif horizontal_or_vertical.upper() == "H":
                for i in range(r):
                    if board[l.index(y)-1][int(x)+i] in shiplist:
                        print("Ship already in the way!")
                        printTable(board)
                        g = 1
                        break
                if g == 1:
                    continue
                for i in range(r):   
                    board[l.index(y)-1][int(x)+i] = ship
            else: 
                raise(ValueError)
            printTable(board)
            break
        except ValueError:
            print("Oopsy Daisy, invalid input, try again!")
            printTable(board)
            continue
        except IndexError:
            print("Not enough space for ship!")
            printTable(board)
            continue

def place_kraken(player1,player2):
    while True:
        try:
            krakenplace = random.randrange(0,10,1)
            krakenplace2 = random.randrange(1,11,1)
            if player1[krakenplace][krakenplace2] == ".":
                player1[krakenplace][krakenplace2] = "K"
                player2[krakenplace][krakenplace2] = "K"
                break
            else:
                raise(ValueError)
        except ValueError:
            continue

def setship_ai(r,board,ship):
    while True:
        try:
            g = 0
            shipplace = random.randrange(0,10,1)
            shipplace2 = random.randrange(1,11,1)
            horizontal_or_vertical = random.randrange(1,3,1)
            y = shipplace
            x = shipplace2
            
            for i in range(r):
                if board[y+i][x] in shiplist:
                    g = 1
                    break
                if board[y][x+i] in shiplist:
                    g = 1
                    break
            if g == 1:
                continue
            if horizontal_or_vertical == 1:
                for i in range(r):
                    if board[y+i][x] in shiplist:
                        g = 1
                        break
                if g == 1:
                    continue   
                for i in range(r):
                    board[y+i][x] = ship
            elif horizontal_or_vertical == 2:
                for i in range(r):
                    if board[y][x+i] in shiplist:
                        g = 1
                        break
                if g == 1:
                    continue 
                for i in range(r):
                    board[y][x+i] = ship
            else: 
                raise(ValueError)
            break
        except ValueError:
            continue
        except IndexError:
            continue


def check_if_ship_sunk(ship, ship2, message,shipsize,defend,y,x):
    if defend[l.index(y)-1][int(x)] == ship:
        defend[l.index(y)-1][int(x)] = ship2
        k = 0
        for i in range(10):
            j = defend[i].count(ship2)
            k = j+k
            if k == shipsize:
                prRed(message)
                break

def random_events(attack,defend):
    if Krakendeath == [1]:
        return None
    event = random.randint(1,11)
    x = 0
    if event == 10:
            for i in attack:
                if i.count("$") > 0:
                    for k in i:
                        if k == "$":
                            defend[attack.index(i)][i.index(k)] = "#"
                            attack[attack.index(i)][i.index(k)] = "$+"
                    x = 1
            if x == 1:
                prRed("The Kraken ate your smallest ship. OMG")
    elif event == 5:
            for i in attack:
                if i.count("¤") > 0:
                    for k in i:
                        if k == "¤":
                            defend[attack.index(i)][i.index(k)] = "#"
                            attack[attack.index(i)][i.index(k)] = "¤+"
                    x = 1
            if x == 1:
                prRed("The Kraken ate one of your 3long ship. No survivers.")
    elif event == 3:
            for i in attack:
                if i.count("%") > 0:
                    for k in i:
                        if k == "%":
                            defend[attack.index(i)][i.index(k)] = "#"
                            attack[attack.index(i)][i.index(k)] = "%+"
                    x = 1
            if x == 1:
                prRed("The Kraken ate one of your 3long ship. Damn it, Kraken!")
    elif event == 2:
        prLightPurple("The Kraken tried to eat your largest ship, but luckily he couldn't swallow it. Poor hungry Kraken!")


def round(attack,defend,points,c,attack1,defend2):
    valami = c[:8] + "'s round!"
    valami2 = c[:8] + " wins!"
    prYellow(valami)
    random_events(attack1,defend2)
    while True:
        try:
            printTable(attack)
            fire = input("Where to shoot?:")
            if fire == "q":
                quit()
            y = fire[:1].upper()
            x = fire[1:]
            os.system('clear')
            if  defend[l.index(y)-1][int(float(x))] != ".":
                if defend[l.index(y)-1][int(float(x))] == "K":
                    defend[l.index(y)-1][int(float(x))] = "K+"
                    attack1[l.index(y)-1][int(float(x))] = "K+"
                    attack[l.index(y)-1][int(x)] = "#"
                    Krakendeath.append(1)
                    print("You killed the Kraken, no more fun!:...(")
                if defend[l.index(y)-1][int(x)] in shiplist2:
                    raise(RuntimeError)
                else:
                    prGreen("Successful attack, hurray, you can shoot again!!!")
                check_if_ship_sunk("X","X+","Ship sunk!",5,defend,y,x)
                check_if_ship_sunk("@","@+","Ship sunk!",4,defend,y,x)
                check_if_ship_sunk("%","%+","Ship sunk!",3,defend,y,x)
                check_if_ship_sunk("¤","¤+","Ship sunk!",3,defend,y,x)
                check_if_ship_sunk("$","$+","Ship sunk!",2,defend,y,x)
                attack[l.index(y)-1][int(x)] = "#"
                points.append(1)
                if points.count(1) == 17:
                    prRed(valami2)
                    quit()
                continue
            else:
                attack[l.index(y)-1][int(x)] = "/"
                prLightPurple("Missed it, you noob!")
                break
        except SystemExit:
            quit()
        except RuntimeError:
            prLightPurple("Why on earth would you shoot the same part of a ship twice?! Try again!")
            continue
        except:
            prLightPurple("How hard it is to insert a valid input, come on?!")
            continue


def round_ai(attack,defend,points,c,attack1,defend2):
    valami = c+ "'s round!"
    valami2 = c + " wins!"
    prYellow(valami)
    random_events(attack1,defend2)
    while True:
        try:
            fire = random.randrange(0,10,1)
            fire2 = random.randrange(1,11,1)
            y = fire
            x = fire2
            if  defend[y][x] != ".":
                if defend[y][x] == "K":
                    defend[y][x] = "K+"
                    attack1[y][x] = "K+"
                    attack[y][x] = "#"
                    Krakendeath.append(1)
                    print("Computer killed the Kraken, no more fun!:...(")
                if defend[y][x] in shiplist2:
                    raise(RuntimeError)
                check_if_ship_sunk("X","X+","Your ship sunk, OMG!",5,defend,y,x)
                check_if_ship_sunk("@","@+","Your ship sunk, OMG!",4,defend,y,x)
                check_if_ship_sunk("%","%+","Your ship sunk, OMG!",3,defend,y,x)
                check_if_ship_sunk("¤","¤+","Your ship sunk, OMG!",3,defend,y,x)
                check_if_ship_sunk("$","$+","Your ship sunk, OMG!",2,defend,y,x)
                attack[y][x] = "#"
                points.append(1)
                if points.count(1) == 17:
                    print(valami2)
                    quit()
                continue
            else:
                attack[y][x] = "/"
                printTable(attack)
                break
        except SystemExit:
            quit()
        except RuntimeError:
            continue
        except:
            continue

def main():
    os.system('clear')
    prRed('''

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
    print("Battleship 0.3.6 copyright by Codecool & Co.")
    try:
        input("Are you ready to destroy your enemy? If yes, insert any keys to go on:")
        while True:
            ai = input("Are you gonna play alone?(Y/N):")
            if ai.upper() != "Y" and ai.upper() != "N":
                print("Was not a proper answer!") 
                continue
            break
        if ai.upper() == "Y":
            prCyan("Don't you have any friends?")
        #Player 1 round for placing ships
        prPurple("Player 1, place your ships!")
        printTable(player1)
        setship(5,player1,"X")
        setship(4,player1,"@")
        setship(3,player1,"%")
        setship(3,player1,"¤")
        setship(2,player1,"$")
        input("If You are ready, insert anything to continue:")
        os.system('clear')
        #Player 2 round for placing ships
        if ai.upper() == "N":
            prPurple("Player 2, place your ships!")
            printTable(player2)
            setship(5,player2,"X")
            setship(4,player2,"@")
            setship(3,player2,"%")
            setship(3,player2,"¤")
            setship(2,player2,"$")
            input("Ships set for both player!!! Insert anything to continue:")
            os.system('clear')
        else:
            setship_ai(5,player2,"X")
            setship_ai(4,player2,"@")
            setship_ai(3,player2,"%")
            setship_ai(3,player2,"¤")
            setship_ai(2,player2,"$")
        
        place_kraken(player1,player2)

        #Battle
        prRed("Battle!!!")
        if ai.upper() == "N":
            while True:
                round(player1a,player2,p1points,"Player 1",player1,player2a)
                round(player2a,player1,p2points,"Player 2",player2,player1a)
        else: 
            while True:
                round(player1a,player2,p1points,"Player 1",player1,player2a)
                round_ai(player2a,player1,p2points,"Computer",player2,player1a)
    except (KeyboardInterrupt, SystemExit):
        print("Bye,bye!")
        quit()
main()