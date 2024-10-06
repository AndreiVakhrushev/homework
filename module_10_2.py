
from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100

    def run(self):
        print(f"{self.name}, на нас напали!")
        i = 0
        while self.enemy > 0:
            i += 1
            self.enemy = self.enemy - self.power
            print(f"{self.name}, сражается {i}, осталось {self.enemy} воинов.")
            sleep(1)
            if self.enemy == 0:
                print(f"{self.name} одержал победу спустя {i} дней(дня)!")


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print("Все битвы закончились!")
