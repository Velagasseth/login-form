class Emp:
    def __init__(self,rate_per_day,rate_per_hour,no_of_hours):
        self.rate_per_day=rate_per_day
        self.rate_per_hour=rate_per_hour
        self.no_of_hours=no_of_hours

    def Evaluation(self):
        basic_salary=self.rate_per_day*31
        allowance=2000
        overtime=(self.rate_per_day*self.no_of_hours)
        grossC=(basic_salary+allowance+overtime)
        return grossC







#employee1=Emp(20, 30, 12)
#employee1.Evaluation()

