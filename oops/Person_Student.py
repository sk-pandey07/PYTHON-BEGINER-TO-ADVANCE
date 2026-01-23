# Problem: Demonstrate inheritance using Person and Student classes

class person:
  def __init__(self,name,id):
    self.name = name
    self.id = id
  def show_details(self):
    print("name:",self.name)
    print("id:",self.id)

class student(person):
  def __init__(self,name,id,roll_no,course):
    super().__init__(name,id)
    self.roll_no = roll_no
    self.course = course

  def show_student(self):
    self.show_details()
    print("roll_no:",self.roll_no)
    print("course:",self.course)

s1 = student("shashi",101,"001","bca")
s1.show_student()
