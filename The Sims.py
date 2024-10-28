import random


class Human:
    def __init__(self,name="Human", job=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.satiety = 50
        self.job = job
        self.home = home
        self.car = car

        def get_job(self):
            pass

        def get_home(self):
            pass

        def get_car(self):
            pass

        def eat(self):
            pass

        def work(self):
            pass

        def shopping(self, manage):
            pass

        def chill(self):
            pass

        def clean_home(self):
            pass

        def to_repair(self):
            pass


        def days_indexes(self, day):
            pass

        def is_alive(self):
            pass

        def live(self, day):
            pass

class Auto:
    def __init__(self, brand_list):
        self.brand = random.choice(list(brand_list))
        self.fuel = brand_list[self.brand]["fuel"]
        self.strenght = brand_list[self.brand]["strenght"]
        self.consumption = brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strenght > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            return True
        else:
            print("Car cannot move")
            return False



brands_of_cars = {
    'BMW' : {'fuel': 100, 'strenght': 100, 'consuption': 6},
    'PORSHE' : {'fuel': 2000, 'strenght': 120, 'consuption': 20},
    'AUDI' : {'fuel': 80, 'strenght': 120, 'consuption': 8},
}

first_car = Auto(brands_of_cars)