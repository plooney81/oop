class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    # creates our print vehicle information method
    def print_info(self):
        print('\n{} {} {}'.format(self.year, self.make, self.model))