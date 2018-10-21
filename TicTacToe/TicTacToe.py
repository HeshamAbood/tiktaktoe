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

def toggleBtnPic(event):
    print("button clicked")
    #change the baground image

for r in play_btn:
    print(r)
    for btn in r:
        btn.resize(100,100)
        btn.move(sp+wid,sp+hgh)
        wid+=100+sp
        btn.setIcon(QIcon(pixmap))
        btn.clicked.connect(toggleBtnPic)

    wid=100
    hgh+=100+sp
    print(rdx)
    rdx+=1
    

result = QMessageBox.question(window, 'Welcome to Tic Tac Toe!', "Player1 select yes to use X, No to use O?", QMessageBox.Yes|QMessageBox.No)

if result==QMessageBox.Yes:
    print("yes")
else:
    print('No')


window.show()
app.exec_()




