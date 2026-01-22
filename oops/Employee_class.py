# Problem: Create an Employee class with name and id


class employee:
  def __init__(self,name,id):
    self.name = name
    self.id = id

e1 = employee("tony",101)
print(e1.name)
print(e1.id)
