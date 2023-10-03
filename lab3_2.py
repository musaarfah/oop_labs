class Timespan2():
    def __init__(self,mins):
        self.mins=mins


    def show(self):
        hours=0
        while self.mins>=60:
            self.mins=self.mins-60
            hours+=1
        print(f'{hours} hours and {self.mins} minutes')

    def add_hours(self,x):
        hours=0
        while self.mins>=60:
            self.mins=self.mins-60
            hours+=1
        new_hrs=hours+x
        print(f'{new_hrs} hours and {self.mins} minutes')


    def add_mins(self,y):
        hours=0
        new_mins=self.mins+y
        while new_mins>=60:
            new_mins=new_mins-60
            hours+=1
        
        print(f'{hours} hours and {new_mins} minutes')

    def change_function(self,ts):
        mins=ts.mins-self.mins
        hours=0
        while mins>=60:
            mins=mins-60
            hours+=1
        print(f'{hours} hours and {mins} minutes')


def main():
    t1=Timespan2(130)
    t1.show()
    
    t1=Timespan2(140)
    t1.add_hours(2)

    t1=Timespan2(130)
    t1.add_mins(70)

    t1=Timespan2(120)
    ts=Timespan2(300)
    t1.change_function(ts)




    

main()