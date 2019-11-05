class MyArray:
    def __init__(self, capacity: int):
        self._data = []
        self._capacity = capacity

    def __len__(self) -> int:
        return len(self._data)

    def __getItem__(self, position: int) -> object:
        return self._data[position]

    def __setItem__(self, index: int, value: object):
        self._data[index] = value

    def __iter__(self):
        for item in self._data:
            yield item

    def find(self, index: int) -> object:
        try:
            return self._data[index]
        except IndexError:
            return None

    def delete(self, index: input) -> bool:
        try:
            self._data.pop(index)
            return True
        except IndexError:
            return False

    def insert(self, index: int, value: int) -> bool:
        if len(self) >= self._capacity:
            return False
        else:
            return self._data.insert(index, value)

    def print_all(self):
        for i, val in enumerate(self):
            print(str(i) + ": " + str(val))



def test_myarray():
    myArray = MyArray(6)
    myArray.insert(0, 4)
    myArray.insert(0, 5)
    myArray.insert(2, 2)
    myArray.insert(4, 1)
    print("len:" + str(len(myArray)))
    myArray.print_all()
    print(myArray.find(3))
    print(myArray.delete(2))
    myArray.print_all()


if __name__ == "__main__":
    test_myarray()
