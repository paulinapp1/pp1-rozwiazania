class Statistics:
    def __init__(self):
        self.numbers=[]
    def add_num(self, number):
        self.numbers.append(number)
    def display_num(self):
        print(' '.join(map(str, self.numbers)))
    def largest_num(self):
        print(f"Largest number is: {max(self.numbers)}")
    def smallest_num(self):
        print(f"The smallest number is: {min(self.numbers)}")
    def mean(self):
        total=sum(self.numbers)
        length=len(self.numbers)
        print(f"The Arithmetic mean is: {total/length}")
    def median(self):
        self.numbers.sort()  
        length = len(self.numbers)
        if length % 2 == 0:  # Jeśli lista ma parzystą liczbę elementów
            mid = length // 2
            print( (self.numbers[mid - 1] + self.numbers[mid]) / 2)
        else:  
              mid = length // 2
              print( f"The median is: {self.numbers[mid]}")


my_numbers=Statistics()
my_numbers.add_num(12)
my_numbers.add_num(37)
my_numbers.add_num(6)
my_numbers.add_num(9)
my_numbers.add_num(17)
my_numbers.display_num()
my_numbers.largest_num()
my_numbers.smallest_num()
my_numbers.mean()
my_numbers.median()





