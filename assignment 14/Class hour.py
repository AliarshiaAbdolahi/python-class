class time:
    def __init__(self,hour,minut,second,hour_2,minut_2,second_2,operation):
        # Properties
        # SUM:
        self.H = hour + hour_2
        self.M = minut + minut_2
        self.S = second + second_2
        # SUBTRACTION:
        self.H_2 = hour - hour_2
        self.M_2 = minut - minut_2
        self.S_2 = second - second_2
        self.OP = operation
        # Methods
    def sum(self):
        while not(0 <= self.S <= 60 and 0 <= self.M <= 60):
            if self.S >= 60:
                self.S -= 60
                self.M += 1
            if self.S < 0:
                self.M -= 1
                self.S += 60
            if self.M >= 60:
                self.M -= 60
                self.H += 1
            if self.M < 0:
                self.H -= 1
                self.M += 60
        print(f"{self.H}:{self.M}:{self.S}")

    def subtraction(self):
        while not(0 <= self.S <= 60 and 0 <= self.M <= 60):
                if self.S < 0:
                    self.M -= 1
                    self.S += 60
                    if self.M < 0:
                        self.H -= 1
                        self.M += 60
        print(f"{self.H}:{self.M}:{self.S}")

Time_A = input("enter time1:for exampel (20:45:30)\n")
Time_B = input("enter time2:for exampel (20:45:30)\n")
opertion = int(input('''
1_(sum)
2_(subtraction)
Please enter your choice: '''))
Time_A = Time_A.split(":")
Time_A = [eval(i) for i in Time_A]
Time_B = Time_B.split(":")
Time_B = [eval(i) for i in Time_B]
Time = time(Time_A[0],Time_A[1],Time_A[2],Time_B[0],Time_B[1],Time_B[2], opertion)
if opertion == 1:
    time.subtraction()
elif opertion == 2:
    time.sum()
else:
    print("Sorry,your number has a problem\nPlaese try again.")