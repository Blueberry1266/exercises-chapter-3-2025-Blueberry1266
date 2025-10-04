from numbers import Number
from numbers import Integral


class Polynomial:

    def __init__(self, coefs):
        self.coefficients = coefs


    def degree(self):
        return len(self.coefficients) - 1


    def __str__(self):
        coefs = self.coefficients
        terms = []
        if coefs[0]:
            terms.append(str(coefs[0]))
        if self.degree() and coefs[1]:
            terms.append(f"{'' if coefs[1] == 1 else coefs[1]}x")
        terms += [f"{'' if c == 1 else c}x^{d}" for d, c in enumerate(coefs[2:], start=2) if c]

        return " + ".join(reversed(terms)) or "0"


    def __repr__(self):
        return self.__class__.__name__ + "(" + repr(self.coefficients) + ")"


    def __eq__(self, other):
        return isinstance(other, Polynomial) and\
             self.coefficients == other.coefficients


    def __add__(self, other):
        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a + b for a, b in zip(self.coefficients, other.coefficients))
            coefs += self.coefficients[common:] + other.coefficients[common:]
            return Polynomial(coefs)
        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] + other,)
                              + self.coefficients[1:])
        else:
            return NotImplemented


    def __radd__(self, other):
        return self + other
    

    def __sub__(self,other):
        if isinstance(other, Polynomial):
            common = min(self.degree(), other.degree()) + 1
            coefs = tuple(a - b for a, b in zip(self.coefficients, other.coefficients))
            if self.degree() >= other.degree():
                coefs += self.coefficients[common:]
            else:
                rest = other.coefficients[common:]
                temp = tuple(-x  for x in rest)
                coefs = coefs + temp
            return Polynomial(coefs)
        elif isinstance(other, Number):
            return Polynomial((self.coefficients[0] - other,) + self.coefficients[1:])
        else:
            return NotImplemented
        

    def __rsub__(self,other):    
        if isinstance(other, Number):
            return Polynomial((other - self.coefficients[0],) + tuple(-x for x in self.coefficients[1:]))
        # 这里self.coefficients[0],的逗号是为了使他成为一个tuple
        else:
            return NotImplemented
    

    def __mul__(self,other):
        if isinstance(other,Polynomial):
            coefs = ()
            result_coef_length = other.degree() + self.degree() + 1 #7
            for index in range(result_coef_length):
                coefs_value = 0
                for index_self in range(min(len(self.coefficients),index + 1)):
                    if index - index_self < len(other.coefficients):
                        coefs_value += self.coefficients[index_self] * other.coefficients[index - index_self]
                coefs += (coefs_value,)
            return Polynomial(coefs)

        elif isinstance(other,Number):
            return Polynomial(tuple(other * x for x in self.coefficients))
        else:
            return NotImplemented


    def __rmul__(self,other):
        return self.__mul__(other)
    

    def __rmul__(self,other):
        return self.__mul__(other)
    
    
    def __pow__(self,other):
        if isinstance(other,Integral) and other > 0:
            result = self
            for i in range(other - 1):
                result = result.__mul__(self)
            return Polynomial(result)
        else:
            return NotImplemented
        
    
    def __call__(self,other):
        if isinstance(other,Integral):
            result = 0
            for i in range(len(self.coefficients)):
                result += self.coefficients[i] * other ** i
            return Polynomial(result)
        else:
            return NotImplemented
        
    
    def dx(self):
        coefs = ()
        if len(self.coefficients) == 1:
            return Polynomial((0,))
        else:
            for i in range(1,len(self.coefficients)):
                coefs += (i * self.coefficients[i],)
            return Polynomial(coefs)
    

def derivative(func):
    if isinstance(func,Polynomial):
        return func.dx()
    else:
        return NotImplemented