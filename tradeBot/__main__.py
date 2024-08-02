from .services import binanceConnection
from .services import Student
BC=binanceConnection()
stu1=Student(32,32)
print(BC.system)
print(Student.__module__)

