from person import Person

p1 = Person('Luiz', 29)
p2 = Person('João', 32)

print(p1.get_year_birth)
print(p2.get_year_birth)

p1.talk('POO')
p2.talk('Movies')

p1 = Person.by_year_birth('Luiz', 1987)
print(p1.name, p1.age)
p1.get_year_birth()
