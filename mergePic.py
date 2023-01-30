from PIL import Image
from uploader.JSON import JSON
import os
import json
CANVAS_SIZE=(374,481)
INIT_POS=(28,135)
GRID_SIZE=(40,40)
BOARD_SIZE=8
MINE_NUM=10
UPLOAD_NUMBER=1000
def open_number(url):
    num=Image.open(url).resize(GRID_SIZE)
    return num
def paste_on_board(board,pic,i,j):
    add=((j%8)*GRID_SIZE[0],(i%8)*GRID_SIZE[1])
    board.paste(pic,(INIT_POS[0]+add[0],INIT_POS[1]+add[1]))
def pick_pic(val):
    if val=='💣':
        return Image.open('numbers/flag.png').resize(GRID_SIZE)
    else:
        return Image.open('numbers/'+str(val)+'.png').resize(GRID_SIZE)

if __name__ == '__main__':
    HISTORY=JSON(os.getcwd() + "/uploader/history.json").readFromFile()
    data = JSON(os.getcwd() + "/uploader/data/metadata.json").readFromFile()
    for k in range(HISTORY['mergePic']+1,HISTORY['mergePic']+UPLOAD_NUMBER+1):
        distr=data[str(k)]['board']
        board=Image.open('pass.png')
        for i in range(8):
            for j in range(8):
                paste_on_board(board,pick_pic(distr[i][j]),i,j)
        board.save('finish/'+str(k)+'.png','PNG')
        with open('uploader/history.json', 'w', encoding='utf-8') as f:
            new_history=HISTORY
            new_history['mergePic']=k
            json.dump(new_history, f, ensure_ascii=False, indent=4)
        
        