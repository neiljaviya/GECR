#Create a class student with following member attributes: roll no, name, age and 
#total marks. Create suitable methods for reading and printing member variables. 
#Write a python program to overload ‘==’ operator to print the details of students 
#having same marks

class Student:
  def __init__(self, roll, name, age, total):
    self.roll = roll
    self.name = name
    self.age = age
    self.total = total
  
  def print_vals(self):
    print("Roll No -",self.roll,"\nName -",self.name,"\nAge -",self.age,"\nTotal -",self.total,"\n")
    
  def __eq__(self, another):
    if self.total == another.total:
      print("Both have same Total\n")
      self.print_vals()
      another.print_vals()
    else:
      print("Both have different Total\n")
      
s1 = Student(44, "Neil", 21, 99)
s2 = Student(51, "Kwiza", 22, 98)
s3 = Student(38, "Rahul", 21, 99)
s4 = Student(66, "Happy", 21, 99)
s5 = Student(6, "Hiral", 21, 96)

s1 == s3
s1 == s2