from behaviors.speech import SpeechBehavior
from entities.dog import Dog
from entities.cat import Cat

if __name__ == "__main__":
    print("--- Запуск из main.py ---")
    dog = Dog()
    cat = Cat()
    dog.speak()
    cat.speak()
