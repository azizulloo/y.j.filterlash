class Person:
    all_persons = []

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        Person.all_persons.append(self)

    @classmethod
    def filter_by_age(cls, min_age, max_age):
        return filter(lambda person: min_age <= person.age <= max_age, cls.all_persons)

    @classmethod
    def filter_by_gender(cls, gender):
        return filter(lambda person: person.gender == gender, cls.all_persons)

    def __repr__(self):
        return f"Person(name={self.name}, age={self.age}, gender={self.gender})"

person1 = Person("Aziza", 25, "Ayol")
person2 = Person("Bobur", 30, "Erkak")
person3 = Person("Alisher", 20, "Erkak")

for person in Person.all_persons:
    print(person)

print("\n20 yoshdan 30 yoshgacha bo'lgan yosh bo'yicha filtrlash:")
for person in Person.filter_by_age(20, 30):
    print(person)

print("\nErkak jinsi bo'yicha filtrlash:")
for person in Person.filter_by_gender("Erkak"):
    print(person)
