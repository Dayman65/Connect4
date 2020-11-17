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
        
printGameBoard(gameBoard)
        

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
    for r in range(1, rows+1, 1):
        print("R =" + str(r))
        space = "R"+str(r)+"C"+str(intColumn)
        print(space)
        if gameBoard[space] ==" ":
            gameBoard[space] = turn
            printGameBoard(gameBoard)
            break

    numConnected = 0
    #Check for 4 in a row horizontal
    for c in range(intColumn, columns+1, 1):
        if gameBoard.get("R"+str(r)+"C"+str(c)) == turn:
            numConnected += 1
        else:
            break
    for cr in range(intColumn-1,0,-1):
        if gameBoard.get("R"+str(r)+"C"+str(cr)) == turn:
            numConnected += 1
        else:
            break

    if numConnected >= 4:
        printGameBoard(gameBoard)
        print("Player "+ turn+" wins horizontally!")
        break
        
    numConnected =0
    #Check for 4 in a row vertical
    for vr in range(r, 0, -1):
        if gameBoard.get("R"+str(vr)+"C"+str(intColumn)) == turn:    
            numConnected += 1
        else:
            break
    if numConnected >= 4:
        printGameBoard(gameBoard)
        print("Player "+ turn+" wins vertically!")
        break

        
    numConnected =0
    dc = intColumn
    #Check for 4 in a row diagonally bottom left to top right
    for dr in range(r,rows+1,1):
        print("in DR  dc ="+str(dc) + " dr ="+str(dr))
        if gameBoard.get("R"+str(dr)+"C"+str(dc)) == turn:
            numConnected += 1
            dc+=1
        else:
            break
    dc = intColumn -1
    for dr in range(r-1,0,-1):
        print("in DR  dc ="+str(dc) + " dr ="+str(dr))
        if gameBoard.get("R"+str(dr)+"C"+str(dc)) == turn:
            numConnected += 1
            dc-=1
        else:
            break

            
    if numConnected >= 4:
        printGameBoard(gameBoard)
        print("Player "+ turn+" wins diagonally!")
        break

    numConnected =0
    dc = intColumn
    #Check for 4 in a row diagonally top left to bottom right
    for dr in range(r,0,-1):
        print("in DR  dc ="+str(dc) + " dr ="+str(dr))
        if gameBoard.get("R"+str(dr)+"C"+str(dc)) == turn:
            numConnected += 1
            dc+=1
        else:
            break
    dc = intColumn -1
    for dr in range(r+1,rows+1,1):
        print("in DR  dc ="+str(dc) + " dr ="+str(dr))
        if gameBoard.get("R"+str(dr)+"C"+str(dc)) == turn:
            numConnected += 1
            dc-=1
        else:
            break
    if numConnected >= 4:
        printGameBoard(gameBoard)
        print("Player "+ turn+" wins diagonally!")
        break

