'''Handling an exception'''
class EvenOnly(list):
    def append(self, value):
        try:
            if isinstance(value,int):
                print("Only integers can be added")
        except:
            print("type error occured")
        try:
            if value % 2 != 0:
                print("Only even numbers can be added")
        
        except:
            print("Value error occured")
        super().append(value)

e=EvenOnly()
e.append(10)
print(e)
e.append(13)
print(e)
e.append('a')
#print(type('a'))
print(e)
