from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QLineEdit, QHBoxLayout

from random import shuffle, choice

app = QApplication([])

from window import *

class Question:
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
        for answer in [btn1, btn2, btn3, btn4]:
            if answer.isChecked():
                if answer.text() == self.right_answer:
                    result_text.setText("Правильно")
                    break
                else:
                    result_text.setTExt("Неправильно")
                    break


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

next_question()
answer_btn.clicked.connect(switch_screen)

window.show()
app.exec_()