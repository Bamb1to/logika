from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import secrets
import string
class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.generate)

    def generate(self):
        if self.ui.checkBox.isChecked() and self.ui.checkBox_2.isChecked():
            symbols = string.ascii_letters + string.digits
        elif self.ui.checkBox.isChecked():
            symbols = string.digits
        elif self.ui.checkBox_2.isChecked():
            symbols = string.ascii_letters
        else:
            symbols = string.ascii_letters + string.digits

        
        
        password = ""

        for i in range(10):
            password += secrets.choice(symbols)

        self.ui.label_2.setText(password)

        with open("passwords.txt", "a") as f:
            f.write(password+"\n")

app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
