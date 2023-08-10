def check(hour, minutes, Second):
    while not(0 <= Second <= 60 and 0 <= minutes <= 60):
        if Second >= 60:
            Second -= 60
            minutes += 1
        if Second < 0:
            minutes -= 1
            Second += 60
        if minutes >= 60:
            minutes -= 60
            hour += 1
        if minutes < 0:
            hour -= 1
            minutes += 60
    return hour,minutes,Second

class Time:
    def __init__(self, hour1, hour2, minutes1, minutes2, Second1, Second2):
        self.H1 = hour1
        self.H2 = hour2
        self.M1 = minutes1
        self.M2 = minutes2
        self.S1 = Second1
        self.S2 = Second2

    def sum(self):
        hour, minutes, Second = self.H1 + self.H2, self.M1 + self.M2, self.S1 + self.S2
        hour, minutes, Second = check(hour, minutes, Second)
        return hour,minutes,Second
    
    def subtraction(self):
        hour, minutes, Second = self.H1 - self.H2, self.M1 - self.M2, self.S1 - self.S2
        hour, minutes, Second = check(hour, minutes, Second)
        return hour,minutes,Second
    
    def show(self,hour, minutes, Second):
        print(f"Answer is:{hour}:{minutes}:{Second}")
    

op = int(input("1_sum\n2_subtraction\nPlease enter your choice: "))
time_1 =input("Please enter time1:for exampel (20:45:30)\n")
time_2 = input("Please enter time2:for exampel (20:45:30)\n")

time = Time(int(time_1.split(":")[0]), int(time_2.split(":")[0]), int(time_1.split(":")[1]), int(time_2.split(":")[1]), int(time_1.split(":")[2]), int(time_2.split(":")[2]))

if op == 1:
    hour, minutes, Second = time.sum()
    time.show(hour, minutes, Second)
elif op == 2:
    hour, minutes, Second = time.subtraction()
    time.show(hour, minutes, Second)