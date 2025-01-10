from PIL import Image, ImageFilter, ImageEnhance
from PyQt5 import QtWidgets, uic
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import sys
import os

import tempfile

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem, QFileDialog
from qt_material import apply_stylesheet

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('imageeditor.ui', self)

class ImageEditor():
    def __init__(self):
        self.image = None
        self.original = None
        self.history = []
        self.history_index = -1
        self.image_path = None
        self.workdir = None
        self.temp_folder = tempfile.TemporaryDirectory()
        self.ui = Ui()
        self.connects()
        self.ui.show()

    def open(self, filename):
        self.image = Image.open(filename)
        self.original = self.image.copy()
        self.history = [self.image.copy()]
        self.history_index = 0
        self.image_path = filename

    def connects(self):
        self.ui.folder_btn.clicked.connect(self.open_folder)    
        self.ui.open_folder.triggered.connect(self.open_folder)
        self.ui.image_list.currentRowChanged.connect(self.choose_image)
        self.ui.black_white.triggered.connect(self.do_black_white)
        self.ui.save_btn.clicked.connect(self.save_file)
        self.ui.save.triggered.connect(self.save_file)
        self.ui.open_file.triggered.connect(self.open_file)
        self.ui.del_btn.clicked.connect(self.delete_file)
        self.ui.rotate_left.clicked.connect(self.rotate_90)
        self.ui.rotate_right.clicked.connect(self.rotate_270)
        self.ui.blur.triggered.connect(self.do_blur)
        self.ui.sharpen.triggered.connect(self.sharpen)
        self.ui.back_btn.clicked.connect(self.back)
        self.ui.forward_btn.clicked.connect(self.forward)
        
    def get_images(self):
        self.folder_images = []
        if self.workdir:
            filenames = os.listdir(self.workdir)
            for file in filenames:
                if file.endswith('.png') or file.endswith('.jpg') or file.endswith('.jpeg'):
                    self.folder_images.append(file)

    def open_folder(self):
        self.workdir = QFileDialog.getExistingDirectory()    
        if self.workdir:
            self.get_images()
            self.ui.image_list.clear()
            self.ui.image_list.addItems(self.folder_images)

    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self.ui, 'Зберегти фото', '', 'Зображення (*.png *.jpg *.jpeg)')
        if file_path:
            self.open(file_path)
            self.show_image(file_path)     

    def choose_image(self):
        if self.ui.image_list.currentRow()>=0:
            title = self.ui.image_list.currentItem().text()
            image_path = os.path.join(self.workdir, title)
            self.open(image_path)
            self.show_image(image_path) 

    def show_image(self, image_path):
        self.ui.current_image.hide()
        pixmap = QPixmap(image_path)
        w, h = self.ui.current_image.width(), self.ui.current_image.height()
        pixmap = pixmap.scaled(w, h, Qt.KeepAspectRatio)
        self.ui.current_image.setPixmap(pixmap)
        self.ui.current_image.show() 

    def back(self):
        if self.history_index > 0:
            self. history_index -= 1
            self.image = self.history[self.history_index]
            self.show_image(self.temp_save())

    def forward(self):
        if self.history_index < len(self.history)-1:
            self. history_index += 1
            self.image = self.history[self.history_index]
            self.show_image(self.temp_save())

    def add_history(self):
        self.history.append(self.image.copy())            
        self.history_index += 1      

    def temp_save(self):
        temp_path = os.path.join(self.temp_folder.name, f'temp_image_{self.history_index}.png')
        self.image.save(temp_path)
        return temp_path

    def save_file(self):
        if self.image:
            save_path, _ = QFileDialog.getSaveFileName(self.ui, 'Зберегти фото', '', 'Зображення (*.png *.jpg *.jpeg)')
            if save_path:
                self.image.save(save_path)
                print('Фото збережено')
                if self.workdir:
                    self.get_images()
                    self.ui.image_list.clear()
                    self.ui.image_list.addItems(self.folder_images)

    def delete_file(self):
        if self.image_path:
            check = QMessageBox.question(self.ui, 'Видалення файлу', 'Ви впевнені що хочете видалити фото?', QMessageBox.Yes|QMessageBox.No)
            if check == QMessageBox.Yes:
                os.remove(self.image_path)
                if self.workdir:
                    self.get_images()
                    self.ui.image_list.clear()
                    self.ui.image_list.addItems(self.folder_images)
                
                self.ui.current_image.setPixmap(QPixmap())
                self.image = None
                self.original = None
                self.history = []
                self.history_index = -1
                self.image_path = None
                
    def do_black_white(self):
        if self.image:
            self.image = self.image.convert('L')
            self.add_history()
            self.show_image(self.temp_save())    

    def do_blur(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.BLUR)  
            self.add_history()
            self.show_image(self.temp_save())
            
    def rotate_90(self):
        if self.image:
            self.image = self.image.transpose(Image.ROTATE_90)
            self.add_history()
            self.show_image(self.temp_save())

    def rotate_270(self):
        if self.image:
            self.image = self.image.transpose(Image.ROTATE_270)
            self.add_history()
            self.show_image(self.temp_save())        

    def sharpen(self):
        if self.image:
            self.image = self.image.filter(ImageFilter.SHARPEN) #чіткість   
            self.add_history()
            self.show_image(self.temp_save())

    

        
app = QApplication([])
editor = ImageEditor()
apply_stylesheet(app, theme='light_red.xml')
app.exec()
