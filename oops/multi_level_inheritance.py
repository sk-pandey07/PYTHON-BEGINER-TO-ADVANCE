# Problem: Demonstrate multilevel inheritance in Python

class grandparent:
  def skill1(self):
    print("house")

class parent(grandparent):
  def skill2(self):
    print("car")

class child(parent):
  def skill3(self):
    print("bike")

c1 = child()
c1.skill1()
c1.skill2()
c1.skill3()
