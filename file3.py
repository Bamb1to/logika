class Animal():
    def __init__(self, name,voice):
        self.name = name
        self.voice = voice
    
    def make_voice(self):
        print("Тварина каже", self.voice)



class Cat(Animal):
    def _init_(self, name, voice, hp=9): 
        super()._init__(name, voice)
        self.hp = hp

    def sleep_all_day(self):   
        print('Кіт спить весь день')




tom = Animal('Tom', 'мяу')
tom.make_voise()
tom.name = "Jerry"














