class Fractie(object):
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f'Fractie: {self.numarator} / {self.numitor}'

    def __add__(self, other_numarator, other_numitor):
        sum_numarator = (self.numarator * other_numitor) + (other_numarator * self.numitor)
        sum_numitor = self.numitor * other_numitor
        return f'Suma fractiilor {self.numarator} / {self.numitor} + {other_numarator} / {other_numitor} = {sum_numarator} / {sum_numitor} '

    def __sub__(self, other_numarator, other_numitor):
        dif_numarator = (self.numarator * other_numitor) - (other_numarator * self.numitor)
        dif_numitor = self.numitor * other_numitor
        return f'Diferenta fractiilor {self.numarator} / {self.numitor} - {other_numarator} / {other_numitor} = {dif_numarator} / {dif_numitor}'

    def __invert__(self):
        return f'Inversa fractiei {self.numarator} / {self.numitor} este {self.numitor} / {self.numarator}'


f1 = Fractie(5, 2)

print(f1)
print(f1.__add__(7, 2))
print(f1.__sub__(7, 3))
print(f1.__invert__())


