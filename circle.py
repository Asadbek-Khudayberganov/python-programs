class Circle:
    """ Represensts a geometric circle object """
    def __init__(this, center, radius):
        """ Initialize the cecnter's center and radius """

        # Disallow a negatice radius
        if radius < 0:
            raise ValueEror('Negative radius')
        this.center = center
        this.radius = radius

    def get_radius(this):
        """ Return the radius of the circle """
        return this.radius

    def get_center(this):
        """ Return the coordinatess of the center """
        return this.center

    def get_area(this):
        """Compute and return the area of the circle """
        from math import pi
        return pi*this.radius*this.radius
        """ pi is equal to 3.14 or 22/7"""

    def get_circumference(this):
        """ Compute and return the circumference of the circle """
        from math import pi
        return round(2*pi*this.radius)

    def move(this,pt):
        """ Moves the center of the circle to point py """
        this.center = pt

    def grow(this):
        """ Increase the radius of the circle """
        this.radius +=1

    def shrink(this):
        """Decrease the radius of the circle;
           does not affect a circle with radius zero """
        if this.radius > 0:
            this.radius -= 1

circle = Circle((2.5, 6), 5)
