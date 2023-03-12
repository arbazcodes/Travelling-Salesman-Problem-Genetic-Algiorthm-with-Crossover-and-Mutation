import random

max = 10000

position = {"P": 0,
            "I": 1,
            "S": 2,
            "K": 3,
            "L": 4,
            "M": 5}

graph = [[0, 20, max, 250, max, 100],
         [20, 0, 30, max, 40, max],
         [max, 30, 0, 200, max, max],
         [250, max, 200, 0, 180, max],
         [max, 40, max, 180, 0, 90],
         [100, max, max, max, 90, 0]]

class genome:
    def __init__(self, _path, _fitness):
        self.path = _path
        self.fitness = _fitness
        
def fitness(genome):

    total_distance = 0

    for i in range(len(genome)-1):

        # if there is no path between the two cities return max, else add it to the
        if graph[position[genome[i]]][position[genome[i+1]]] == max:

            return max

        else:

            total_distance += graph[position[genome[i]]][position[genome[i+1]]]

    return total_distance

def generate_path(cities):
    start_city = random.choice(cities)
    remaining_cities = [city for city in cities if city != start_city]
    random.shuffle(remaining_cities)
    end_city = start_city
    path = [start_city]
    
    for i in range(len(remaining_cities)):
        if i == 6:
            break
        city = remaining_cities[i]
        if city != end_city:
            path.append(city)
    
    path.append(end_city)
    return ''.join(path)


def initialize_population(population_size, cities):
    population = []
    
    for i in range(population_size):
        path = generate_path(cities)
        individual = genome(path, fitness(path))
        population.append(individual)
        
    return population

population = initialize_population(population_size, cities)

for i in range(100):
    print(population[i].path, population[i].fitness)