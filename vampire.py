class Vampire:

    coven = []

    def __init__(self, name, age, in_coffin, drank_blood_today):
        self.name = name
        self.age = age
        self.in_coffin = in_coffin
        self.drank_blood_today = drank_blood_today
# create, which creates a new vampire and adds it to the coven
    @classmethod
    def create(cls, name, age, in_coffin, drank_blood_today):
        new_vampire = Vampire(name, age, in_coffin, drank_blood_today)
        cls.coven.append(new_vampire)
        return new_vampire

# drink_blood, which sets a vampire's drank_blood_today boolean to true
    def drink_blood(self):
        self.drank_blood_today = True

# sunrise, which removes from the coven any vampires who are out of their
# coffins or who haven't drank any blood in the last day
    @classmethod
    def sunrise(cls):
        for num in range(0, len(Vampire.coven)):
            this_vamp = Vampire.coven[num]
            if not this_vamp.drank_blood_today or not this_vamp.in_coffin:
                Vampire.coven.remove(this_vamp)
# sunset, which sets drank_blood_today and in_coffin to false for the entire
# coven as they go out in search of blood
    @classmethod
    def sunset(cls):
        for num in range(0, len(Vampire.coven)):
            this_vamp = Vampire.coven[num]
            this_vamp.in_coffin = False
            this_vamp.drank_blood_today = False

# go_home, which sets a vampire's in_coffin boolean to true
    def go_home(self):
        self.in_coffin = True


bill = Vampire.create("Bill", '400', True, True)
dracula = Vampire.create("Dracula", '1000', True, True)
print(Vampire.coven)
Vampire.sunset()
print(Vampire.coven)
Vampire.sunrise()
print(Vampire.coven)
