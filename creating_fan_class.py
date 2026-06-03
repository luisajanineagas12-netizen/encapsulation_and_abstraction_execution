# name of a class
class Fan:
    # class constants
    SLOW = 1
    MEDIUM = 2
    HARD = 3

    def __init__(self, speed=SLOW, on=False, radius=5, color="blue"):
        # private member
        self.__speed = speed
        self.__on = on
        self.__radius = radius
        self.__color = color

    # Accessor (Getters)
    def get_speed(self):
        return self.__speed

    def get_on(self):
        return self.__on

    def get_radius(self):
        return self.__radius

    def get_color(self):
        return self.__color

    # Mutators (Setters)
    def set_speed(self, speed):
        if speed in [Fan.SLOW, Fan.MEDIUM, Fan.HARD]:
            self.__speed = speed
        else:
            print("Invalid speed value")

    def set_on(self, on):
        self.__on = on

    def set_radius(self, radius):
        if radius > 0:
            self.__radius = radius
        else:
            print("Radius must be a positive value")

    def set_color(self, color):
        self.__color = color

