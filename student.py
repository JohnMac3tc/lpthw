__author__ = 'johnmcelligott'
class Student():
    def __init__(self, stdName, stdId, stdScore):
        self.name = stdName
        self.id = stdId
        self.score = stdScore

    def getScore(self):
        return self.score



std1 = Student("Joe", 1, 78)

print(std1.getScore())

aList = [std1]

print(len(aList))

