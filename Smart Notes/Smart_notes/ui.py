# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Smart_notes.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(630, 534)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(70, 0))
        self.centralwidget.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.left_col_3 = QtWidgets.QVBoxLayout()
        self.left_col_3.setObjectName("left_col_3")
        self.new_note = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("C:/Users/user/Downloads/circle-plus.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.new_note.setIcon(icon)
        self.new_note.setObjectName("new_note")
        self.left_col_3.addWidget(self.new_note)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(70, 0))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("C:/Users/user/Downloads/search (1).svg"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.pushButton.setIcon(icon1)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.search_line = QtWidgets.QLineEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_line.sizePolicy().hasHeightForWidth())
        self.search_line.setSizePolicy(sizePolicy)
        self.search_line.setObjectName("search_line")
        self.horizontalLayout_2.addWidget(self.search_line)
        self.left_col_3.addLayout(self.horizontalLayout_2)
        self.notes_list = QtWidgets.QListWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notes_list.sizePolicy().hasHeightForWidth())
        self.notes_list.setSizePolicy(sizePolicy)
        self.notes_list.setObjectName("notes_list")
        self.left_col_3.addWidget(self.notes_list)
        self.horizontalLayout_3.addLayout(self.left_col_3)
        self.right_col_2 = QtWidgets.QVBoxLayout()
        self.right_col_2.setObjectName("right_col_2")
        self.note_title = QtWidgets.QLineEdit(self.centralwidget)
        self.note_title.setObjectName("note_title")
        self.right_col_2.addWidget(self.note_title)
        self.note_text = QtWidgets.QTextEdit(self.centralwidget)
        self.note_text.setObjectName("note_text")
        self.right_col_2.addWidget(self.note_text)
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("C:/Users/user/Downloads/device-floppy.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.save_btn.setIcon(icon2)
        self.save_btn.setObjectName("save_btn")
        self.right_col_2.addWidget(self.save_btn)
        self.delete_btn = QtWidgets.QPushButton(self.centralwidget)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("C:/Users/user/Downloads/circle-minus.svg"), QtGui.QIcon.Disabled, QtGui.QIcon.On)
        self.delete_btn.setIcon(icon3)
        self.delete_btn.setObjectName("delete_btn")
        self.right_col_2.addWidget(self.delete_btn)
        self.horizontalLayout_3.addLayout(self.right_col_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 630, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.new_note.setText(_translate("MainWindow", "Нова замітка"))
        self.pushButton.setText(_translate("MainWindow", "Шукати"))
        self.search_line.setPlaceholderText(_translate("MainWindow", "Пошук замітки"))
        self.note_title.setPlaceholderText(_translate("MainWindow", "Назва замітки"))
        self.note_text.setPlaceholderText(_translate("MainWindow", "Текст замітки"))
        self.save_btn.setText(_translate("MainWindow", "Зберегти"))
        self.delete_btn.setText(_translate("MainWindow", "Видалити"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
