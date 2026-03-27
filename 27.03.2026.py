# class User:
#     def __init__(self, first_name, last_name,age):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.__age = age
#
#     def get_age(self):
#         return self.__age
#
#     def set_age(self, value):
#         if value < 0:
#             return ValueError("Yosh manfiy bo'lmasligi lozim!")
#         self.__age = value
#
# Bobur = User("Bobur","Jovliyev",15)
#
# print(Bobur.get_age())
# Bobur.set_age(25)
# print(Bobur.get_age())