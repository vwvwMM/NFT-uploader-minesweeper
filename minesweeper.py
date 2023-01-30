from random import randint
import json
import os
from uploader.JSON import JSON

MERGE_NUM=1



def print_board(board,boardSize):
    print("Current board")
    for x in range(boardSize):
        row=''
        for g in board[x]:
            if g !='💣': row+=str(g)+" "
            else :row+=g
        print(row)

def create_boards(boardSize,mineNum,random):
    board=[]
    mineLocations=[]
    if not random:
        mineLocations=[(0,0),(0,1),(0,2),(1,0),(1,2),(2,0),(2,1),(2,2),(4,5),(6,8)]
    # Create a blank board
    for x in range(boardSize):
        subCol = []
        for y in range(boardSize):
            subCol.append(0)
        board.append(subCol)
    # Random bombs locations
    mineCount = 0
    if random:
        while mineCount < mineNum:
            x = randint(0,boardSize-1)
            y = randint(0,boardSize-1)
            if board[x][y] == 0:            # Check this location has not been located a mine.
                board[x][y] = '💣'          # Change the value of the cell to '💣'
                mineLocations.append((x,y))
                mineCount+=1
    else:
        while mineCount<mineNum:
            x=mineLocations[mineCount][0]
            y=mineLocations[mineCount][1]
            if board[x][y]:
                board[x][y] = '💣'          # Change the value of the cell to '💣'
                mineCount+=1
    for r in range(boardSize):
        for c in range(boardSize):
            if board[r][c] == '💣': continue
            # Top
            if r > 0 and board[r - 1][c] == '💣': board[r][c]+=1
            # Top Right
            if r > 0 and c < boardSize - 1 and board[r - 1][c + 1] == '💣': board[r][c]+=1
            # Right
            if c < boardSize - 1 and board[r][c + 1] == '💣': board[r][c]+=1
            # Bottom Right
            if r < boardSize - 1 and c < boardSize - 1 and board[r + 1][c + 1] == '💣': board[r][c]+=1
            # Bottom
            if r < boardSize - 1 and board[r + 1][c] == '💣': board[r][c]+=1
            # Bottom Left
            if r < boardSize -1 and c > 0 and board[r + 1][c - 1] == '💣': board[r][c]+=1
            # Left
            if c > 0 and board[r][c - 1] == '💣': board[r][c]+=1
            # Top Left
            if r > 0 and c > 0 and board[r - 1][c -1] == '💣': board[r][c]+=1
    return board,mineLocations
if __name__ == '__main__':   
    data=JSON(os.getcwd() + "/uploader/data/metadata.json").readFromFile()
    for k in range(len(data),len(data)+MERGE_NUM):
        distr,mines=create_boards(8,10,False)
        sub_data={"description":"Imagine how cool it is to own an unique distribution of minesweeeper! <br /> Go to [minesweeper online](https://minesweeper.online/) to know more about minesweeper","link":"https://minesweeper.online/","board":distr,"mines":mines}
        numbers=[0,0,0,0,0,0,0,0,0]
        for i in range(8):
            for j in range(8):
                val=distr[i][j]
                if val!='💣':
                    numbers[val]+=1
        for i in range(1,len(numbers)):
            if numbers[i]!=0:
                sub_data[str(i)]=numbers[i]
        data[str(101)]=sub_data
    with open('uploader/data/metadata.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)