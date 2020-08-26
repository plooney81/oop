# given the following person class, write code to:

class Person:
    # because this is a primitive value(aka not a list or tuple or dictionary) we can update it for each instance and it won't update for all of the instances
    alive = True
    

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greet_counter = 0
        # becuase this is not a primitive value, we cannot use it as a class attribute and expect each list to be different from instance to instance.
        self.unique_greeting_counter = []
        

    def __str__(self):
        return 'This is {}. Whose phone # is {} and email is {}'.format(self.name, self.phone, self.email)

    def greet(self, other_person):
        print('\nHello {}, I am {}!'.format(other_person.name, self.name))
        self.greet_counter += 1
        if self.alive == False:
            print('{} can\'t answer right now, they are dead'.format(self.name))
        elif other_person.name not in self.unique_greeting_counter:
            self.unique_greeting_counter.append(other_person.name)
    
    def print_contact_info(self):
        print('\n{}\'s email is: {}\n{}\'s phone # is: {}'.format(self.name, self.email, self.name, self.phone))

    def add_friend(self, other_person):
        self.friends.append(other_person)
    
    def num_friends(self):
        return len(self.friends)

    def num_unique_people_greeted(self):
        return len(self.unique_greeting_counter)

    def die(self):
        self.alive = False

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    # creates our print vehicle information method
    def print_info(self):
        print('\n{} {} {}'.format(self.year, self.make, self.model))

# Instantiate an instance object of person with name of 'Sonny', email of 'sonny@hotmail.com', and phone of '483-485-4948'
sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")

# instantiate person named jordan
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")

lachlan = Person("Lachlan", "lachlan@yahoo.com", "678-555-1234")

# have jordan greet sonny
jordan.greet(sonny)
jordan.greet(sonny)
jordan.greet(lachlan)
lachlan.greet(sonny)

print(jordan.unique_greeting_counter)
print(lachlan.unique_greeting_counter)
#print contact info using our new methods
# sonny.print_contact_info()
# jordan.print_contact_info()

#show case our num_friends method and add_friends method
# print(jordan.num_friends())
# jordan.add_friend(sonny)
# print(jordan.num_friends())


# car = Vehicle("Tesla", "Cybertruck", "2020")

# car.print_info()
# print(str(jordan))
# print(jordan.num_unique_people_greeted())

jordan.die()
print(f'jordan is alive? {jordan.alive}')
print(f'sonny is alive? {sonny.alive}')

# jordan.greet(lachlan)
# sonny.greet(lachlan)