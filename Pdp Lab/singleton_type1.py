#1 Here we do use exception methods, 

class Singleton1:

  instance = None     #it will save the object created for the class. it called as class variable.
  
  def __init__(self):   # works if we don't have the static method
    if Singleton1.instance != None:
       raise Exception("Singleton object already created!")
    else:
       Singleton1.instance = self


  @staticmethod 
  def getInstance():
    if Singleton1.instance == None:
      Singleton1()
    return Singleton1.instance

  

s1 = Singleton1.getInstance()
print(s1)
s2 = Singleton1.getInstance()
print(s2)

s1.x = 5
print(s1.x)
s2.x = 10
print(s2.x)
print(s1.x)

#s3=Singleton1()



#2 Here we don't need any exception methods

class Singleton2:

  __instance = None 

  def __new__(cls):

    if (cls.__instance is None):    # it will be applicable for all classes

      cls.__instance = super(Singleton2,cls).__new__(cls)
    
    return cls.__instance 

s1 = Singleton2()
print(s1)
s2 = Singleton2()
print(s2)

s1.x = 5
print(s1.x)

s2.x = 15
print(s2.x)

print(s1.x)