#
# #
# # #Q1
# # class person:
# #     def __init__(self, name, age, address):
# #         self.name = name
# #         self.age = age
# #         self.address = address
# #     def introduction(self):
# #         print (f"HI i  {self.name},{self.age} years old")
# #
# #     def change_address(self, new_address):
# #         self.address = new_address
# #
# # p = person("ali",18,"Tehran" )
# # p.introduction()
# #
#
# #Q.6
# class student:
#     def __init__(self, name,grade):
#         self.name = name
#         self.grade = []
#     def add_grade(self,*args):
#         for arg in args:
#             self.grade.append(arg)
#         print(self.grade)
#     def average(self):
#         result =  sum(self.grade)/len(self.grade)
#         print(result)
#
# students = student("alice",25)
# students.add_grade(18, 14, 13, 18 )
#
# students.average()
from abc import ABC, abstractmethod
class shape (ABC): #
    @abstractmethod
    def area (self):
        pass
class rectangel(shape):
    pass
    def __init__(self, x:int, y:int):
        self.x = x
        self.y = y
    def area(self):
        return self.redius **2*3.14

rectangel = rectangel(10,20)


def circle(param):
    pass


circle = circle(8)

pass
shape =rectangel

from tkinter import Tk
