
import pydantic as _pydantic

class Animal():
    name: str
    species: str
    height: int

def my_func(animal):
    animal.name = "myname"
    animal.species = "giraffe"
    animal.height = 5

if __name__ == "__main__":
    a = Animal()
    my_func(a)
    print(a.name, a.species, a.height)