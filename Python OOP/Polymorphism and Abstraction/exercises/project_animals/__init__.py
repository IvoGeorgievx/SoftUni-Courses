from polymorphism_and_abstraction.exercise.project_animalss.cat import Cat
from polymorphism_and_abstraction.exercise.project_animalss.kitten import Kitten

kitten = Kitten("Kiki", 1)
print(kitten.make_sound())
print(kitten)
cat = Cat("Johnny", 7, "Male")
print(cat.make_sound())
print(cat)