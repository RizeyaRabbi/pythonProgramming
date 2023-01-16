# Python inheritance
'''
class parentClass:
    def __init__(self, num1=500, num2=100):
        self.number1 = num1
        self.number2 = num2

    def sum(self):
        print(self.number1+self.number2)


class childClass(parentClass):
    def __init__(self):
        parentClass.__init__(self, 100, 200)

    def printFromChild(self):
        parentClass.sum(self)


object1 = childClass()
object1.printFromChild()
object1.sum()

object2 = parentClass()
object2.sum()
'''

'''
class parentClass:
    def __init__(self, num1=100, num2=200):
        self.number1 = num1
        self.number2 = num2

    def sum(self):
        return self.number1+self.number2


class childClass(parentClass):
    def __init__(self, num1, num2):
        super().__init__(num1, num2)

    def printFromChild(self):
        print(parentClass.sum(self))


cobj = childClass(500, 600)
cobj.printFromChild()

pobj = parentClass()
print(pobj.sum())
'''
