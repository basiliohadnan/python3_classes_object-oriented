class Employee:
      def __init__(self, name, age, position, salary) -> None:
            self.name = name
            self.age = age
            self.position = position
            self.salary = salary
            self._annual_salary = None

      def increase_salary(self, percent):
            self.salary += self.salary * (percent/100)

      def __str__(self) -> str:
            return f"{self.name} is {self.age} years old. Employee is a {self.position} with salary of ${self.salary}"
      
      def __repr__(self) -> str:
            return (
                  f"Employee("
                  f"{repr(self.name)}, {repr(self.age)}, "
                  f"{repr(self.position)}, {repr(self.salary)})"
            )
      
      @property      
      # property basic declaration
      def salary(self):
            return self._salary
      
      @salary.setter
      # property setter, based on the declaration syntax
      def salary(self, salary):
            if (salary < 1000):
                  raise ValueError('Minimum wage is 1000.')
            # resets annual salary value before changing it
            self._annual_salary = None
            self._salary = salary

      @property
      # computed property
      def annual_salary(self):
            # only modifies annual salary if it was not filled before
            if self._annual_salary is None:
                  self._annual_salary = self.salary * 12
            return self._annual_salary 

employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1250)

print(employee1.annual_salary)
employee1.salary = 2000
print(employee1.annual_salary)