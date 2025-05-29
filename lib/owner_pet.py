# lib/owner.py
class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        # Return all pets whose owner is this instance
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("add_pet expects a Pet instance")
        pet.owner = self

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)


# lib/pet.py
class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet_type '{pet_type}'")
        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
