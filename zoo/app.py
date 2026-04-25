class Animal:
    def __init__(self, name, age=0, health=50, happiness=50):
        self.name = name
        self.age = age
        self.health = health
        self.happiness = happiness

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Health: {self.health}, Happiness: {self.happiness}")

    def feed(self):
        self.health += 10
        self.happiness += 10
        return self


class Lion(Animal):
    def __init__(self, name):
        super().__init__(name)

    def feed(self):
        self.health += 20
        self.happiness += 20
        return self


class Tiger(Animal):
    def __init__(self, name):
        super().__init__(name)

    def feed(self):
        self.health += 15
        self.happiness += 15
        return self


class Bear(Animal):
    def __init__(self, name):
        super().__init__(name)

    def feed(self):
        self.health += 5
        self.happiness += 5
        return self


class Zoo:
    def __init__(self, zoo_name):
        self.zoo_name = zoo_name
        self.animals = []

    def add_lion(self, name):
        self.animals.append(Lion(name))
        return self

    def add_tiger(self, name):
        self.animals.append(Tiger(name))
        return self

    def add_bear(self, name):
        self.animals.append(Bear(name))
        return self

    def print_all_info(self):
        print("-" * 20, self.zoo_name, "-" * 20)
        for animal in self.animals:
            animal.display_info()


zoo1 = Zoo("John's Zoo")

zoo1.add_lion("Nala")
zoo1.add_lion("Simba")
zoo1.add_tiger("Rajah")
zoo1.add_tiger("Shere Khan")
zoo1.add_bear("Baloo")

zoo1.print_all_info()