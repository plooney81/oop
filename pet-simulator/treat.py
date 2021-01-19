class Treat():
    def __init__(self, name, fullness_effect, happiness_effect):
        self.name = name
        self.fullness_effect = fullness_effect
        self.happiness_effect = happiness_effect
    
    def __str__(self):
        return f'{self.name} '
    
class ColdPizza(Treat):
    def __init__(self):
        super().__init__('Cold Pizza', 10, 25)

class Bacon(Treat):
    def __init__(self):
        super().__init__('Bacon', 5, 30)

class VeganSnack(Treat):
    def __init__(self):
        super().__init__('Vegan Snack', 5, 20)
