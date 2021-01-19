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