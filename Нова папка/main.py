from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout, QMessageBox

from random import shuffle, choice
from time import sleep
app = QApplication([])

from window import *

class Question:
    crorrect_counter = 0
    total_counter = 0

    def __init__(self, text, right_answer, ans1, ans2, ans3):
        self.text = text
        self.right_answer = right_answer
        self.answers = [self.right_answer, ans1, ans2, ans3]
        shuffle(self.answers)

    def show_question(self):
        question_text.setText(self.text)
        shuffle(self.answers)
        btn1.setText(self.answers[0])
        btn2.setText(self.answers[1])
        btn3.setText(self.answers[2])
        btn4.setText(self.answers[3])
        answer_text.setText(self.right_answer)

    def check_answer(self):
        radio_group.setExclusive(False)
        Question.total_counter+=1

        for answer in [btn1, btn2, btn3, btn4]:
            if answer.isChecked():
                answer.setChecked(False)
                if answer.text() == self.right_answer:
                    result_text.setText("Правильно")
                    Question.crorrect_counter+=1
                    break
                else:
                    result_text.setText("Неправильно")
                    break

        radio_group.setExclusive(True)

questions = [
    Question("клавіатура", "keyboard", "keys", "klaviatura", "computer board"),
    Question("миша", "mouse", "mause", "mouce", "mysha"),
    Question("екран", "screen", "ecran", "csreen", "scrin"),
]    

shuffle(questions)
current_question = None

def next_question():
    global current_question

    current_question = choice(questions)
    current_question.show_question()


def switch_screen():
    if answer_btn.text() == 'Відповісти':
        current_question.check_answer()
        group_box.hide()
        result_box.show()
        answer_btn.setText('Наступне питання')
    else:
        next_question()
        result_box.hide()
        group_box.show()
        answer_btn.setText('Відповісти')

def show_stat():
    stat_win = QMessageBox()
    stat_win.setIcon(QMessageBox.Information)    
    stat_win.setWindowTitle("Статистика")   
    try:
        accaracy = Question.crorrect_counter / Question.total_counter * 100
        stat_win.setText(f'Кількість відповідей: {Question.total_counter} \nПравильні відповіді : {Question.crorrect_counter}\nТочність відповідей: {accaracy}')
    except:
        stat_win.setText("Дайте хоча б одну відповідь для підрахунку статистики")
    stat_win.exec()

def rest():
    pause_time = int(time_box.value()) * 60               
    window.hide()
    sleep(pause_time)
    window.show()

next_question()
answer_btn.clicked.connect(switch_screen)
menu_btn.clicked.connect(show_stat)
rest_btn.clicked.connect(rest)

window.show()
app.exec_()          