import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
window = QWidget()
window.setWindowIcon(QIcon('TicTacToe//python.png'))
window.setWindowTitle("TicTacToe")
window.setToolTip('TicTacToe')

window.resize(700, 700)
window.move(100, 100)
# window.setGeometry(300, 300, 400, 400)
pixmap = QPixmap('TicTacToe//border.png')
play_btn=[[QPushButton(window) for i in range(3) ] for r in range(3)]
rdx=1
wid=100
hgh=100
sp=20



def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  
            (board[4] == mark and board[5] == mark and board[6] == mark) or  
            (board[1] == mark and board[2] == mark and board[3] == mark) or  
            (board[7] == mark and board[4] == mark and board[1] == mark) or  
            (board[8] == mark and board[5] == mark and board[2] == mark) or  
            (board[9] == mark and board[6] == mark and board[3] == mark) or  
            (board[7] == mark and board[5] == mark and board[3] == mark) or  
            (board[9] == mark and board[5] == mark and board[1] == mark))


test_board = ['#',None,None,None,None,None,None,None,None,None]

result = QMessageBox.question(window, 'Welcome to Tic Tac Toe!', "Player1 select yes to use X, No to use O?", QMessageBox.Yes|QMessageBox.No)

if result==QMessageBox.Yes:
    print("yes")
    p1="x"
    p2="o"

else:
    print('No')
    p1="o"
    p2="x"


player_mark=p1
print(player_mark)


def on_button(n,nn):
    print('Button {} clicked {}'.format(n,nn))
    global player_mark
    print("playermark", player_mark)
    mark=player_mark
    
    idx=n.text( )
    print("idx",idx)
    test_board[int(idx)]=mark
    btn.setIcon(QIcon('TicTacToe//python.png'))
    
    btn.setEnabled(False)
    if win_check(test_board,mark ):
        if mark ==p1:
            print("player1 win")
        else:
            print ("player2 win")

    if player_mark=="x":
        player_mark="o"
    else:
        player_mark="x"

i=0
for r in play_btn:
    print(r)
    for btn in r:
        btn.resize(100,100)
        btn.move(sp+wid,sp+hgh)
        wid+=100+sp
        btn.setText(str(i))
        i+=1
        btn.setIcon(QIcon(pixmap))
        #btn.clicked.connect(toggleBtnPic)
        #btn.clicked.connect(lambda btn=btn,i=i : on_button(btn,i))
    wid=100
    hgh+=100+sp
    print(rdx)
    rdx+=1

mapping = [(play_btn[0][0], 1),
           (play_btn[0][1], 2),
           (play_btn[0][2], 3),
           (play_btn[1][0], 4),
           (play_btn[1][1], 5),
           (play_btn[1][2], 6),
           (play_btn[2][0], 7),
           (play_btn[2][1], 8),
           (play_btn[2][2], 9)]

for button, n in mapping:
    button.clicked.connect(lambda  state, n=n: on_button(button,n))

window.show()
app.exec_()
