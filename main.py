"""
This code implements a genetic algorithm to solve the travelling salesman problem for a given graph. The algorithm works as follows:

*First, a population of random genomes is initialized, where each genome is a random path in the graph.

*Then, the fitness of each genome is calculated as the total distance travelled on the path.

*The genetic algorithm is then applied to the population for a number of generations.

*In each generation, the fittest individuals are selected using tournament selection.

*Then, crossover is applied to the selected individuals to create new offspring.

*Finally, mutation is applied to the offspring with a given mutation rate.

*The new offspring replace the weakest individuals in the population.

*This process is repeated for a number of generations until a stopping criterion is reached 
 (in this case, a maximum number of generations is defined).

*The fittest individual in the final population is returned as the solution to the travelling salesman problem.

The code defines several functions to implement the genetic algorithm, including:

*fitness(): a function to calculate the fitness of a given genome (i.e. the total distance travelled on the path).

*select_population(): a function to select a random sample of individuals from a given population.

*tournament_selection(): a function to select the fittest individuals from a given population using tournament selection.

*ordered_crossover(): a function to apply ordered crossover to two parent genomes and generate new offspring.

*mutation(): a function to apply mutation to a given genome.

*total_population_score(): a function to calculate the total score of a given population 
 (i.e. the sum of all the fitness scores of the individuals in the population).

*generate_path(): a function to generate a random path in the graph.

*initialize_population(): a function to initialize a random population of given size.
"""


from random import randint
import random

max = 1000


# Initialize Parameters.

population_size = 100
maximum_generations = 10
mutation_rate = 1
selection_pressure = 5
convergance_rate = 96
threshhold = population_size * max * (convergance_rate/100)


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

        # if there is no path between the two cities return max, else add it to the total distance travelled.
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
# Return a certain number of fittest individuals in a given population.

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

    return float(score)


# Function to generate a random path.

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


# Function to initialize a random population.

def initialize_population(population_size, cities):
    population = []

    for i in range(population_size):
        path = generate_path(cities)
        individual = genome(path, fitness(path))
        population.append(individual)

    return population


# Main Function

def main():

    # Initialize a population.

    population = initialize_population(population_size, cities)

    score = total_population_score(population)

    generations = 1
    
    fittest = []

    # Apply genetic algorithm until a maximum number of generations is reached or the population score is greater than threshhold.
    while True:
        
        print("\n\nGeneration: ", generations)
        print("Score: ", score)

        fittest_genomes = tournament_selection(population, selection_pressure)

        # Print Fittest Genomes after selection.
        print("\nFittest Genomes:\nPATH\t\tFITNESS")
        for i in fittest_genomes:
            print(i.path, "\t", i.fitness)

        new_generation = []
        possible_parents = []

        for i in range(len(fittest_genomes)):
            possible_parents.append(i)

        for i in range(population_size-len(fittest_genomes)):

            parent_1, parent_2 = random.sample(possible_parents, 2)
            new_offspring = ordered_crossover(
                fittest_genomes[parent_1], fittest_genomes[parent_2], 2, 5)
            mutated_new_offspring = mutation(new_offspring)
            new_generation.append(mutated_new_offspring)

        for i in range(len(fittest_genomes)):
            mutated_new_offspring = mutation(fittest_genomes[i])
            new_generation.append(mutated_new_offspring)

        # Print the new generation.
        print("\nNew Generation:\nPATH\t\tFITNESS")
        for i in new_generation:
            print(i.path, "\t", i.fitness)
            
        # Stopping Criterion.
        if(score <= threshhold or generations == maximum_generations):
            
            # Print the generation number and the shorted distance found by the genetic algorithm.
            print("\n\nGeneration: ",generations,"/",maximum_generations)
            fittest_genomes.sort(key=lambda x: x.fitness)
            print("Shortest Distance Found:", fittest_genomes[0].path, fittest_genomes[0].fitness)
            break
        
        population = new_generation
        score = total_population_score(population)
        generations += 1

    


if __name__ == "__main__":
    main()
