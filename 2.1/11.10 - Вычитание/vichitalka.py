class Spysok(list):
    def __init__(self, *args):
        super(Spysok, self).__init__(args)
    def __sub__(self, other):
        return self.__class__(*[item for item in self if item not in other])
x = Spysok(7, 8, 9, 77, 52)
y = Spysok(25, 5, 2, 7, 8)
print(x - y)