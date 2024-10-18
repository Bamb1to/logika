from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit,QRadioButton, QHBoxLayout, QButtonGroup, QSpinBox, QGroupBox



window = QWidget()# створення вікна
window.setWindowTitle("Memory Card")# назва вікна
window.resize(500, 500)# ЗМІНИТИ РОЗМІР ВІКНА
window.move(200,200)# ПОЛОЖЕННЯ ВІКНА

window.setStyleSheet('''
background: #7a302b;
font-size: 25px;
color: white;                                          
''')

menu_btn = QPushButton("Статистика")

btn_style = '''
background: #7a302b;
font-size: 25px;
color: white;
border: 2px solid #D52A73;
padding: 10px;
border-radius: 20px;
'''
menu_btn.setStyleSheet(btn_style)

rest_btn = QPushButton("Відпочити")
rest_btn.setStyleSheet(btn_style)
time_box = QSpinBox()
time_label = QLabel("Хвилин")

row1 = QHBoxLayout()
row1.addWidget(menu_btn)
row1.addStretch(1)
row1.addWidget(rest_btn)
row1.addWidget(time_box)
row1.addWidget(time_label)

# Напис з запитанням
question_text = QLabel("mouse")

btn1 = QRadioButton("ьірка")
btn2 = QRadioButton("щур")
btn3= QRadioButton("мішок")
btn4 = QRadioButton("миша")

radio_group = QButtonGroup()
radio_group.addButton(btn1)
radio_group.addButton(btn2)
radio_group.addButton(btn3)
radio_group.addButton(btn4)

group_box = QGroupBox("Bаріанти перекладу")
box_style = '''
background: #7a302b;
font-size: 15px;
color: white;
border: 2px solid #D52A73;
padding: 10px;
border-radius: 20px;
'''
group_box.setStyleSheet(box_style)

col1 = QVBoxLayout()
col2 = QVBoxLayout()
row2 = QHBoxLayout()

col1.addWidget(btn1)
col1.addWidget (btn2)

col2.addWidget (btn3)
col2.addWidget (btn4)

row2.addLayout(col1)
row2.addLayout(col2)

group_box.setLayout(row2)

result_box = QGroupBox("Результат")
result_text = QLabel("Правильно")#Результат: Правильно/Неправильно
answer_text = QLabel("Миша")# Правильна відповідь

result_col = QVBoxLayout()
result_col.addWidget(result_text)
result_col.addWidget(result_text, alignment=Qt.AlignCenter, stretch=2)

result_box.setLayout(result_col)
result_box.hide()

answer_btn = QPushButton("Відповісти")
answer_btn.setStyleSheet(btn_style)

# Додаємо всі віджети на головну напрямну лінію
main_line = QVBoxLayout()
main_line.addLayout(row1, stretch=1)
main_line.addWidget(question_text, alignment=Qt.AlignCenter, stretch=2)
main_line.addWidget(result_box, stretch=5)
main_line.addWidget(group_box, stretch=5)
main_line.addWidget(answer_btn, stretch=3)

window.setLayout(main_line)