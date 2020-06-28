class Fraction:
    def __init__(self, num, den):
        self.num = num
        self.den = den

    def __str__(self):
        if self.den != 1:
            return str(self.num) + "/" + str(self.den)
        return str(self.num)

    def __add__(self, otherfrac):
        newnum = (self.num * otherfrac.den) + (otherfrac.num *  self.den)
        newden = self.den * otherfrac.den
        gcd = self.gcd(newnum, newden)
        return Fraction(newnum//gcd, newden//gcd)

    def __sub__(self, otherfrac):
        newnum = (self.num * otherfrac.den) - (otherfrac.num * self.den)
        newden = self.den * otherfrac.den
        gcd = self.gcd(newnum, newden)
        return Fraction(newnum//gcd, newden//gcd)

    def __eq__(self, otherfrac):
        num1 = self.num * otherfrac.den
        num2 = otherfrac.num * self.den
        return num1 == num2

    def __mul__(self, otherfrac):
        newnum = self.num * otherfrac.num
        newden = self.den * otherfrac.den
        gcd = self.gcd(newnum, newden)
        return Fraction(newnum//gcd, newden//gcd)

    def __truediv__(self, otherfrac):
        newnum = self.num * otherfrac.den
        newden = self.den * otherfrac.num
        gcd = self.gcd(newnum, newden)
        return Fraction(newnum//gcd, newden//gcd)

    # lesser than operator
    def __lt__(self, otherfrac):
        num1 = self.num * otherfrac.den
        num2 = otherfrac.num * self.den
        return num1 < num2

    def __rt__(self, otherfrac):
        num1 = self.num * otherfrac.den
        num2 = otherfrac.num * self.den
        return num1 > num2

    def gcd(self, a, b):
        if a == 0:
            return b
        return self.gcd(b%a, a)


myfac1 = Fraction(1, 5)
myfac2 = Fraction(4, 3)

print(myfac1 > myfac2)
