from entities.dog import Dog
from entities.cat import Cat

class SpeechBehavior:
    def __init__(self):
        self.cat = Cat()
        self.dog = Dog()

    def speak(self):
        self.dog.speak()
        self.cat.speak()

cat = Cat()
dog = Dog()

dog.speak()
