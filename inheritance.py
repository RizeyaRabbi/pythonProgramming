# Python inheritance

class parentClass:
    def __init__(self, num1=500, num2=100):
        self.number1 = num1
        self.number2 = num2

    def sum(self):
        print(self.number1+self.number2)


class childClass(parentClass):
    def __init__(self):
        parentClass.__init__(self, 100, 50)

    def printFromChild(self):
        parentClass.sum(self)


object1 = childClass()
object1.printFromChild()
object1.sum()

object2 = parentClass()
object2.sum()
