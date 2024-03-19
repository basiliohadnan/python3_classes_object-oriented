class Employee:
      __slots__ = ("name", "age", "salary")

      def __init__(self, name, age, salary) -> None:
            self.name = name
            self.age = age
            self.salary = salary

      def increase_salary(self, percent):
            self.salary += self.salary * (percent/100)

      def has_slots(self):    
            return hasattr(self, "__slots__")

class SlotInspectorMixing:
      __slots__ = ()
      def has_slots(self):
            return hasattr(self, "__slots__")

class Developer(SlotInspectorMixing, Employee):
      __slots__ = ("framework")

      def __init__(self, name, age, salary, framework) -> None:
            super().__init__(name, age, salary)
            self.framework = framework
            
      def increase_salary(self, percent, bonus = 0):
            super().increase_salary(percent)
            self.salary += bonus

employee1 = Developer("Ji-Soo", 38, 1200, "Ruby")

# print(employee1.has_slots())
# method resolution order
# print(Developer.__mro__)
# only works if parent class doesn`t define a slots behavior
print(employee1.__dict__)