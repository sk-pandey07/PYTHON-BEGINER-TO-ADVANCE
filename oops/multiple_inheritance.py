# Problem: Demonstrate multiple inheritance in Python

class father:
  def skill1(self):
    print("driving")

class mother:
  def skill2(self):
    print("cocking")

class child(father,mother):
  def skill3(self):
    print("coding")

c1 = child()
c1.skill1()
c1.skill2()
c1.skill3()
