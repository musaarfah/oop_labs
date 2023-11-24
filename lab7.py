class Department:
    def __init__(self,name,loc):
        self.name=name
        self.loc=loc

    def __str__(self) -> str:
        return f'{self.name}\t Location: {self.loc}'
        
class Employee:
    def __init__(self,e_nmbr,name,cnic,phone_no,address,department):
        self.e_nmbr=e_nmbr
        self.name=name
        self.cnic=cnic
        self.phone_no=phone_no
        self.address=address
        self.department=department
        

    def __str__(self):
        return f'Name:{self.name}\tEmployee Number:{self.e_nmbr}\tCNIC:{self.cnic}\nPhone No:{self.phone_no}\tAddress:{self.address}\nDepartment :{self.department}'
        

    
class Salaried(Employee):
    def __init__(self,e_nmbr,name,cnic,phone_no,address,weekly_salary,department):
        super().__init__(e_nmbr,name,cnic,phone_no,address,department)
        self.weekly_salary=weekly_salary

    def __str__(self):
        return f'{super().__str__()}\tSalary:{self.weekly_salary}'
    
    

class Hourly(Employee):
    def __init__(self,e_nmbr,name,cnic,phone_no,address,hours_worked,rate_ph,department):
        super().__init__(e_nmbr,name,cnic,phone_no,address,department)
        self.hours_worked=hours_worked
        self.rate_ph=rate_ph
        self.weekly_sal=rate_ph*hours_worked


    
    
    def __str__(self):
        return f'{super().__str__()}\tSalary:{self.weekly_sal}'
    

    
class Payroll:
    def __init__(self) -> None:
        self.employees=[]
    
    def add_emp(self,emp):
        self.employees.append(emp)
    
    def show(self): 
       for employee in self.employees:
           print(employee)


    
def main():
    sales=Department('Sales','Lahore')
    acc=Department('Accounting','Kasur')
    man=Department('Manufacturing','Faislabad')
    
    
    rizwan=Salaried(12,'Rizwan','0000-0000000-0','01234567899','Kamoki',82000,sales)
    fakhar=Hourly(11,'Fakhar Zaman','34202-091731-8','0307-1234589','Khanpur',40,1800,acc)
    kohli=Hourly('7','Virat Kohli','3202-081931-7','0317-0987111','Punjabi',40,3500,man)

    pr=Payroll()
    pr.add_emp(rizwan)
    pr.add_emp(fakhar)
    pr.add_emp(kohli)
    pr.show()
main()
    




        