class Calculator:
    def __init__(self, name):
        self.name = name

    @classmethod
    def alternative_name_create(cls, alternative_name):
        return cls(alternative_name + 'Name')

    def say_my_name(self):
        print('Your name is ' + self.name)

    @staticmethod
    def add( a, b):
        return a + b

    @staticmethod
    def subs( a, b):
        return a - b

    def mult(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


if __name__ == '__main__':
    a = 3
    b = 1
    calc = Calculator('Konstantins')
    calc.say_my_name()
    calc.name = 'Random Name'
    calc.say_my_name()

    var_1 = Calculator.alternative_name_create('Joe Biden')
    var_1.say_my_name()


