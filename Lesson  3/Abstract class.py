from abc import ABC, abstractmethod

class ABsclass(ABC):

    def print(self, x):
        print("Passed value is: ", x)
    @abstractmethod
    def task(self):
        print ("we are in abstract class")
class test_class(ABsclass):
    def task(self):
        print("we are inside test_class task")

test__obj = test_class()
test__obj.task()
test__obj.print(100)