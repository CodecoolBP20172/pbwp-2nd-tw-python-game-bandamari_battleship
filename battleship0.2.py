import random
import os
def prRed(prt): print("\033[91m {}\033[00m" .format(prt))
def prGreen(prt): print("\033[92m {}\033[00m" .format(prt))
def prYellow(prt): print("\033[93m {}\033[00m" .format(prt))
def prLightPurple(prt): print("\033[94m {}\033[00m" .format(prt))
def prPurple(prt): print("\033[95m {}\033[00m" .format(prt))
def prCyan(prt): print("\033[96m {}\033[00m" .format(prt))
def prLightGray(prt): print("\033[97m {}\033[00m" .format(prt))
def prBlack(prt): print("\033[98m {}\033[00m" .format(prt))
os.system('clear')
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
shiplist2 = ["X+","@+","%+","¤+","$+"]
p1points = [] 
p2points = []

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
            ship_place = input(question)
            if ship_place == "q":
                quit()
            horizont_or_vertical_input = input("Horizontal(H) or vertical(V)?:")
            os.system('clear')
            y = ship_place[:1].upper()
            x = ship_place[1:]
            if horizont_or_vertical_input.upper() == "V":
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
            elif horizont_or_vertical_input.upper() == "H":
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

def setshipai(r,board,ship):
    while True:
        try:
            g = 0
            ship_place = random.randrange(0,10,1)
            ship_place2 = random.randrange(1,11,1)
            horizont_or_vertical_input = random.randrange(1,3,1)
            y = ship_place
            x = ship_place2
            
            for i in range(r):
                if board[y+i][x] in shiplist:
                    g = 1
                    break
                if board[y][x+i] in shiplist:
                    g = 1
                    break
            if g == 1:
                continue
            if horizont_or_vertical_input == 1:
                for i in range(r):
                    if board[y+i][x] in shiplist:
                        g = 1
                        break
                if g == 1:
                    continue   
                for i in range(r):
                    board[y+i][x] = ship
            elif horizont_or_vertical_input == 2:
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

#Player 1 round
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
input("Are you ready to destroy your enemy? If yes, insert any keys to go on:")
while True:
    ai = input("Are you gonna play alone?(Y/N):")
    if ai.upper() != "Y" and ai.upper() != "N":
        print("Was not a proper answer!") 
        continue
    break
if ai.upper() == "Y":
    prCyan("Don't you have any friends?")
prPurple("Player 1, place your ships!")
printTable(player1)
setship(5,player1,"X")
setship(4,player1,"@")
setship(3,player1,"%")
setship(3,player1,"¤")
setship(2,player1,"$")
input("If You are ready, insert anything to continue:")
os.system('clear')
#Player 2 round
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
    setshipai(5,player2,"X")
    setshipai(4,player2,"@")
    setshipai(3,player2,"%")
    setshipai(3,player2,"¤")
    setshipai(2,player2,"$")


#Battle
prRed("Battle!!!")

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


def round(attack,defend,points,c):
    valami = c[:8] + "'s round!"
    valami2 = c[:8] + " wins!"
    prYellow(valami)
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


def roundai(attack,defend,points,c):
    valami = c+ "'s round!"
    valami2 = c + " wins!"
    prYellow(valami)
    while True:
        try:
            fire = random.randrange(0,10,1)
            fire2 = random.randrange(1,11,1)
            y = fire
            x = fire2
            if  defend[y][x] != ".":
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


if ai.upper() == "N":
    while True:
        round(player1a,player2,p1points,"Player 1")
        round(player2a,player1,p2points,"Player 2")
else: 
   while True:
        round(player1a,player2,p1points,"Player 1")
        roundai(player2a,player1,p2points,"Computer")
