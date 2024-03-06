class Employee:
      def __init__(self, name, age, position, salary) -> None:
            self.name = name
            self.age = age
            self.position = position
            self.salary = salary

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

employee1 = Employee("Ji-Soo", 38, "developer", 1200)
employee2 = Employee("Lauren", 44, "tester", 1250)

employee2.increase_salary(20)

print(eval(repr(employee1)))