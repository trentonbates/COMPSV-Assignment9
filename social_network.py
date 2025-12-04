class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    
    def __init__(self, name):
        self.name = name
        self.friends = list()

    def add_friend(self, friend):
        if not isinstance(friend, Person):
            raise TypeError('The new friend needs to be a Person object.')
        else:
            self.friends.append(friend)

class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    
    def __init__(self):
        self.people = dict()

    def add_person(self, name):
        if name not in self.people.keys():
            tempPerson = Person(name)
            self.people[tempPerson.name] = tempPerson
        else:
            print(f'{name} is already in the network!')

    def add_friendship(self, person1_name, person2_name):
        if person1_name not in self.people.keys():
            print(f"Friendship not created. {person1_name} doesn't exist!")
        elif person2_name not in self.people.keys():
            print(f"Friendship not created. {person2_name} doesnt exist!")
        else:
            self.people[person1_name].add_friend(self.people[person2_name])
            self.people[person2_name].add_friend(self.people[person1_name])

    def print_network(self):
        for person in self.people.keys():
            result = f'{person} is friends with: '

            for person in self.people[person].friends:
                result += f'{person.name}, '

            print(result[0:-2])
        print()

alex = Person('Alex')
jordan = Person('Jordan')

assert alex.name == 'Alex'
assert alex.friends == list()
assert jordan.name == 'Jordan'
assert jordan.friends == list()

alex.add_friend(jordan)

assert alex.friends[0].name == 'Jordan'

network = SocialNetwork()
network.add_person('Alex')
network.add_person('Jordan')

print(network.people)

network.add_person('Morgan')
network.add_person('Taylor')
network.add_person('Casey')
network.add_person('Riley')

network.add_friendship('Alex', 'Jordan')
network.add_friendship('Alex', 'Morgan')
network.add_friendship('Jordan', 'Taylor')
network.add_friendship('Jordan', 'Johnny')
network.add_friendship('Morgan', 'Casey')
network.add_friendship('Taylor', 'Riley')
network.add_friendship('Casey', 'Riley')
network.add_friendship('Morgan', 'Riley')
network.add_friendship('Alex', 'Taylor')

network.print_network()

network.add_person('Alex')

network.print_network()

'''
Why is a graph the right structure to represent a social network?

    A graph structure is the right structure to represent a social network because it is able
    to show the relationship between people and their friendships. In the model that was
    implemented, people are the nodes while friendships are the edges on the graph. Social networks
    are also non-heirarchical and can often have circular friendships. With a graph being flexible
    enough to model these connections, it is the best structure to represent a social network.

Why wouldn't a list or tree work as well for this?

    Neither a list nor a tree would work as well to represent a social network. A list is only useful
    for sequential or linear data and lacks the structure to efficiently show complex relationships
    between elements. Searching for a specific person would be slow as it would have to iterate over
    the entire list of people. A tree does offer more than a list, but its usefulness in this scenario
    stops with only allowing each node to have a single parent.

What performance or structural trade-offs did you notice when adding friends or printing the network?

    With performance trade-offs, the use of a dictionary to map names to their corresponding Person
    object results in constant time. The adding of a friend also results in constant time since it is
    only appending to the end of a list. Printing the network does require to iterate through each person
    and then iterating through their friends which does cause a performance loss and could cause issues
    if scaled too big. The structural trade-off is related to how friendships are stored. When adding a
    friendship, the method gets called twice, and the friendship is also stored twice, once in each person's
    friendships. This will in the end speed up the process of finding all of a person's friends, which happen instantly.
'''