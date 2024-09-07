from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout
from PyQt5.QtGui import QIntValidator

from random import randint

app = QApplication([])

window = QWidget()
window.setWindowTitle("Генератор переможця")
window.resize(500, 400)

text = QLabel("Переможець:")
winner = QLabel("?")
btn = QPushButton("Натисни, щоб обрати переможця")

start = QLineEdit()
start.setPlaceholderText("Початок")
start.setValidator(QIntValidator())
end = QLineEdit()
end.setPlaceholderText("Кінець")
row = QHBoxLayout()
row.addWidget(start)
row.addWidget(end)
end.setValidator(QIntValidator())


line1 = QVBoxLayout()
line1.addLayout(row)
line1.addWidget(text, alignment=Qt.AlignCenter )
line1.addWidget(winner, alignment=Qt.AlignCenter)
line1.addWidget(btn , alignment=Qt.AlignCenter)


window.setLayout(line1)

def show_winner():
    try:  
        a = int(start.text())
        b = int(end.text())
        number = randint(a,b)

    except:
        number = randint(0, 100)
    winner.setText(str(number))

btn.clicked.connect(show_winner)




window.show()
app.exec_()

