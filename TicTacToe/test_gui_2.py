import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)
window = QWidget()
window.setWindowIcon(QIcon('TicTacToe//python.png'))
window.setWindowTitle("TicTacToe")
window.setToolTip('TicTacToe')

window.resize(400, 400)
window.move(300, 300)
# window.setGeometry(300, 300, 400, 400)

btn = QPushButton('Close',window)
btn.resize(120,40)
btn.move(100,80)
btn.setToolTip('Click to close')
btn.clicked.connect(exit)

result = QMessageBox.question(window, 'Message', "Select yes for player1 use X, No for O?", QMessageBox.Yes|QMessageBox.No)

if result==QMessageBox.Yes:
    print("yes")
else:
    print('No')

lbl=QLabel(window, text='User Name')
lbl.move(120,120)

pixmap = QPixmap('TicTacToe//python.png')
lbl.setPixmap(pixmap)
#lbl.resize(pixmap.width(),pixmap.height())




window.show()
app.exec_()

