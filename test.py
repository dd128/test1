class Test:
    i=10
    def prt(self):
        print(self)
        print(self.i)
        print(self.__class__)
 
t = Test()
t.prt()
t.i=t.i+1
print (t.i)

print('类也是对象：')
Test.prt(Test)
Test.i=Test.i*2
print(Test.i)

c=Test()
print(c.i)




