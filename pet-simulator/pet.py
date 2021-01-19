class Pet:
    def __init__(self, name, fullness=50, happiness=50, hunger=5, mopiness=5):
        self.name = name
        self.fullness = fullness
        self.happiness = happiness
        self.hunger = hunger
        self.mopiness = mopiness
        self.toys = []
    
    def __str__(self):
        return f"""
            {self.name}:
                Fullness: {self.fullness}
                Happiness: {self.happiness}
        """

    def eat_food(self, some_food):
        self.fullness += some_food.fullness_effect
        self.happiness += some_food.happiness_effect

    def get_love(self):
        self.happiness += 30

    def be_alive(self):
        self.fullness -= self.hunger
        self.happiness -= self.mopiness
        for toy in self.toys:
            self.happiness += toy.use()
    
    def get_toy(self, some_toy):
        self.toys.append(some_toy)
        
class CuddlyPet(Pet):
    def __init__(self, name, fullness=50, hunger=5, cuddle_level=1):
        super().__init__(name, fullness, 100, hunger, 1)
        self.cuddle_level = cuddle_level
    
    def __str__(self):
        return f"""
            {self.name}:
                Fullness: {self.fullness}
                Happiness: {self.happiness}
                EXTRA CUDDLY
        """
    def be_alive(self):
        super().be_alive()
        self.happiness += self.mopiness/2

        
    def cuddle(self, other_pet):
        # Super cuddle powers, activate!
        for i in range(self.cuddle_level):
            other_pet.get_love()