class employee:
  def meera_function(self,name,age,sal,address,city):
    self.name =name
    self.age =age
    self.sal = sal
    self.address = address
    self.city = city
  
  
  def get_num(self):
    print("name is :",self.name)
    print("age is:",self.age)
    print("sal is:",self.sal)
    print("address is:",self.address)
    print("city is :",self.city)

output= employee('meera',23,56000,'at pune','ambajogai')
output.get_num()
