class Rational:

    """
    Represensts a rational number (fraction)
    """

    def __init__(this, num, den):
        this.__numerator = num
        if den != 0:
            this.__denominator = den
        else:
            raise ValueError("Where did you see when denominator was 0")

    def get_numerator(this):
        """Returns the numerator of the fraction. """
        return this.__numerator

    def get_denominator(this):
        """ Returns the denominator of the fraction """
        return this.__denominator

    def set_numerator(this, n):
        this.__numerator = n

    def set_denominator(this,d):

        """
        Sets the denominator of the fraction tod,
        unless d is zero. If d is zero, the method
        terminates the program with an error message.
        """

        if d != 0:
            this.__denominator = d
        else:
            raise ValueError('Error: zero denominator!')

    def __mul__(this,other):

        """ Returns the product of this rational number object with
            the other rational object.
        """
        return Rational(this.__numerator * other.__numerator,
                        this.__denominator * other.__denominator)

    def __add__(this, other):

        """ Returns the sum of this rational number object with
            the other rational object.
        """
        pass
    def __str__(this):
        """
        Make a string representation of a Rational object
        """
        return str(this.get_numerator()) + '/' + str(this.get_denominator())

# Client code that uses Rational objects
def main():
    fract1 = Rational(1, 2)
    fract2 = Rational(2, 3)
    print("fract1 =", fract1)
    print("fract2 =", fract2)
    fract1.set_numerator(3)
    fract1.set_denominator(4)
    fract2.set_numerator(1)
    fract2.set_denominator(10)
    print("fract1 =", fract1)
    print("fract2 =", fract2)
    fract3 = Rational(1, 2)
    fract4 = Rational(3, 5)
    print(fract3, "*", fract4, "=", fract3 * fract4)
main()
