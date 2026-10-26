class Pet:

    def __init__(self, name, animal_type, color):
        print(f"{name} is eating happily~")
        self.name = name
        self.animal_type = animal_type
        self.color = color
        self.happy = 50

    def play(self):
        print(f"{self.name} is playing with you and having so much fun!")
        self.happy += 30

    def sleep(self):
        print(f"{self.name} is sleeping soundly zzz")
        if self.happy <= 100:
            self.happy += 10

    def show_status(self):
        print(f"Name: {self.name}\n Type: {self.animal_type}\n Color: {self.color}\n\n Happiness: {self.happy}")


abigail = Pet("Abigail", "Guinea Pig", "White")
abigail.play()
abigail.show_status()
doggy = Pet("Alice", "Betta Fish", "Red")
doggy.sleep()
doggy.show_status()