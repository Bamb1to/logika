from PIL import Image, ImageFilter, ImageEnhance
from PyQt5 import QtWidgets, uic
import sys

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('untitled.ui', self)

class ImageEditor():
    def __init__(self):
        self.image = None
        self.origina = None
        self.save_path = 'edited/'
        self.ui = Ui()

    def open(self, filename):
        self.image = Image.open(filename)
        self.original = self.image
        # self.image.show() 

    def do_black_white(self):
        self.image = self.image.convert('L')

    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)  

    def rotate_90(self):
        self.image = self.image.transpose(Image.ROTATE_90)

    def sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN) #чіткість   

        
app = QApplication([])
editor = ImageEditor()
apply_stylesheet(app, theme='light_red.xml')

editor = ImageEditor() 
