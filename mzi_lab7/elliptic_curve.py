def inv(n, q):
    """ Calcutating modular inverse of n by mod q """

    for i in range(q):
        if (n * i) % q == 1:
            return i

class EllipticCurve:
    """ Elliptic curve class """

    def __init__(self, a, b, p):
        """ EllipticCurve initialization, params: a, b, p """

        self.a = a
        self.b = b
        self.p = p

    def point_at(self, x):
        ysq = (x ** 3 + self.a * x + self.b) % self.p
        for i in range(1, self.p):
            if pow(i, 2, self.p) == ysq:
                return EllipticCurvePoint(self, x, i)


class EllipticCurvePoint:
    """ Elliptic curve's point class """

    def __init__(self, curve, x, y):
        """ EllipticCurvePoint initialization, params: curve, x, y"""

        self.curve = curve
        self.x = x
        self.y = y

    def __neg__(self):
        """ Neg(-) operation for curve point """

        return EllipticCurvePoint(self.curve, self.x, -self.y % self.curve.p)

    def __add__(self, other):
        """ Add(+) operation for curve point """

        if (self.x, self.y) == (0, 0):
            return other
        if (other.x, other.y) == (0, 0):
            return EllipticCurvePoint(self.curve, self.x, self.y)
        if self.x == other.x and (self.y != other.y or self.y == 0):
            return EllipticCurvePoint(self.curve, 0, 0)
        if self.x == other.x:
            l = (3 * self.x ** 2 + self.curve.a) * inv(2 * self.y, self.curve.p) % self.curve.p
        else:
            l = (other.y - self.y) * inv(other.x - self.x, self.curve.p) % self.curve.p

        x = (l * l - self.x - other.x) % self.curve.p
        y = (l * (self.x - x) - self.y) % self.curve.p

        return EllipticCurvePoint(self.curve, x, y)

    def __mul__(self, number):
        """ Mul(*) operation for curve point """

        result = EllipticCurvePoint(self.curve, 0, 0)
        temp = EllipticCurvePoint(self.curve, self.x, self.y)

        while 0 < number:
            if number & 1 == 1:
                result += temp
            number, temp = number >> 1, temp + temp
        return result

    def __eq__(self, other):
        """ Eq(==) operation for curve point """

        return (self.curve, self.x, self.y) == (other.curve, other.x, other.y)

    def __str__(self):
        """ str() operation for curve point """
        
        return '\n x: {}, y: {}'.format(self.x, self.y)