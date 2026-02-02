from typing import Optional
from krypto_lib.utils import mod_inverse

class EllipticCurve:
    """Represents an Elliptic Curve over a finite field GF(p).
    Equation: y^2 = x^3 + ax + b (mod p)
    """
    def __init__(self, a: int, b: int, p: int):
        self.a = a
        self.b = b
        self.p = p

    def __eq__(self, other):
        if not isinstance(other, EllipticCurve):
            return False
        return self.a == other.a and self.b == other.b and self.p == other.p

class Point:
    """Represents a Point on an Elliptic Curve."""
    def __init__(self, curve: EllipticCurve, x: Optional[int] = None, y: Optional[int] = None):
        self.curve = curve
        self.x = x
        self.y = y
        # If x or y is None, it represents the Point at Infinity (Identity element)
        self.is_infinity = x is None or y is None

    def __str__(self):
        if self.is_infinity:
            return "Infinity"
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        if not isinstance(other, Point):
            return False
        return self.curve == other.curve and self.x == other.x and self.y == other.y

    def __add__(self, other: 'Point') -> 'Point':
        """Adds two points on the elliptic curve."""
        if self.curve != other.curve:
            raise ValueError("Points must be on the same curve")

        # 1. Handling point at infinity
        if self.is_infinity:
            return other
        if other.is_infinity:
            return self

        assert self.x is not None and self.y is not None
        assert other.x is not None and other.y is not None

        # 2. Handling P + (-P) = Infinity
        if self.x == other.x and (self.y + other.y) % self.curve.p == 0:
            return Point(self.curve)

        # 3. Calculate slope (lambda)
        p = self.curve.p
        if self == other:
            # Point doubling
            num = (3 * self.x**2 + self.curve.a) % p
            den = mod_inverse(2 * self.y, p)
        else:
            # Point addition
            num = (other.y - self.y) % p
            den = mod_inverse(other.x - self.x, p)

        lmbda = (num * den) % p

        # 4. Calculate new coordinates
        x3 = (lmbda**2 - self.x - other.x) % p
        y3 = (lmbda * (self.x - x3) - self.y) % p

        return Point(self.curve, x3, y3)

    def __mul__(self, scalar: int) -> 'Point':
        """Scalar multiplication: scalar * Point (using Double-and-Add)."""
        result = Point(self.curve) # Infinity
        addend = self

        while scalar > 0:
            if scalar & 1:
                result = result + addend
            addend = addend + addend
            scalar >>= 1

        return result

    def __neg__(self) -> 'Point':
        """Returns the additive inverse of the point."""
        if self.is_infinity:
            return self
        return Point(self.curve, self.x, (-self.y) % self.curve.p)

    def __sub__(self, other: 'Point') -> 'Point':
        """Subtracts two points on the elliptic curve."""
        return self + (-other)
