def printGameBoard(gameBoard):
    print("|"+gameBoard[43]+"|"+gameBoard[44]+"|"+gameBoard[45]+"|"+gameBoard[46]+"|"+gameBoard[47]+"|"+gameBoard[48]+"|"+gameBoard[49]+"|")
    print("|"+gameBoard[36]+"|"+gameBoard[37]+"|"+gameBoard[38]+"|"+gameBoard[39]+"|"+gameBoard[40]+"|"+gameBoard[41]+"|"+gameBoard[42]+"|")
    print("|"+gameBoard[29]+"|"+gameBoard[30]+"|"+gameBoard[31]+"|"+gameBoard[32]+"|"+gameBoard[33]+"|"+gameBoard[34]+"|"+gameBoard[35]+"|")
    print("|"+gameBoard[22]+"|"+gameBoard[23]+"|"+gameBoard[24]+"|"+gameBoard[25]+"|"+gameBoard[26]+"|"+gameBoard[27]+"|"+gameBoard[28]+"|")
    print("|"+gameBoard[15]+"|"+gameBoard[16]+"|"+gameBoard[17]+"|"+gameBoard[18]+"|"+gameBoard[19]+"|"+gameBoard[20]+"|"+gameBoard[21]+"|")
    print("|"+gameBoard[8]+"|"+gameBoard[9]+"|"+gameBoard[10]+"|"+gameBoard[11]+"|"+gameBoard[12]+"|"+gameBoard[13]+"|"+gameBoard[14]+"|")
    print("|"+gameBoard[1]+"|"+gameBoard[2]+"|"+gameBoard[3]+"|"+gameBoard[4]+"|"+gameBoard[5]+"|"+gameBoard[6]+"|"+gameBoard[7]+"|")


    
gameBoard = {1: " ", 2: " ", 3: " ", 4: " ", 5: " ", 6: " ", 7: " ",
             8: " ", 9: " ", 10: " ", 11: " ", 12: " ", 13: " ", 14: " ",
             15: " ", 16: " ", 17: " ", 18: " ",19: " ", 20: " ", 21: " ",
             22: " ", 23: " ", 24: " ", 25: " ", 26: " ", 27: " ", 28: " ",
             29: " ", 30: " ", 31: " ", 32: " ", 33: " ", 34: " ", 35: " ",
             36: " ", 37: " ", 38: " ", 39: " ", 40: " ", 41: " ", 42: " ",
             43: " ", 44: " ", 45: " ", 46: " ", 47: " ", 48: " ", 49: " "}
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
