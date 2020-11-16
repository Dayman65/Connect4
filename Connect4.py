#Updated print game Board function
def printGameBoard(gameBoard):
    line =''
    for r in range(rows, 0,-1):
        line =line + "|"
        for c in range(1, columns+1 ,1):
            line = line + gameBoard["R"+ str(r) + "C" + str(c)]+"|"
        line = line +'\n'
    print(line)

#Number of rows and columns
rows = 6
columns = 7
gameBoard ={ }
#Create gameBoard based on number of rows and columns
for c in range(1, columns+1, 1):
    for r in range(1, rows+1, 1):
        gameBoard["R"+str(r)+"C"+str(c)] =" "
        
print(gameBoard)
        

for i in range(50):
    if i % 2 ==0:
        turn ="Z"
    else:
        turn="O"
    
    while True:
        print("Player "+ turn +" enter a Column: 1 -7")
        column = input()
        if 1 <= int(column) <= 7:
            break
        
    intColumn =int(column)
    
    #place piece in first empty space
    for k in range(7):
        space = intColumn + (k * 7)
        print("K = " + str(k))
        print("Space = " + str(space))
        if gameBoard[space] ==" ":
            gameBoard[space] = turn
            print(gameBoard[space])
            break

    numConnected = 0
    #Check for 4 in a row horizontal
    for h in range(space, (7-(6+space)%7+space), 1):
        
        print(gameBoard[h])
        if gameBoard[h] == turn:
            numConnected += 1
            #print("H Match :"+str(numConnected))
        else:
            break
    for hr in range(space-1,space-1-(space-1)%7,-1):      
        if gameBoard[hr] == turn:
            numConnected += 1
            #print("HR Match :" +str(numConnected))
        else:
            break

    if numConnected >= 4:
        printGameBoard(gameBoard)
        print("Player "+ turn+" wins!")
        break
        
    numConnected =0
    #Check for 4 in a row vertical
    for v in range(space, 50, 7):
        if gameBoard[v] == turn:    
            numConnected += 1
            #print("V Match: " + str(numConnected))
        else:
            break
    for vr in range(space-7, 0, -7):
        if gameBoard[vr] == turn:    
            numConnected += 1
            #print("VR Match: " + str(numConnected))
        else:
            break
    if numConnected >= 4:
        printGameBoard(gameBoard)
        print("Player "+ turn+" wins!")
        break
        
    numConnected =0

    #Check for 4 in a row diagonally left to right from bottom to top
    for d in range(space, 50, 8):
        if space in(7,6,14,5,13,21,43,36,44,29,37,45):
            break
        else:
            print("d = " + str(d))
            if gameBoard[d] ==turn:
                numConnected += 1
                #print("D Match: " + str(numConnected))
            else:
                break
    for dr in range(space-8,0,-8):
        if space in(7,6,14,5,13,21,43,36,44,29,37,45):
            break
        else:
            print("dr = " + str(dr))
            if gameBoard[dr] == turn:
                numConnected +=1
                #print("DR Match: " +str(numConnected))
            else:
                break
    if numConnected >= 4:
        printGameBoard(gameBoard)
        print("Player "+ turn+" wins!")
        break

    numConnected =0

    #Check for 4 in a row diagonally
    for dl in range(space, 44, 6):
        if space in(1,2,3,8,9,15,49,48,42,47,41,35):
            break
        else:
            print("dl = " + str(dl))
            if gameBoard[dl] ==turn:
                numConnected += 1
                print("DL Match: " + str(numConnected))
            else:
                break
    for dlr in range(space-6,3,-6):
        if space in(1,2,3,8,9,15,49,48,42,47,41,35):
            break
        else:
            print("dlr = " + str(dlr))
            if gameBoard[dlr] == turn:
                numConnected +=1
                print("DLR Match: " +str(numConnected))
            else:
                break
    if numConnected >= 4:
        printGameBoard(gameBoard)
        print("Player "+ turn+" wins!")
        break
    
    printGameBoard(gameBoard)
