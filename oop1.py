#test2
class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary, age):
      self.name = name
      self.age = age
      self.salary = salary
      Employee.empCount += 1

   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
     print "Name:", self.name
     print "Salary:", self.salary
     print "Age:", self.age

emp1 = Employee("Zara", 2000, 6)
emp2 = Employee("Manni", 5000, 7)
emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee: %d" % Employee.empCount
