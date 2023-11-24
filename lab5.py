class Department:
    def __init__(self,name,chairman,id):
        self.name=name
        self.chairman=chairman
        self.__id=id

    def __str__(self) -> str:
        return f'Department : {self.name} , {self.chairman} , {self.__id}'

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self,new_id):
        return new_id
    
    

class Student:
    def __init__(self,name,roll,sem,cgpa,dept_id):
        self.name=name
        self.roll=roll
        self.sem=sem
        self.cgpa=cgpa
        self.__dept_id=dept_id

    def __str__(self) -> str:
        return f'{self.name}\t\t{self.roll}\t\t\t\t{self.sem}\t\t{self.cgpa}'
    
    
    def less_cgpa(self):
         if float(self.cgpa) < 1.7:
            return f'{self.name}\t\t{self.roll}\t\t\t\t{self.sem}\t\t{self.cgpa}'
        
         
        

    @property
    def dept_id(self):
        return self.dept_id
    @dept_id.setter
    def dept_id(self,new_dept_id):
        return new_dept_id
    



    
cs_dept=Department('Computer Science','Dr. Erwin Smith','CS')
    
cs_stdnts=[
    Student('Eren Jeager','BSCSF19112','2','1.4','CS'),
    Student('Zeke Jeager','BSCSF18234','6','3.97','CS'),
    Student('Mikasa Ackerman','BSCSF19115','4','3.45','CS')
]

ds_dept=Department('Data Science','Dr.Yamamoto Genryusai','DS')
ds_stdnts=[
    Student('Ichigo Kurosaki','BSDSF19112','2','1.50','DS'),
    Student('Urahara Kisuke','BSDSF18234','6','3.97','DS'),
    Student('Jushiro Ukitake','BSDSF19115','4','3.45','DS')
]

se_dept=Department('Software Engineering','Dr.Vegapunk','SE')
se_stdnts=[
    Student('Monkey.D Luffy','BSSEF19112','2','1.50','SE'),
    Student('Roronoa Zoro','BSSEF18234','6','3.97','SE'),
    Student('Vinsmoke Sanji','BSSEF19115','4','3.45','SE')
]

it_dept=Department('Information Technology','Dr.Tsunade','IT')
it_stdnts=[
    Student('Uzamaki Naruto','BSITF19112','2','1.50','IT'),
    Student('Hatake Kakashi','BSitF18234','6','3.97','IT'),
    Student('Nara Shikamaru','BSITF19115','4','3.45','  IT')
]


print(cs_dept)
print(f'Name\t\t\tRoll-No\t\t\t\t\tSemester\tCGPA')
for i in range(3):
    print(cs_stdnts[i])
print()

print(ds_dept)
print(f'Name\t\t\tRoll-No\t\t\t\t\tSemester\tCGPA')
for i in range(3):
    print(ds_stdnts[i])
print()

print(se_dept)
print(f'Name\t\t\tRoll-No\t\t\t\t\tSemester\tCGPA')
for i in range(3):
    print(se_stdnts[i])
print()

print(it_dept)
print(f'Name\t\t\tRoll-No\t\t\t\t\tSemester\tCGPA')
for i in range(3):
    print(it_stdnts[i])
print()

print(f'STUDENTS WITH GPA LESS THAN 1.7')
for i in range (len(cs_stdnts)):
    low_stdnt=cs_stdnts[i].less_cgpa()
    if low_stdnt:
        print(cs_dept)
        print(f'Name\t\t\tRoll-No\t\t\t\t\tSemester\tCGPA')
        print(low_stdnt)

for student in ds_stdnts:
    low_stdnt=student.less_cgpa()
    if low_stdnt:
     print(ds_dept)
     print(f'Name\t\t\tRoll-No\t\t\t\t\tSemester\tCGPA')
     print(low_stdnt)

for student in se_stdnts:
    low_stdnt=student.less_cgpa()
    if low_stdnt:
     print(se_dept)
     print(f'Name\t\t\tRoll-No\t\t\t\t\tSemester\tCGPA')
     print(low_stdnt)


for student in it_stdnts:
    low_stdnt=student.less_cgpa()
    if low_stdnt:
     print(it_dept)
     print(f'Name\t\t\tRoll-No\t\t\t\t\tSemester\tCGPA')
     print(low_stdnt)