class Jar:

    def __init__(self, capacity=12):
            self.capacity = capacity
            self.size = 0

    def __str__(self):
        return "🍪"*self.size


    def deposit(self, n):
        self.size = self.size+n

    def withdraw(self, n):
        self.size = self.size-n

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        if capacity < 1:
            raise ValueError
        else:
            self._capacity = capacity

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, size):
        if self.capacity < size or size < 0:
            raise ValueError
        self._size = size


if __name__=="__main__":
    cap = input("Jar Capacity: ")
    jar = Jar(int(cap))
    jar.capacity=40

    while True:
        cmd = input ("Command (add, withdraw, show): ")
        n = int(input ("Number: "))
        if cmd == "+":
            jar.deposit(n)
        elif cmd == "-":
            jar.withdraw(n)
        elif cmd == "show":
            print(jar.size)
            print(jar.capacity)
            break
        print(jar.size)
        print(jar)


