class Employee:
    def __init__(self):
        self.__name = ""
        self.__age = 0
        self.__salary = 0.0

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    def set_salary(self, salary):
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary


# Membuat objek Employee
employee = Employee()

# Mengatur nilai atribut menggunakan metode set
employee.set_name("John Doe")
employee.set_age(30)
employee.set_salary(50000)

# Mendapatkan nilai atribut menggunakan metode get
print("Employee Name:", employee.get_name())
print("Employee Age:", employee.get_age())
print("Employee Salary:", employee.get_salary())