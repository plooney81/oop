from pet import Pet, CuddlyPet
from toy import Toy
from treat import ColdPizza, Bacon, VeganSnack
from menu import Menu

# Begin with no pets.
pets = []

main_menu = [   
    "Adopt a Pet",
    "Play with Pet",
    "Feed Pet",
    "View status of pets",
    "Give a toy to all your pets",
    "Do nothing",
]

adoption_menu = [
    "Pet",
    "Cuddly Pet"
]

menu_menu = [
    'Cold Pizza',
    'Bacon',
    'Vegan Snack'
]

def main():
    app = Menu('Please choose an Option: ', main_menu)
    types = Menu('Please choose a Pet Option: ', adoption_menu)
    treats = Menu('Please choose a Treat Option: ', menu_menu)
    while True:
        choice = app.get_choice()
        if choice == 1:
            pet_name = input('What do you want to name your pet?')
            type_choice = types.get_choice()
            if (type_choice == 1):
                pets.append(Pet(pet_name))
            elif (type_choice == 2):
                pets.append(CuddlyPet(pet_name))
            print(f'\n\nYou now have {len(pets)} pets')
        elif choice == 2:
            for pet in pets: pet.get_love()
        elif choice == 3:
            treat_choice = treats.get_choice()
            food_to_feed = 0
            if(treat_choice == 1):
                food_to_feed = ColdPizza()
            elif(treat_choice == 2):
                food_to_feed = Bacon()
            elif(treat_choice == 3):
                food_to_feed = VeganSnack()
            for pet in pets: pet.eat_food(food_to_feed)
        elif choice == 4:
            for pet in pets:
                print(pet)
        elif choice == 5:
            for pet in pets:
                pet.get_toy(Toy())
        elif choice == 6:
            for pet in pets: 
                pet.be_alive()
                print(pet)

main()