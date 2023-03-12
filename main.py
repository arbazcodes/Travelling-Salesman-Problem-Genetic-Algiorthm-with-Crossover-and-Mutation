from random import randint
import random

# Initialize Parameters.
mutation_rate = 3
population_size = 100
total_generations = 10
selection_pressure = 5
threshhold = 600
max = 1000

# Initialize Graph.

total_cities = 6

cities = "PISKLM"

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

# Define genome class.
# Includes the path taken and fitness.
# Fitness is calculated the total distance travelled on a given path .
class genome:
    def __init__(self, _path, _fitness):
        self.path = _path
        self.fitness = _fitness

# Define fitness function.
# Calculates fitness by adding the distance between all the neigbouring cities in the genome,
# and return the total distance traversed in a given path.
def fitness(genome):

    total_distance = 0

    for i in range(len(genome)-1):

        # if there is no path between the two cities return max, else add it to the
        if graph[position[genome[i]]][position[genome[i+1]]] == max:

            return max

        else:

            total_distance += graph[position[genome[i]]][position[genome[i+1]]]

    return total_distance

# Function to return a random sample of genomes from a given population.
def select_population(population, number):

    selected = []

    while (len(selected) < number):

        value = randint(0, len(population)-1)

        if population[value] not in selected:

            selected.append(population[value])

    return selected

# Define Tournament Selection function.
# Return the a certain number of fittest individuals in a given population.
def tournament_selection(population, number):

    population.sort(key=lambda x: x.fitness)
    fittest = population[0:number]
    return fittest

# Define ordered crossover function.
# Apply ordered cross (OX) on a genome and return the newly generated genome.
def ordered_crossover(parent_1, parent_2, crossover_start, crossover_end):

    p1_path = list(parent_1.path[0:len(parent_1.path) - 1])
    p2_path = list(parent_2.path[0:len(parent_2.path) - 1])
    offspring = []

    for i in range(len(p1_path)):
        offspring.extend("x")

    offspring[crossover_start:crossover_end] = p1_path[crossover_start:crossover_end]

    i = crossover_end
    j = 0

    while 'x' in offspring:

        if i < len(p2_path):
            if p2_path[i] not in offspring and j < len(offspring):
                offspring[j] = p2_path[i]
                j += 1
            i += 1
        else:
            i = 0

    offspring.extend(offspring[0])
    path = "".join(offspring)
    new_genome = genome(path, fitness(path))
    return new_genome

# Define Mutatuion Function.
# Apply mutation by replacing a random order of cities and return the newly generated genome.
def mutation(chromosome):

    offspring = []
    possible_postions = []
    for i in range(len(chromosome.path) - 1):
        offspring.extend(chromosome.path[i])

    for i in range(len(offspring)):
        possible_postions.append(i)

    for i in range(mutation_rate):

        position_1, position_2 = random.sample(possible_postions, 2)
        temp = offspring[position_1]
        offspring[position_1] = offspring[position_2]
        offspring[position_2] = temp

    offspring.extend(offspring[0])
    path = "".join(offspring)
    new_offspring = genome(path, fitness(path))
    return new_offspring

# Calculate the total score of the population by adding all of their fitness scores.
def total_population_score(population):

    score = 0

    for individual in population:
        score += individual.fitness

    return score

# Function to generate a random path
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

# Function to initialize a random population
def initialize_population(population_size, cities):
    population = []
    
    for i in range(population_size):
        path = generate_path(cities)
        individual = genome(path, fitness(path))
        population.append(individual)
        
    return population

# Main Function
def main():
    
    # Initialize a population
    
    population = initialize_population(population_size, cities)

    score = total_population_score(population)

    generations = 1

    # Apply genetic algorithm until a maximum number of generations is reached or the poplation score is not less than threshhold.
    while (generations <= total_generations) and (score > threshhold):

        print("\n\nGeneration: ", generations)
        print("Score: ", score)

        fittest = tournament_selection(population, selection_pressure)

        # Print fittest individuals after selection.
        print("\nFittest:\nPATH\t\tFITNESS")
        for i in fittest:
            print(i.path,"\t",i.fitness)

        new_generation = []
        possible_parents = []
        for i in range(len(fittest)):
            possible_parents.append(i)

        for i in range(population_size-len(fittest)):

            parent_1, parent_2 = random.sample(possible_parents, 2)
            new_offspring = ordered_crossover(
                fittest[parent_1], fittest[parent_2], 2, 5)
            mutated_new_offspring = mutation(new_offspring)
            new_generation.append(mutated_new_offspring)

        for i in range(len(fittest)):
            mutated_new_offspring = mutation(fittest[i])
            new_generation.append(fittest[i])
            
        # Print the new generation.
        print("\nNew Generation:\nPATH\t\tFITNESS")
        for i in new_generation:
            print(i.path,"\t",i.fitness)

        population = new_generation
        score = total_population_score(population)
        generations += 1

    # Print the shorted distance found by the genetic algorithm.
    print("Shortest Distance Found:", fittest[0].path, fittest[0].fitness)


if __name__ == "__main__":
    main()
