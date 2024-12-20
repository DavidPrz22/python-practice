class Glass:
    def __init__(self, toughness):
        self.toughness = toughness

    def brand(self):
        print("Prada")


class Jar(Glass):
    uwu = 0
    jars = []

    def __init__(self, capacity:int = 12, toughness=12):
        super().__init__(toughness)
        self.capacity = capacity
        self.size = 0 

        Jar.jars.append(self)

    def __str__(self):
        return "🍪" * self.capacity
    
    def deposite(self, size):
        if self.capacity >= size:
            self.size = size
            self.capacity = self.capacity - size
        else:
            return f"Can not deposite in jar, {self.capacity}"

    def withdraw(self, amount):
        if self.size >= amount:
            self.size -= amount
            self.capacity += amount
            return "🍪" * amount
        else:
            return f"Cant draw that much cookies :c"


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size

    @capacity.setter
    def capacity(self, n):
        try:
            if not isinstance(n, int):
                raise ValueError("Only Ints")
            if n < 0:
                raise ValueError("No negative numbers")
            
            self._capacity = n
        except ValueError as error:
            print(error)

    @size.setter
    def size(self, n):
        self._size = n

    @staticmethod
    def random():
        print('...')



cookie_jar = Jar(10, 20)
print(cookie_jar.uwu)


