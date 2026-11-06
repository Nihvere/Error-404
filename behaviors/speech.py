class SpeechBehavior:
    def speak(self, name, text):
        print(f"{name}: {text}")
    def shout(self, name, text):
        print(f"{name.upper()}: {text.upper()}")
    def whisper(self, name, text):
        print(f"{name.lower()}: {text.lower()}")