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
player1 = [["A",".",".",".",".",".",".",".",".",".","."],
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
            carrierp1 = input(question)
            if carrierp1 == "q":
                quit()
            carrierp1place = input("Horizontal(H) or vertical(V)?:")
            os.system('clear')
            y = carrierp1[:1].upper()
            x = carrierp1[1:]
            if carrierp1place.upper() == "V":
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
            elif carrierp1place.upper() == "H":
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
            carrierp1 = random.randrange(0,10,1)
            carrierp2 = random.randrange(1,11,1)
            carrierp1place = random.randrange(1,3,1)
            y = carrierp1
            x = carrierp2
            
            for i in range(r):
                if board[y+i][x] in shiplist:
                    g = 1
                    break
                if board[y][x+i] in shiplist:
                    g = 1
                    break
            if g == 1:
                continue
            if carrierp1place == 1:
                for i in range(r):
                    if board[y+i][x] in shiplist:
                        g = 1
                        break
                if g == 1:
                    continue   
                for i in range(r):
                    board[y+i][x] = ship
            elif carrierp1place == 2:
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
            if  defend[l.index(y)-1][int(x)] != ".":
                if defend[l.index(y)-1][int(x)] in shiplist2:
                    raise(RuntimeError)
                else:
                    prGreen("Successful attack, hurray, you can shoot again!!!")
                if defend[l.index(y)-1][int(x)] == "X":
                    defend[l.index(y)-1][int(x)] = "X+"
                    k = 0
                    for i in range(10):
                        j = defend[i].count("X+")
                        k = j+k
                        if k == 5:
                            prRed("Ship sunk!")
                            break
                if defend[l.index(y)-1][int(x)] == "@":
                    defend[l.index(y)-1][int(x)] = "@+"
                    k = 0
                    for i in range(10):
                        j = defend[i].count("@+")
                        k = j+k
                        if k == 4:
                            prRed("Ship sunk!")
                            break
                if defend[l.index(y)-1][int(x)] == "%":
                    defend[l.index(y)-1][int(x)] = "%+"
                    k = 0
                    for i in range(10):
                        j = defend[i].count("%+")
                        k = j+k
                        if k == 3:
                            prRed("Ship sunk!")
                            break
                if defend[l.index(y)-1][int(x)] == "¤":
                    defend[l.index(y)-1][int(x)] = "¤+"
                    k = 0
                    for i in range(10):
                        j = defend[i].count("¤+")
                        k = j+k
                        if k == 3:
                            prRed("Ship sunk!")
                            break
                if defend[l.index(y)-1][int(x)] == "$":
                    defend[l.index(y)-1][int(x)] = "$+"
                    k = 0
                    for i in range(10):
                        j = defend[i].count("$+")
                        k = j+k
                        if k == 2:
                            prRed("Ship sunk!")
                            break
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
                if defend[y][x] == "X":
                    defend[y][x] = "X+"
                    k = 0
                    for i in range(10):
                        j = defend[i].count("X+")
                        k = j+k
                        if k == 5:
                            print("Your ship sunk, OMG!")
                            break
                if defend[y][x] == "@":
                    defend[y][x] = "@+"
                    k = 0
                    for i in range(10):
                        j = defend[i].count("@+")
                        k = j+k
                        if k == 4:
                            print("Your ship sunk, OMG!")
                            break
                if defend[y][x] == "%":
                    defend[y][x] = "%+"
                    k = 0
                    for i in range(10):
                        j = defend[i].count("%+")
                        k = j+k
                        if k == 3:
                            print("Your ship sunk, OMG!")
                            break
                if defend[y][x] == "¤":
                    defend[y][x] = "¤+"
                    k = 0
                    for i in range(10):
                        j = defend[i].count("¤+")
                        k = j+k
                        if k == 3:
                            print("Your ship sunk, OMG!")
                            break
                if defend[y][x] == "$":
                    defend[y][x] = "$+"
                    k = 0
                    for i in range(10):
                        j = defend[i].count("$+")
                        k = j+k
                        if k == 2:
                            print("Your ship sunk, OMG!")
                            break
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
