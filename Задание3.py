import random

class Flower:
    def __init__(self, stem_length, freshness):
        self.stem_length = stem_length
        self.freshness = freshness

    @property
    def stem_length(self):
        return self._stem_length

    @stem_length.setter
    def stem_length(self, value):
        if not isinstance(value, int):
            raise ValueError('Длина стебля должна быть целым числом')
        elif value < 5 or value > 20:
            raise ValueError('Длина стебля должна быть в диапазоне от 5 до 20')
        else:
            self._stem_length = value

    @property
    def freshness(self):
        return self._freshness

    @freshness.setter
    def freshness(self, value):
        if not isinstance(value, int):
            raise ValueError('Уровень свежести должен быть целым числом')
        elif value < 1 or value > 10:
            raise ValueError('Уровень свежести должен быть в диапазоне от 1 до 10')
        else:
            self._freshness = value

f = []
for _ in range(5):
    f.append(Flower(random.randint(5, 20), random.randint(1, 10)))

start_range = int(input('Введите начальное значение диапазона: '))
end_range = int(input('Введите конечное значение диапазона: '))

result = sorted(f, key=lambda x: x.freshness)
for flower in result:
    if start_range <= flower.stem_length <= end_range:
        print(f'Цветок: длина стебля - {flower.stem_length}, уровень свежести - {flower.freshness}')
