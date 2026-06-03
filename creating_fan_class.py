# name of a class
class Fan:
    # class constants
    SLOW = 1
    MEDIUM = 2
    FAST = 3

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
        if speed in [Fan.SLOW, Fan.MEDIUM, Fan.FAST]:
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

    def __str__(self):
        # Lines of info
        lines = [
            f"speed={self.__speed}",
            f"on={self.__on}",
            f"radius={self.__radius}",
            f"color={self.__color}"
        ]
        # Find the longest line length
        width = max(len(line) for line in lines)
        # Top border
        box = "\n+" + "-" * (width + 2) + "+\n"
        # Content lines centered inside the box
        for line in lines:
            box += "| " + line.ljust(width) + " |\n"
        # Bottom border
        box += "+" + "-" * (width + 2) + "+"
        return box

# Test program
def test_fan():
    # First Fan Object
    fan1 = Fan()
    fan1.set_speed(Fan.FAST)
    fan1.set_radius(10)
    fan1.set_color("yellow")
    fan1.set_on(True)

    print("Fan 1: ", fan1)

test_fan()