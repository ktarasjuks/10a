class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def Year(cls, name, year):
        return cls(name, 2022 - year)


if __name__ == '__main__':
    bruno = Dog('Bruno', 1)
    print(bruno.name)
    print(bruno.age)

    rex = Dog.Year('Rex', 2020)
    print(rex.name)
    print(rex.age)