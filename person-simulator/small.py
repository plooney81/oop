from person import Person
from vehicle import Vehicle

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