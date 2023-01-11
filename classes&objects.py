# Python Classes and Objects
'''
class testClass:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def sum(self):
        print(self.num1+self.num2)


objectOfClass0 = objectOfClass1 = objectOfClass2 = testClass(5, 6)
objectOfClass0.sum()
objectOfClass1.sum()
objectOfClass2.sum()
'''

'''
class testClass:
    def __init__(self):
        pass

    def sum(self, num1, num2):
        print(num1+num2)


obj = testClass()
obj.sum(5, 6)
'''

# Example with constructor
'''
class student:
    def __init__(self, name, sub1, sub2, sub3):
        self.name = name
        self.sub1 = sub1
        self.sub2 = sub2
        self.sub3 = sub3

    def tnm(self):
        print(self.name+" Total number:", self.sub1+self.sub2+self.sub3)

    def grd(self):
        if (self.sub1+self.sub2+self.sub3) >= 240:
            print("Grade: A+")
        if (self.sub1+self.sub2+self.sub3) < 120:
            print("Grade: F")


s0 = student("aaa", 80, 90, 95)
s1 = student("bbb", 30, 35, 28)
print(s0.tnm(), s0.grd())
print(s1.tnm(), s1.grd())
'''
