"""
Create an hierarchy of classes - abstract class Employee and subclasses HourlyEmployee, SalariedEmployee, Manager and Executive. 
Every one's pay is calculated differently, research a bit about it. 
After you've established an employee hierarchy, create a Company class that allows you to manage the employees. 
You should be able to hire, fire and raise employees.
"""

from abc import ABCMeta, abstractmethod

class Employee: 
    __metaclass__ = ABCMeta

    @abstractmethod
    def salary_calculator(self): pass

class HourlyEmployee: 
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

class SalariedEmployee: 
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

class Manager: 
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

class Executive: 
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2

class Company: 
    def __init__(self, param1, param2):
        self.param1 = param1
        self.param2 = param2