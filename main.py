from behaviors.speech import SpeechBehavior

from entities.dog import Dog
from entities.cat import Cat
from entities.person import Person
from entities.robot import Robot


speech = SpeechBehavior()

dog = Dog(speech)
cat = Cat(speech)

person = Person(speech, "Привет, меня зовут Алекс!")
robot = Robot(speech, "Я искусственный интеллект!")


dog.speak()
cat.speak()
person.speak()
robot.speak()

print("\n--- Дополнительные возможности ---\n")

speech.shout("Кошка", "Мяу!")
speech.whisper("Робот", "Привет...")