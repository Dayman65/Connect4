import pygame
pygame.init()

#Number of rows and columns
rows = 6
columns = 7
gameBoard ={ }
#Create gameBoard based on number of rows and columns
for c in range(1, columns+1, 1):
    for r in range(1, rows+1, 1):
        gameBoard["R"+str(r)+"C"+str(c)] =" "

pygame.display.set_caption("Connect 4")
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
grey = (201,201,201)
black = (0,0,0)

intColumn=0
x = 1400
y = 900
width = 40
height = 60
vel = 5
fullColumn = 0
win = pygame.display.set_mode((x, y))

column1 = pygame.draw.rect(win, black, (0,0,150,1050))
column2 = pygame.draw.rect(win, black, (150,0,150,1050))
column3 = pygame.draw.rect(win, black, (300,0,150,1050))
column4 = pygame.draw.rect(win, black, (450,0,150,1050))
column5 = pygame.draw.rect(win, black, (600,0,150,1050))
column6 = pygame.draw.rect(win, black, (750,0,150,1050))
column7 = pygame.draw.rect(win, black, (900,0,150,1050))
win.fill(grey)
pygame.draw.line(win,black, (0,150), (1050,150), 1)
pygame.draw.line(win,black, (0,300), (1050,300), 1)
pygame.draw.line(win,black, (0,450), (1050,450), 1)
pygame.draw.line(win,black, (0,600), (1050,600), 1)
pygame.draw.line(win,black, (0,750), (1050,750), 1)
pygame.draw.line(win,black, (150,0), (150,900), 1)
pygame.draw.line(win,black, (300,0), (300,900), 1)
pygame.draw.line(win,black, (450,0), (450,900), 1)
pygame.draw.line(win,black, (600,0), (600,900), 1)
pygame.draw.line(win,black, (750,0), (750,900), 1)
pygame.draw.line(win,black, (900,0), (900,900), 1)
pygame.draw.line(win,black, (1050,0), (1050,900), 1)
for row in range(7):
    pygame.draw.circle(win, white, (75+(150*row),75), 70)
    pygame.draw.circle(win, white, (75+(150*row),225), 70)
    pygame.draw.circle(win, white, (75+(150*row),375), 70)
    pygame.draw.circle(win, white, (75+(150*row),525), 70)
    pygame.draw.circle(win, white, (75+(150*row),675), 70)
    pygame.draw.circle(win, white, (75+(150*row),825), 70)
    
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Choose Another Column', True, green, blue)
textRect = text.get_rect()  
textRect.center = (x // 2, y // 2)

pygame.display.update()
i = 0
run = True
while run:
    event = pygame.event.wait()

    if event.type == pygame.QUIT:
        run = False
        pygame.quit()

    if event.type == pygame.MOUSEBUTTONDOWN:
        if i%2 == 0:
            turn ="1"
        else:
            turn ="2"



        while True:
            pos = pygame.mouse.get_pos()
            pressed1, pressed2, pressed3 = pygame.mouse.get_pressed()
            if column1.collidepoint(pos) and pressed1:
                intColumn = 1
            if column2.collidepoint(pos) and pressed1:
                intColumn = 2
            if column3.collidepoint(pos) and pressed1:
                intColumn = 3
            if column4.collidepoint(pos) and pressed1:
                intColumn = 4
            if column5.collidepoint(pos) and pressed1:
                intColumn = 5
            if column6.collidepoint(pos) and pressed1:
                intColumn = 6
            if column7.collidepoint(pos) and pressed1:
                intColumn = 7
            if gameBoard.get("R"+str(rows)+"C"+str(intColumn))==" ":
                break
            else:
                pygame.event.wait()

            
        for r in range(1, rows+1, 1):
            print("R =" + str(r))
            space = "R"+str(r)+"C"+str(intColumn)
            print(space)
            if gameBoard.get(space) ==" ":
                gameBoard[space] = turn
                if turn == "1":
                    pygame.draw.circle(win, (255,0,0),(-75+(150*intColumn),975-(150*r)),70)
                else:
                    pygame.draw.circle(win, (5,5,5),(-75+(150*intColumn),975-(150*r)),70)
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
            print("Player "+ turn+" wins horizontally!")
            run=False
            
        numConnected =0
        #Check for 4 in a row vertical
        for vr in range(r, 0, -1):
            if gameBoard.get("R"+str(vr)+"C"+str(intColumn)) == turn:    
                numConnected += 1
            else:
                break
        if numConnected >= 4:
            print("Player "+ turn+" wins vertically!")
            run=False

            
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
            print("Player "+ turn+" wins diagonally!")
            run =False

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
            print("Player "+ turn+" wins diagonally!")
            run = False
            
        #.circle for a circle
        
        pygame.display.update()
        i += 1
   
