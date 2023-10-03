class Timespan():
    def __init__(self,hrs,mins):
        self.hrs=hrs
        self.mins=mins

    def show(self):
        print(f'{self.hrs} hours and {self.mins} minutes')

    def add_hours(self,x):
        new_hrs=self.hrs+x
        print(f'{new_hrs} hours and {self.mins} minutes')


    def add_mins(self,y):
        new_mins=self.mins+y
        while new_mins>=60:
            new_mins=new_mins-60
            self.hrs+=1
        
        print(f'{self.hrs} hours and {new_mins} minutes')

    def change_function(self,ts):
       self_mins=self.hrs*60+self.mins
       ts_mins=ts.hrs*60+ts.mins
       diff=ts_mins-self_mins
       print(diff)





    
    


def main():
    t1=Timespan(2,30)
    t1.show()
    t1.add_hours(2)
    t1.add_mins(40)

    ts=Timespan(7,45)
    t1.change_function(ts)

main()