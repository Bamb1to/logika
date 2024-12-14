from PIL import Image, ImageFilter, ImageEnhance

class ImageEditor():
    def __init__(self):
        self.image = None
        self.origina = None
        self.save_path = 'edited/'

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

            

        

editor = ImageEditor() 
editor.open('erik-mclean-3Z3NGXT1Vy4-unsplash.jpg')  
# editor.do_black_white()  
# editor.do_blur()
# editor.rotate_90()
editor.sharpen()
editor.image.save('result.png')