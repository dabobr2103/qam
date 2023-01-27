
class Human():
    energy = 100
    def __init__(self, name, surname, gender = '') -> None:
        self.name = name
        self.surname = surname
        self.gender = gender
    def __repr__(self) -> str:
        return f'{self.name}, {self.surname}, {self.gender};'


    def eat(self):
        self.energy += 5

    def sleep(self):
        self.energy += 10

    def talk(self):
        self.energy -= 5

    def walk(self):
        self.energy -= 10

    def do_homework(self):
        self.energy -= 90

Jim = Human('Jim','Moriarty','male')
John = Human('John','Watson','male')
Sherlock = Human('Sherlock','Holmes','male')
Mary = Human('Mary','Morstan','female')
Molly = Human('Molly','Hooper','female')

Jim.walk()
Jim.talk()

John.eat()
John.do_homework()
John.sleep()

Sherlock.talk()
Sherlock.do_homework()

Mary.talk()
Mary.eat()
Mary.walk()

Molly.do_homework()
Molly.sleep()
Molly.walk()

Humans = [Jim, John, Sherlock, Mary, Molly]
max_energy = 0
max_Human = None
for Human in Humans:
    if Human.energy > max_energy:
        max_energy = Human.energy
        max_Human = Human
print(max_Human.name)