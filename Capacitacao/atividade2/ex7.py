from math import gcd

class Racional:
    def __init__(self, p: int, q: int) -> None:
        if q == 0:
            raise ValueError("Denominador não pode ser zero.")
        mdc = gcd(p, q)
        self.p = p // mdc
        self.q = q // mdc

    def __repr__(self) -> float:
        return f"{self.p}/{self.q}"

    def __neg__(self) -> float:
        return Racional(-self.p, self.q)

    def __add__(self, other: int) -> float:
        p = self.p * other.q + other.p * self.q
        q = self.q * other.q
        return Racional(p, q)

    def __sub__(self, other: int) -> float:
        return self + (-other)

    def __mul__(self, other: int) -> float:
        p = self.p * other.p
        q = self.q * other.q
        return Racional(p, q)

    def __truediv__(self, other: int) -> float:
        if other.p == 0:
            raise ValueError("Não é possível dividir por zero.")
        return self * Racional(other.q, other.p)
    

rac = Racional(p=20, q=2)
print(rac)

