class ClassData:

    def __init__(self):
        self.infimum = 0.0
        self.supremum = 0.0
        self.population = 0
        self.experimental_frequency = 0.0
        self.theorical_frequency = 0.0

    def __str__(self):
        return f"ClassData(infimum:{self.infimum}, " \
               f"supremum:{self.supremum}, " \
               f"population: {self.population}, " \
               f"experimental_frequency:{self.experimental_frequency}, " \
               f"theorical_frequency:{self.theorical_frequency})"

    def __repr__(self):
        return str(self)
