class AdminUser():
#add admin
    def __init__(self, adminName, password):
        self.adminName = adminName
        self.password = password

        
#delete student from database stud
    def deleteStud(self, stud_id):
        stud_id = input("enter student id: ")
        if stud_id in stud_database:
            stud_database.remove(stud_id)
            print("student deleted: ", stud_database)
        else:
            print("student not found")
                         
class Student():
    
    def __init__(self, stud_name, stud_id, stud_dept):
        self.stud_name = stud_name
        self.stud_id = stud_id
        self.stud_dept = stud_dept
    
class Course():
    
    def Admin_course(self, adName, adPass):
        self.adName = adName
        self.adPass = adPass
    
    def addCourse(self, courseInstr, courseName, courseNum, courseTopic):
            self.courseInstr=courseInstr
            self.courseName=courseName
            self.courseNum=courseNum
            self.courseTopic=courseTopic
            self.students = list()
            self.grades = list()
 
    def modifyCourse(self, course_id):
        if course_id == self.courseNum:
            print("Enter new course details below:")
            crse_name = input("Course nameCode: ")
            crse_num = input("Course number: ")
            crse_topic = input("Course topic: ")
            self.courseName = crse_name
            self.courseNum = crse_num
            self.courseTopic = crse_topic
    
    def delCourse(self, course_id):
        A = "yes"
        B = "no"
        if course_id == self.courseNum:
            print("Course details: ", self.courseInstr, self.courseName + self.courseNum, self.courseTopic, self.students)
            print("Do you want to delete course: ")
            answer = input("enter yes or no: ")
            if answer == A:
                self.courseInstr = ""
                self.courseName = ""
                self.courseNum = ""
                self.courseTopic = ""
                self.students = ""
                self.grades = ""
                print("Course Deleted!")
            elif answer == B:
                print("Course Not deleted")
    
    #only takes in student ID
    def enrol(self, stud_id):
        self.students.append(stud_id)
    
    def unenrol(self, stud_id):
        if stud_id in self.students:
            self.students.remove(stud_id)
        else:
            print("student not found!")
    
    #Modify student ID
    def modifyStudent(self, stud_id):
        for i in range(self.students.__len__()):
            if stud_id in self.students[i]:
                print("Student ID found")
                stud_id = input("enter New student ID: ")
                self.students[i] = stud_id
                
                
    def addStudgrade(self, stud_id):
        for i in range(self.students.__len__()):
            if stud_id in self.students[i]:
                grade = input("enter student grade: ")
                self.grades.insert(i, grade)
    
    def checkStudGrade(self, stud_id):
        for i in range(self.students.__len__()):
            if stud_id in self.students[i]:
                print("Your grade is: ", self.grades[i])


1. Create course #only course admin
2. enrol student #only course admin
3. unenrol student #only course admin
4. Modify course #only course admin
5. Modify student #only course admin
6. Submit grades #only course admin
7. delete student #System admin
8. students enrol courses
9. student see the courses enrolled




adminC = Course()
adminC.Admin_course("Edikan", "edi54")
ad1 = input("enter admin name: ")
ad2 = input("enter admin password: ")

if adminC.adName == ad1 and adminC.adPass == ad2:

    course1 = Course()
    course2 = Course()
    course3 = Course()

#AddCourse
    course1.addCourse("James", "ELG", "5300", "Software dev")
    course2.addCourse("Jeff", "GNG", "7100", "Java")
    course3.addCourse("Joe", "ELG", "6500", "Full stack")

#AddStudent
    student1 = Student("Edikan", "000557", "Elec")
    student2 = Student("Gabriel", "000600", "Meng")
    student3 = Student("Jane", "000700", "Peng")

#enrol student_id to course1
    course1.enrol(student1.stud_id)
    course1.enrol(student2.stud_id)
    course1.enrol(student3.stud_id)
    print(vars(course1))
#unenrol student 2 from course1
    print("---------------------")
    print("---------------------")
    
    course1.unenrol(student1.stud_id)
    print(vars(course1))
#modify Course1, accepts input so I commented it out
    print("---------------------")
    print("---------------------")
    course1.modifyCourse(course1.courseNum)    
    print(vars(course1))

#submit student grade, accepts input
    print("---------------------")
    print("------submit grade----------")
    print("---------------------")
    course1.addStudgrade(student2.stud_id)
    course1.addStudgrade(student3.stud_id)
    print(vars(course1))

    print("---------------------")
    print("-------check student grade for student 2-------------")
    print("---------------------")
    course1.checkStudGrade(student2.stud_id)

#modify student
    print("---------------------")
    print("-------Modify Student----------")
    print("---------------------")
    course1.modifyStudent(student3.stud_id)
    print(vars(course1))

#del Course1, accepts input so I commented it out
    print("---------------------")
    print("--------delete Course1---------")
    print("---------------------")
    course1.delCourse(course1.courseNum)
    print(vars(course1))
    
else:
    print("You are not authorized to perform this action!")

"""
print("---------------------")
print("--------delete Student---------")
print("---------------------")

admin_all = AdminUser("Russell", "rus240")
ad3 = input("enter admin name: ")
ad4 = input("enter admin password: ")

if admin_all.adminName == ad3 and admin_all.password == ad4:
    student1 = Student("Edikan", "000557", "Elec")
    student2 = Student("Gabriel", "000600", "Meng")
    student3 = Student("Jane", "000700", "Peng")
    #student database
    stud_database = [[student1.stud_name, student1.stud_id, student1.stud_dept],
                     [student2.stud_name, student2.stud_id, student2.stud_dept],
                     [student3.stud_name, student3.stud_id, student3.stud_dept]]

    
    print(stud_database)
    
    stud_database.deleteStud(student1.stud_name)
    
    print(stud_database)
else:
    print("student not found: ")
    """