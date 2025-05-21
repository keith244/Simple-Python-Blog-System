"""Object-Oriented Programming (OOP) in Python"""

class Dog:
    species = 'Cannis fimiliaris' # all dogs created will have this similar attribute
    def __init__(self,name,age,):#breed): # changes for every dog i.e name = Terry or James etc
        self.name = name
        self.age = age
        # self.breed = breed

    def __str__(self):
        return f'{self.name} is {self.age} years old.'
    # instance method
    def description(self):
        return f'{self.name} is {self.age} year old '
    
    def speak(self,sound):
        return f'{self.name} says {sound}'

class GoldenRetriever(Dog):
    def speak(self,sound = 'Bark'):
        return super().speak(sound)


class Terrie(Dog):
    def speak(self, sound):
        return super().speak(sound)

goldie = GoldenRetriever('goldie',4,)
print(goldie.speak())
print(goldie)
terry = Terrie('terry',4)
print(terry.speak('Woof woof woof'))
print(type(terry))
print(isinstance(terry,Dog))
miles = Dog('Miles',4)
print(miles)
sound = miles.speak('Woof! Woof!')
print(sound)
print(miles.description())
print(miles.species)

class DogPark(Dog):
    pass

class Car:
    def __init__(self,color,mileage):
        self.color = color
        self.mileage = mileage
    
    def __str__(self):
        return f'The {self.color} car has {self.mileage} miles'

toyota = Car('red',20000)
print(toyota)


fname = ''
age = 23
role = ''
id_number = 0000
kirk = {'James':fname,
        34:age,
        'Captain':role,
        2265:id_number}
for key in kirk:
    if key == 'James':
        print(key)
print(kirk['James'])