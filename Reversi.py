import pygame
from math import sqrt
import random
from time import sleep
import time
def text_disp(inp_text,coords,color,font):#display text in pygame
    text = font.render(inp_text,1,color)
    display.blit(text,coords)
    pygame.display.update()



class struc:
	def __init__(self):
		self.corner=0
		self.no_of_moves=0
		self.no_of_coins_of_enemy=0
		self.no_of_coins_of_ally=0
		self.heuristic_value=0
		self.reference_no=0
		self.children=[]
		self.move=[0,0] 
def tree(move1):		
	obj=struc()
	
	if (turn_counter%2==1):		
		obj.no_of_moves=some_legal_move(board,turn_counter)
	countw=0
	countb=0
	countref=1
	obj.reference_no=1
	obj.move=move1
	object=[]
	ptr=struc()
	children=all_legal_moves(board,turn_counter)
	for i in range (0,5):
		for j in range (0,5):
			
			if(children[i][j]==1):
				countref+=1
				board1=board
				findflips(board1,i,j,turn_counter+1)
				for i1 in range (0,5):
					for j1 in range (0,5):
						if(board1[i1][j1]==1):
							countw+=1
						elif(board1[i1][j1]==-1):
							countb+=1
				ptr.move = [i1,j1]
				if((i==0 and j==0) or(i==5 and j==5) or (i==0 and j==5) or (i==5 and j==0)):
					ptr.corner=1
				ptr.no_of_coins_of_ally=countw
				ptr.no_of_coins_of_enemy=countb
				ptr.no_of_moves=some_legal_move(board1,turn_counter+1)
				ptr.heuristic_value=(ptr.corner*100)-(ptr.no_of_moves*5)+(ptr.no_of_coins_of_ally*2)-(ptr.no_of_coins_of_enemy*2)
				ptr.reference_no=countref
				obj.children.append(countref)
				object.append(ptr)
	max=object[0].heuristic_value
	mv_to_be_played=object[0].move
	for i in range (1,countref-1):
            if(object[i].heuristic_value>max):
                max=object[i].heuristic_value
                mv_to_be_played=object[i].move
	findflips(board,mv_to_be_played[0],mv_to_be_played[1],turn_counter)
	





def flip(board,playedrow,  playedcol,  opp_row, opp_col):
	if(playedrow==opp_row):
	
		if(playedcol<opp_col):
			startcol=playedcol
			endcol=opp_col
		else:
			startcol=opp_col
			endcol=playedcol
		i = startcol+1
		while(i<endcol):
			board[playedrow][i] = (-1)*board[playedrow][i];
			i+=1

	elif (playedcol==opp_col):
		if(playedrow<opp_row):
			startrow=playedrow
			endrow=opp_row
		else:
			startrow=opp_row
			endrow=playedrow
		i = startrow+1

		while(i<endrow):
			board[i][playedcol] = (-1)*board[i][playedcol]
			i+=1


	elif ( (playedrow + playedcol) == (opp_row + opp_col)):
		j = playedrow + playedcol
		if(playedrow<opp_row):
			startrow=playedrow
			endrow=opp_row
		else:
			startrow=opp_row
			endrow=playedrow
		i = startrow+1
		while(i<endrow):
			board[i][j-i] = (-1)*board[i][j-i]
			i+=1
	elif ( playedrow-playedcol == opp_row-opp_col ):
		j= playedrow-playedcol
		if(playedrow<opp_row):
			startrow=playedrow
			endrow=opp_row
		else:
			startrow=opp_row
			endrow=playedrow
		i = startrow+1
		while(i<endrow):
			board[i][i-j] = (-1)*board[i][i-j]		
			i+=1	
	else:
		return


def findflips( board, playedrow, playedcol, turncounter):
	found = 0
	if(turncounter%2 == 1):
		ally = (-1)
		enemy = 1
	else:
		ally = 1
		enemy = (-1)
	i = playedrow
	j = playedcol
	while( ((i+1)<5) and(board[i+1][j] == enemy)):
		i+=1
		if(board[i+1][j]==ally):
			opp_row =i+1
			opp_col = j
			found = 1
			break
	if(found):
		flip(board, playedrow, playedcol, opp_row, opp_col)
	found = 0
	i = playedrow
	j = playedcol
	while(((j+1)<5) and (board[i][j+1] == enemy)):
		j+=1
		if(board[i][j+1]==ally):
			opp_row = i
			opp_col = j+1
			found = 1
			break
	if(found):
		flip(board, playedrow, playedcol, opp_row, opp_col)
	found = 0
	i = playedrow
	j = playedcol
	while( ((i-1)>0) and(board[i-1][j] == enemy) ):
		i-=1
		if(board[i-1][j]==ally):
			opp_row =i-1
			opp_col = j
			found = 1
			break
	if(found):
		flip(board, playedrow, playedcol, opp_row, opp_col)
	found = 0
	i = playedrow
	j = playedcol
	while( ((j-1)>0) and(board[i][j-1] == enemy)):
		j-=1
		if(board[i][j-1]==ally):
			opp_row =i
			opp_col = j-1
			found = 1
			break
	if(found):
		flip(board, playedrow, playedcol, opp_row, opp_col)
	found = 0
	i = playedrow
	j = playedcol
	while( ((j+1)<5) and((i+1)<5) and (board[i+1][j+1] == enemy)):
		j+=1
		i+=1
		if(board[i+1][j+1]==ally):
			opp_row =i+1
			opp_col = j+1
			found = 1
			break
	if(found):
		flip(board, playedrow, playedcol, opp_row, opp_col);
	found = 0
	i = playedrow
	j = playedcol
	while(((j-1)>0)and((i-1)>0) and(board[i-1][j-1] == enemy)):
		j-=1
		i-=1
		if(board[i-1][j-1]==ally):
			opp_row =i-1
			opp_col = j-1
			found = 1
			break
	if(found):
		flip(board, playedrow, playedcol, opp_row, opp_col)
	found = 0
	i = playedrow
	j = playedcol
	while(((j+1)<5)and((i-1)>0) and(board[i-1][j+1] == enemy)):
		j+=1
		i-=1
		if(board[i-1][j+1]==ally):
			opp_row =i-1
			opp_col = j+1
			found = 1
			break
	if(found):
		flip(board, playedrow, playedcol, opp_row, opp_col)
	found = 0
	i = playedrow
	j = playedcol
	while( ((j-1)>0)and((i+1)<5) and(board[i+1][j-1] == enemy)):
		j-=1
		i+=1
		if(board[i+1][j-1]==ally):
			opp_row =i+1
			opp_col = j-1
			found = 1
			break
	if(found):
		flip(board, playedrow, playedcol, opp_row, opp_col)
	found = 0
	i = playedrow
	j = playedcol
	board[i][j] = ally




def legal_move(board,  i,  j,  turn_counter):

    if turn_counter%2==1:
        enemy,ally=1,-1
    else:
        enemy,ally=-1,1

    i1 = i-1
    i2 = i+1
    j1 = j-1
    j2 = j+1

    if((i>1) and (board[i][j]==0)):
        if (board[i1][j]== enemy):
            while(i1>=0):
                if(board[i1][j] == ally):
                    return True
                elif(board[i1][j]== 0):
                    break
                i1-=1



    if((i<4) and (board[i][j]==0)):
        if (board[i2][j]== enemy):
            while(i2<6):

                if(board[i2][j] == ally):
                    return True
                elif(board[i2][j]== 0):
                    break
                i2+=1

    i1 = i-1
    i2 = i+1
    j1 = j-1
    j2 = j+1

    if((j>1) and (board[i][j]==0)):
        if (board[i][j1]== enemy):
            while(j1>=0):
                if(board[i][j1] == ally):
                    print("good")
                    return True
                elif(board[i][j1]== 0):
                    break
                j1-=1

    i1 = i-1
    i2 = i+1
    j1 = j-1
    j2 = j+1

    if((j<4) and(board[i][j]==0)):
        if (board[i][j2]== enemy):
            while(j2<6):

                
                if(board[i][j2] == ally):
                    return True
                elif(board[i][j2]== 0):
                    break
                j2+=1

    i1 = i-1
    i2 = i+1
    j1 = j-1
    j2 = j+1




    if((i<4)and(j<4) and(board[i][j]==0)):
        if (board[i2][j2]== enemy):
            while((j2<6)and(i2<6)):

                if(board[i2][j2]==ally):
                    return True
                elif(board[i2][j2]==0):
                    break
                i2+=1  
                j2+=1


    if((i>1) and (j>1) and (board[i][j]==0)):
    
        if (board[i1][j1]== enemy):
        
            while((j1>=0)and(i1>=0)):
            

                if(board[i1][j1]==ally):
                    return True
                elif(board[i1][j1]==0):
                    break

                i1-=1
                j1-=1

    i1 = i-1
    i2 = i+1
    j1 = j-1
    j2 = j+1




    
    if((i>1) and(j<4) and (board[i][j]==0)):
        if (board[i1][j2]== enemy):
            while((j2<6)and(i1>=0)):
            

                if(board[i1][j2]==ally):
                    return True
                elif(board[i1][j2]==0):
                    break
                i1-=1
                j2+=1


    if((i<4) and(j>1) and(board[i][j]==0)):
        if (board[i2][j1]== enemy):
            while((j1>=0)and(i2<6)):
                if(board[i2][j1]==ally):
                    return True
                elif(board[i2][j1]==0):
                    break
                i2+=1
                j1-=1






def accept_user_input(board,turn_counter):
    while True:
        for event in pygame.event.get():#quit
            if event.type ==pygame.QUIT:
                pygame.quit()
                quit()                


            if event.type == pygame.MOUSEBUTTONUP:
    
                x,y = pygame.mouse.get_pos()
                print(x,y)# the attack points
                if x in range(100,340) and y in range(100,340):
                    posx = posy = None
                
                    for i in range(6):
                        if 100+40*(i)<= x and 100+40*(i+1)>=x:
                            posx = i
                            break
                    for j in range(6):
                        if 100+40*(j)<= y and 100+40*(j+1)>=y:
                            posy = j
                            break
                if legal_move(board,posx,posy,turn_counter):
                    board = findflips(board,posx,posy,turn_counter)
                    pygame.display.flip()

                return [posx,posy];
        
def some_legal_move(board,turn_counter):
    count = 0
    for i in range(6):
        for j in range(6):
            if (legal_move(board,i,j,turn_counter)):
                count +=1

    return count

        
def all_legal_moves(board,turn_counter):
    return [[legal_move(board,i,j,turn_counter) for i in range(6)] for j in range(6)]








def initialize(turn_counter):
    while(some_legal_move(board,turn_counter) or some_legal_move(board,turn_counter+1)):
        turn_counter +=1
        if not some_legal_move(board,turn_counter):
            continue
        elif turn_counter %2==1:
            posx,posy = accept_user_input(board,turn_counter)
            disp_board()
        elif turn_counter%2==0:
            tree([posx,posy])
            time.sleep(2)
            disp_board()

    ##check who won here
    

    

def disp_board():
    for i in range(6):#display all coins
        for j in range(6):
            if board[i][j] ==0:
                display.blit(empty_pic,(100+40*i,100+40*j))
            elif board[i][j] ==1:
                display.blit(white_pic,(100+40*i,100+40*j))
            elif board[i][j] ==-1:
                display.blit(black_pic,(100+40*i,100+40*j))
    pygame.display.flip()
    



#basic initialization of
blue = (0,0,255)
red = (255,0,0)
white = (255,255,255)
yellow = (255,255,0)
black = (0,0,0)

display = pygame.display.set_mode((600,600))
pygame.font.init()
font = pygame.font.Font(None,30)
bigfont = pygame.font.Font(None,45)
vict_font= pygame.font.SysFont("ComicSansMs", 60, bold=True, italic=True)
display.fill(yellow)
pygame.display.flip()

empty_filnam = "empty.png"
black_filnam =  "black.jpg"
white_filnam =  "white.jpg"
empty_pic = pygame.image.load(empty_filnam)
black_pic = pygame.image.load(black_filnam)
white_pic = pygame.image.load(white_filnam)

board = [[0 for i in range(6)]for j in range(6)]
board[2][3] = -1
board[3][2] = -1
board[2][2] = 1
board[3][3] = 1
turn_counter = 0
#start screen of the game.
print("hi")
occurences = 0
while occurences < 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONUP:
            occurences += 1
            disp_board()
            initialize(turn_counter)
        if event.type ==pygame.KEYDOWN:
            pressed = pygame.key.get_pressed()
            if pressed[pygame.K_b]:
                occurences +=1




sum =0
for i in range(6):
    for j in range(6):
        sum +=board[i][j]

if(sum >0):
    text_disp("White Won",(10,10),white,vict_font)
elif(sum <0):
    text_disp("Black Won",(10,10),black,vict_font)
else:
    text_disp("Tie",(10,10),blue,vict_font)
sleep(3)
pygame.quit()
quit()
