class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5

    def get_speed(self):
        return self.__speed

def test_car():
    car_type = Car("2026", "BMW")

    print("Accelerating........")
    for i in range(5):
        car_type.accelerate()
        print(f"After car accelerated {i+1}, Speed = {car_type.get_speed()}")

    for i in range(2):
        print("----------------------------------")

    print("Braking........")
    for i in range(5):
        car_type.brake()
        print(f"After car brake {i+1}, Speed = {car_type.get_speed()}")

test_car()