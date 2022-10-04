class Student:
    def __init__(self, name, age,id,gender,course):
        self.course = course
        self.age=age
        self.id=id
        self.gender=gender
        self.name = name

    def get_student_details(self):
        print("Your name is " + self.name + " age is " , self.age ," id-> ",self.id , " Gender is ",self.gender," Course -> ", self.course)
        