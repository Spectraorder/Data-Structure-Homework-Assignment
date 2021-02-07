class Fraction:
    def __init__(self, numerator = 0, denominator = 1):
        self.numerator = numerator
        if denominator != 0:  
            self.denominator = denominator
        else:
            raise ZeroDivisionError()

    def __add__(self, other):
        # If either the "self" or the "other" Fraction object is negative in mathematical means,
        # signSelf and signOther are the new Fraction objects that could change the negative sign to numerator if the denominator is negative
        signSelfNume, signSelfDeno = signChanger(self.numerator, self.denominator)
        signOtherNume, signOtherDeno = signChanger(other.numerator, other.denominator)
        signSelf = Fraction(signSelfNume, signSelfDeno)
        signOther = Fraction(signOtherNume, signOtherDeno)

        outNume = signSelf.numerator * signOther.denominator + signSelf.denominator * signOther.numerator
        outDeno = signSelf.denominator * signOther.denominator
        outFrac = Fraction(outNume, outDeno)
        return outFrac

    def __iadd__(self, other):
        signSelfNume, signSelfDeno = signChanger(self.numerator, self.denominator)
        signOtherNume, signOtherDeno = signChanger(other.numerator, other.denominator)
        signSelf = Fraction(signSelfNume, signSelfDeno)
        signOther = Fraction(signOtherNume, signOtherDeno)
        outNume = signSelf.numerator * signOther.denominator + signSelf.denominator * signOther.numerator
        outDeno = signSelf.denominator * signOther.denominator
        self.numerator = outNume
        self.denominator = outDeno
        return self

    def __sub__(self, other):
        signSelfNume, signSelfDeno = signChanger(self.numerator, self.denominator)
        signOtherNume, signOtherDeno = signChanger(other.numerator, other.denominator)
        signSelf = Fraction(signSelfNume, signSelfDeno)
        signOther = Fraction(signOtherNume, signOtherDeno)
        outNume = signSelf.numerator * signOther.denominator - signSelf.denominator * signOther.numerator
        outDeno = signSelf.denominator * signOther.denominator
        outFrac = Fraction(outNume, outDeno)
        return outFrac

    def __mul__(self, other):
        signSelfNume, signSelfDeno = signChanger(self.numerator, self.denominator)
        signOtherNume, signOtherDeno = signChanger(other.numerator, other.denominator)
        signSelf = Fraction(signSelfNume, signSelfDeno)
        signOther = Fraction(signOtherNume, signOtherDeno)
        outNume = signSelf.numerator * signOther.numerator
        outDeno = signSelf.denominator * signOther.denominator
        signOutNume, signOutDeno = signChanger(outNume, outDeno)
        outFrac = Fraction(signOutNume, signOutDeno)
        return outFrac

    def __eq__(self, other):
        signSelfNume, signSelfDeno = signChanger(self.numerator, self.denominator)
        signOtherNume, signOtherDeno = signChanger(other.numerator, other.denominator)
        outSelfNume, outSelfDeno = simplify(signSelfNume, signSelfDeno)
        outOtherNume, outOtherDeno = simplify(signOtherNume, signOtherDeno)
        if((outSelfNume==outOtherNume)&(outSelfDeno==outOtherDeno)):
            return True
        else:
            return False

    def reduce(self):
        self.numerator, self.denominator = simplify(self.numerator, self.denominator)

    def __str__(self):
        return str(self.numerator) + ' / ' + str(self.denominator)

def simplify(num1, num2):
    if((num1<0)&(num2<0)):
        num1 *= -1
        num2 *= -1
    if(num1<=num2):
        i = 2
        if(num1>0):
            while(i<=num1):
                if((num1%i==0)&(num2%i==0)):
                    num1 //= i
                    num2 //= i
                i += 1
        elif(num1<0):
            while(i<=(num1 * -1)):
                if((num1%i==0)&(num2%i==0)):
                    num1 //= i
                    num2 //= i
                i += 1
    else:
        k = 2
        while(k<=num2):
            if((num1%k==0)&(num2%k==0)):
                num1 //= k
                num2 //= k
            k += 1
    return num1, num2

# It changes the sign of the numerator and denominator if denominator is negative only
def signChanger(num, den):
    if((den<0)&(num>0)):
        den *= -1
        num *= -1
    return num, den

'''
Note: 
To get autograded on gradescope, you program can't print anything.

Thus, please comment out the main function call, if you are submitting for auto grading.

'''

def main():
    x = Fraction(3, 4)
    y = Fraction(4, 6)
    print(x)        # 3 / 4
    print(y)        # 4 / 6
    print(x + y)    # 34 / 24 or any value that is equal
    z = x + y
    print(x * y)    # 12 / 24 or any value that is equal
    print(x - y)    # 2 / 24 or any value that is equal
    y.reduce()
    print(y)        # 2 / 3
    z.reduce()
    print(z)        # 17 / 12

    print(z == Fraction(-17, -12))  # True
    print(z == Fraction(51, 36))  # True
    print(z == Fraction(-7, 4))   # False
    
if __name__ == '__main__':
    main()
