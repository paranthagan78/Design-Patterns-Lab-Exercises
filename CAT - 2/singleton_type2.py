class Singleton2:

  __instance = None 

  def __new__(cls):

    if (cls.__instance is None):
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


class sin:
  _instance=None
  def __new__(cls):
    if cls._instance is None:
      cls._instance=super(sin,cls).__new__(cls)
    return cls._instance
s=sin()
s1=sin()
print(s)
print(s1)
print(s1 is s)
