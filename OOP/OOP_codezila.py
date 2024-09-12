from datetime import date


# class Student:
#     no_of_studends = 0

#     # initialize func(constractor)
#     def __init__(self, name, age=0, courses="none") -> None:
#         # __name >> privet
#         self.__name = name
#         self.__age = age
#         self.__courses = courses
#         Student.no_of_studends += 1

#     # example of encapsulation (setters & getters func.)

#     # def get_name(self):
#     #     return self.__name

#     # def set_name(self, new_name):
#     #     self.__name = new_name

#     def describe(self):
#         print(
#             f"my name is {self.__name} and my age is {self.__age}, study {self.__courses}"
#         )

#     # def is_old(self, num):
#     #     if self.__age >= num:
#     #         print("student is old")
#     #     else:
#     #         print("studen in normal age")

#     # instance methods (object methods)

#     # student_1 = Student("Mostafa", 25, ["Js", "py"])
#     # student_2 = Student("Eslam", 30)
#     # student_1.describe()

#     # student_1.is_old(40)
#     # student_2.is_old(20)
#     # # print(student_1.age, student_2.age)
#     # # print(Student.no_of_studends)
#     # print(student_1.get_name())
#     # student_2.set_name("Abdo")
#     # print(student_2.get_name())

#     # # student_2.name = "Ali"
#     # print(student_2.name)
#     # print(student_2.get_name())

#     # Class Methods start with Decorator @classmethod
#     # self in instance method >>> cls in class methods


# #     @classmethod
# #     def initFromBirthYear(cls, name, birthYear):
# #         return cls(name, date.today().year - birthYear)


# # student_3 = Student.initFromBirthYear("Ahmed", 1992)
# # student_3.describe()


# # static methods >> don't know any thing in class (@staticmethod)
# class Math:

#     # @staticmethod
#     # def add(x, y):
#     #     return x + y

#     # @staticmethod
#     # def add5(num):
#     #     return num + 5

#     # @staticmethod
#     # def add10(num):
#     #     return num + 10

#     @staticmethod
#     def PI():
#         return 3.14


# class Pizza:
#     def __init__(self, radius, ingradients) -> None:
#         self.radius = radius
#         self.ingradients = ingradients

#     #     @classmethod
#     #     def Veg(cls):
#     #         return cls(["mashrooms", "oloves", "onions"])

#     #     @classmethod
#     #     def Margherit(cls):
#     #         return cls(["mozarella", "oloves", "sauce"])

#     #     # dunder func. >> __func__

#     def __str__(self) -> str:
#         return f"pizza ingradients are {self.ingradients}"

#     def area(self):
#         return Pizza.circle_area(self.radius)

#     @staticmethod
#     def circle_area(r):
#         return r**2 * Math.PI()


# # pizza_1 = Pizza(["tomatoes", "oloves"])
# # pizza_2 = Pizza.Margherit()
# # pizza_3 = Pizza.Veg()

# # print(pizza_2)
# # print(pizza_1)
# # print(pizza_3)


# # x = Math.add(5, 30)
# # y = Math.add5(20)
# # z = Math.add10(90)
# # print(x, y, z)

# p = Pizza(6, ["tomatoes", "oloves"])
# print(p.area())
# print(Pizza.circle_area(4))


# # ## Inhertance
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def display(self):
#         return f"my name is {self.name} and my age is {self.age}"

#     @classmethod
#     def initFromBirthYear(cls, name, birthYear, extra):
#         return cls(name, date.today().year - birthYear, extra)


# class Man(Person):
#     gender = "Male"
#     no_of_men = 0

#     def __init__(self, name, age, voice):
#         super().__init__(name, age)
#         self.voice = voice
#         Man.no_of_men += 1

#     def display(self):
#         s = super().display()
#         return s + f" and my voice is {self.voice} and my gender is {self.gender}"


# man_1 = Man("Bolbol", 66, "hard")
# print(man_1.display())
# print(Man.no_of_men)

# man_1 = Man("MO", 30, "soft")
# print(man_1.display())
# print(Man.no_of_men)


# class Woman(Person):
#     gender = "Female"
#     no_of_women = 0

#     def __init__(self, name, age, hair):
#         super().__init__(name, age)
#         self.hair = hair
#         Woman.no_of_women += 1

#     def display(self):
#         w = super().display()
#         return w + f" and my hair color is {self.hair} and my gender is {self.gender}"


# woman_1 = Woman("Aya", 20, "Yello")
# print(woman_1.display())

# print(Man.no_of_men)

# man_3 = Man.initFromBirthYear("Ali", 2000, "high")
# print(man_3.display())
# print(Man.no_of_men)

# woman_2 = Man.initFromBirthYear("May", 1998, "Black")
# print(woman_2.display())
# print(Man.no_of_men)

# print(isinstance(man_1, Man))
# print(isinstance(man_1, Woman))
# print(isinstance(man_1, Person))

# >>> Abstraction <<<<<
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.__side = side

    def area(self):
        return self.__side * self.__side

    def perimeter(self):
        return self.__side * 4


class Rect(Shape):
    def __init__(self, lenght, width):
        self.__lenght = lenght
        self.__width = width

    def area(self):
        return self.__lenght * self.__width

    def perimeter(self):
        return (self.__lenght + self.__width) * 2


square = Square(10)
print(f"Square area is {square.area()} and perimeter is {square.perimeter()}")
rect = Rect(10, 3)
print(f"Rectangle area is {rect.area()} and perimeter is {rect.perimeter()}")

print(dir(Shape))
