from random import randint
import random

#graph
mutation_rate = 3
total_cities = 6
population_size = 10
total_generations = 10
max = 1000

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
        
        if graph[position[genome[i]]][position[genome[i+1]]] == max:
            
            return max
        
        else: 
            
            total_distance += graph[position[genome[i]]][position[genome[i+1]]]
        
    return total_distance



def select_population(population, number): 
    
    selected = []

    while (len(selected) < number):

        value = randint(0, len(population)-1)
        
        if population[value] not in selected:

            selected.append(population[value])
        
    return selected



def tournament_selection(population, number):
             
    population.sort( key=lambda x: x.fitness)
    fittest = population[0:number]                                
    return fittest


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
            if  p2_path[i] not in offspring and j < len(offspring):
                offspring[j] = p2_path[i]
                j += 1
            i += 1
        else:
            i = 0
            
    offspring.extend(offspring[0])
    path = "".join(offspring)
    new_genome = genome(path, fitness(path))
    return new_genome

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


def total_population_score(population):
    
    score = 0
    
    for individual in population:
        score += individual.fitness
        
    return score
     
                
def main():
    
    g1 = genome("PISKLMP", 0)
    g2 = genome("IPMLKSI", 0)
    g3 = genome("KSILMPK", 0)
    g4 = genome("LISKPML", 0)
    g5 = genome("SILKPMS", 0)
    g6 = genome("SKLMPIS", 0)
    g7 = genome("MLKSIPM", 0)
    g8 = genome("ILMPKSI", 0)
    g9 = genome("LISKPML", 0)
    g10 =genome("MLKPISM", 0)
    
    genomes = [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10]
    
    population = []
    
    for i in genomes:    
        i.fitness = fitness(i.path)
        population.append(i)
 
    score = total_population_score(population)
    
    generations = 1
    
    while (generations <= total_generations) and (score > 600):
    
        print("Generation: ", generations)
        print("Score: ", score)
    
        fittest = tournament_selection(population, 5)
        
        for i in fittest:
            print("Fittest\n", i.path, i.fitness)
                       
        new_generation = []
        possible_parents = []
        for i in range(len(fittest)):
            possible_parents.append(i)
        
        for i in range(population_size-len(fittest)):
            
            parent_1, parent_2 = random.sample(possible_parents, 2)
            new_offspring = ordered_crossover(fittest[parent_1], fittest[parent_2], 2, 5)
            mutated_new_offspring = mutation(new_offspring)
            new_generation.append(mutated_new_offspring)
            
        for i in range(len(fittest)):
            mutated_new_offspring = mutation(fittest[i])
            new_generation.append(fittest[i])

        for i in new_generation:
            print("New Generation\n", i.path, i.fitness)
            
        population = new_generation
        score = total_population_score(population)
        generations += 1

    print("Shortest Distance Found:", fittest[0].path, fittest[0].fitness)

        
if __name__ == "__main__":
    main()