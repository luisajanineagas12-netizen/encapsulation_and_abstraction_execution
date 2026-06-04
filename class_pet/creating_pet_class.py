class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age

def pet():
    name = input("Please enter your pet name: ")
    animal_type = input("Enter your pet animal type: ")
    age = int(input("Please enter your pet age: "))

    pets_information = Pet(name, animal_type, age)

    print(f"\nName of pet: {pets_information.get_name()}")
    print(f"Animal type: {pets_information.get_animal_type()}")
    print(f"Age: {pets_information.get_age()}")

pet()


