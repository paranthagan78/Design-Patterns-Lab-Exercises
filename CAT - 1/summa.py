def cal_price(*args,**kwargs):
    total = 0
    lst = list(kwargs.keys())
    print(args)
    print(lst)
    for i in range(len(args)):
        total += args[i] - (args[i]* kwargs[lst[i]]/100)
    return total

price = cal_price(100,200,300,400,d1=10,d2=20,d3=30,d4=40)
print(price)


def cal(*args,**kwargs):
    var=0
    lst=list(kwargs.values())
    for i in range(len(args)):
        var = var + (args[i] - (args[i]*lst[i]/100))
    print(var)
cal(10,20,30,d1=5,d2=10,d3=15)


class A():
    def fun(self):
        print("I'm function 1")

class B(A):
    def fun(self):
        super().fun()
        print("I'm function 2")

class C(A):
    def fun(self):
        super().fun()
        print("I'm function 3")
        
class D(B,C):        
    def fun(self):
        super().fun()
        print("I'm function 4")
        

d=D()
print(D.__mro__)
d.fun()


