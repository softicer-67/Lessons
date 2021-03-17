class Road:
    def __init__(self, _length, _width, _weight, _height):
        self._length = _length
        self._width = _width
        self._weight = _weight
        self._height = _height

    def mass(self):
        return self._length * self._width * self._weight * self._height


r = Road(20, 5000, 25, 5)
print(r.mass() / 1000)