class moyarigna:
    def __init__(self, data):
        self.data = data

    def __iter__(self):
        yield from self.data

fumoidk = moyarigna([1, 2, 3, 4])
for i in fumoidk:
    print(i)