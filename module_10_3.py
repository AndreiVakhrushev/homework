import threading
from time import sleep
from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for i in range(100):
            replenishment_deposit = randint(50, 500)
            with self.lock:
                if self.balance <= 500 and self.lock.locked():
                    self.balance += replenishment_deposit
                    print(f'Пополнение: {replenishment_deposit}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for i in range(100):
            take_money = randint(50, 500)
            print(f'Запрос на {take_money}')
            with self.lock:
                if take_money <= self.balance:
                    self.balance -= take_money
                    print(f'Снятие: {take_money}. Баланс: {self.balance}')
                else:
                    print(f'Запрос отклонен, недостаточно средств')
            sleep(0.001)


bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
