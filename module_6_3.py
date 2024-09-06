
class Horse:
    sound = 'Frrr'

    def __init__(self):
        self.x_distance = 0

    def run(self, dx):
        self.x_distance += dx
        return self.x_distance


class Eagle:
    sound = 'I train, eat, sleep, and repeat'

    def __init__(self):
        self.y_distance = 0

    def fly(self, dy):
        self.y_distance += dy
        return self.y_distance


class Pegasus(Horse, Eagle):
    sound = Eagle.sound

    def __init__(self):
        Horse.__init__(self)
        Eagle.__init__(self)

    def move(self, dx, dy):
        super().run(dx)
        super().fly(dy)

    def get_pos(self):
        pos = (self.x_distance, self.y_distance)
        return pos

    def voice(self):
        print(self.sound)


print(Horse.mro())
print(Eagle.mro())
print(Pegasus.mro())

p1 = Pegasus()

print(p1.get_pos())
p1.move(10, 15)
print(p1.get_pos())
p1.move(-5, 20)
print(p1.get_pos())

p1.voice()
