class Student():
    course = 3901
    group_name = "группа 3901"
    number_bilet = 0
    avg_grade = 0
    name = "Васильев"

    def addFio(self):
        self.mname = input("Введите имя: ")
        self.lname = input("Введите отчество: ")
        self.name = self.name+" "+self.mname+" "+self.lname
        print("Имя студента - "+self.name)

    def goToCollege(self):
        self.avg_grade += 1
        return self.avg_grade
    def upCourse(self):
        self.course += 1
        self.group_name = self.group_name[0:len(self.group_name)-1] + str(self.course % 10)
        return self.group_name



s = Student()
print(s.goToCollege())
print(s.goToCollege())
print(s.avg_grade)
print(s.name)
s.addFio()
print(s.name)
k = Student()
print(k.name)
print(s.upCourse())
