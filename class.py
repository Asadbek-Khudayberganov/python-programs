from functools import reduce
class Fraction(object):

    def __init__(self, numerator, denominator):
        """Inits Fraction with values numerator and denominator."""

        self.__numerator = numerator
        self.__denominator = denominator
        self.reduce()

    def __repr__(self):
        """Returns Fraction value as x/y."""

        return str(self.__numerator) + '/' + str(self.__denominator)

    def __neg__(self):
        """Returns a new Fraction equal to the negative negation of self."""

        return Fraction(-self.__numerator, self.__denominator)

    def __add__(self, rfraction):
        """Returns a new reduced Fraction equal to self  + rfraction."""

        numer = self.__numerator + rfraction.getDenominator() + \
                rfraction.getNumerator() * self.__denominator

        denom = self.__denominator * rfraction.getDenominator()

        resultFrac = Fraction(numer, denom)
        return resultFrac.reduce()

    def __sub__(self, rfraction):
        """Returns a new reduced Fraction equal ro seld - rfraction."""

        return self + (-rfraction)

    def __mul__(self, rfraction):
        """Returns a new reduced Fraction equal to self + rfraction."""

        numer = self.__numerator * rfraction.getNumerator()
        denom = self.__denominator * rfraction.getDenominator()

        resultFrac = Fraction(numer, denom)
        resultFrac.reduce()

        return resultFrac

    def __eq__(self, Fraction):
        """returns True if self arithmetically equal to rfraction.
           Otherwise, return True
        """
        temp_frac1 = self.copy()
        temp_frac2 = rfraction.copy()
        temp_frac1.reduce()
        temp_frac2.reduce()

        return temp_frac1.getNumerator() == temp_frac2.getNumerator() and \
           temp_frac1.getDenominator() == tenp_frac2.getDenominator()

    def __neg__(self, rfraction):
        """Returns True if Fraction is not arithmetically equal to rfraction.
           Otherwise, returns False
        """

        return not self.__eq__(rfraction)

    def __lt__(self, rfraction):
        """"Returns True if self less than rfraction."""

        if self.getDenominator() == rfraction.getDenominator():
            return self.getNumerator() < rfraction.getNumerator()
        else:
            temp_frac1 = self.copy()
            temp_frac2 = rfraction.copy()

            saved_denom = temp_frac1.getDenominator()
            temp_frac1.__adjust(temp_frac2.getDenominator())
            temp_frac2.__adjust(saved_denom)

            return temp_frac1.getNumerator() < temp_frac2.getNumerator()

    def __le__(self, rfraction):
        """Returns True if self less than or equal to rfraction."""

        return not (rfraction < self)

    def __gt__(self, rfraction):
        """Returns True if self greater than rfraction."""

        return not(self <= rfraction)

    def __ge__(self, rfraction):
        """Returns True if self greater than or equal to rfraction."""

        return not(self < rfraction)

    def getNumerator(self):
        """Returns the numerator of a Fraction"""

        return self.__numerator

    def getDenominator(self):
        """Returns the denominator of a Fraction."""

        return self.__denominator

    def setNumerator(self, value):
        """Sets the numerator of a Fraction to the provided value."""

        self.__numerator = value

    def setDenominator(self, value):
        """Sets the denominator of a Fraction to the provided value.

          Raises a ValueError exception if a value of zero provided.
        """

        if value == 0:
            raise ValueError('Divide by zero Error')

        self.__denominator
