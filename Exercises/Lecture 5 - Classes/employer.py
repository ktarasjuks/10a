class Employer:
    salary = 30000

    def __init__(self, name, age, tax):
        self.name = name
        self.age = age
        self.tax = tax

    def salary_calculation(self, tax):
        tax_rate = 100 - tax
        self.salary = self.salary * tax_rate / 100

    def check_salary(self):
        self.salary_calculation(self.tax)
        return self.salary


if __name__ == '__main__':
    employe = Employer('SomeName', 25, 10)
    print(employe.name)
    print(employe.age)
    print(employe.tax)
    print(employe.check_salary())
