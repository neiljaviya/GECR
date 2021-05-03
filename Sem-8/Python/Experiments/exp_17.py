#Create a class Employee with data members: name, department and salary. 
#Create suitable methods for reading and printing employee information

class Employee:
  def __init__(self, name, dept, salary):
    self.name = name
    self.dept = dept
    self.salary = salary

  def print_data(self):
    print("Data for",self.name,":")
    print("\tDepartment:",self.dept,"\n\tSalary:",self.salary,"\n\n")
    
e1 = Employee("Neil", "Management", 100000)
e2 = Employee("Rahul", "ios", 80000)
e3 = Employee("Happy", "web", 70000)

e1.print_data()
e2.print_data()
e3.print_data()