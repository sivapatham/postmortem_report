import math
class report:
    def __init__ (self):
        self.temp1 = 0
        self.temp2 = 0
        self.rtemp = 0
        self.t = 0
        self.c = 0
        self.k = 0
        self.et = 0
    def values(self):
        print 'All temprature quantities in farenheit and time in minutes'
        self.temp1 = input ('Enter the intial measured temperature of the body: ')
        self.temp2 = input ('Enter the second measured temprature of the body: ')
        self.t = input ('Enter the time interval between the two measurements: ')
        self.rtemp = input ('Enter room temprature: ')
    def calc(self):
        self.c = self.temp1 - self.rtemp
        self.k = (math.log((self.temp2 - self.rtemp) / self.c)) / self.t
        self.et = -1 * (math.log((98.6 - self.rtemp) / self.c)) / self.k
    def print_report(self):
        print 'The time of death is ',self.et,'before the measurement of the first temprature'
def main():
    exp = report()
    exp.values()
    exp.calc()
    exp.print_report()
main()
    
