class Pet:
    def __init__(self, name, animal_type, age):
        self.__name = name
        self.__animal_type = animal_type
        self.__age = age

    def set_name(self):
        self.__name = self.__name

    def set_animal_type(self):
        self.__animal_type = self.__animal_type

    def set_age(self):
        self.__age = self.__age

    def get_name(self):
        return self.__name

    def get_animal_type(self):
        return self.__animal_type

    def get_age(self):
        return self.__age
    
