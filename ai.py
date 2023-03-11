from random import randint
import random

#graph

cities = {"P": "Peshawar",
          "I": "Islamabad",
          "S": "Sialkot",
          "K": "Karachi",
          "L": "Lahore",
          "M": "Multan"}

total_cities = 6

position = {"P": 0,
            "I": 1,
            "S": 2,
            "K": 3,
            "L": 4,
            "M": 5}
                              
graph = [[0, 20, float('inf'), 250, float('inf'), 100], 
         [20, 0, 30, float('inf'), 40, float('inf')], 
         [float('inf'), 30, 0, 200, float('inf'), float('inf')], 
         [250, float('inf'), 200, 0, 180, float('inf')],
         [float('inf'), 40, float('inf'), 180, 0, 90],
         [100, float('inf'), float('inf'), float('inf'), 90, 0]]

mutation_rate = 3

class genome:
  def __init__(self, _path, _fitness):
    self.path = _path
    self.fitness = _fitness

def fitness(genome):
    
    total_distance = 0
    
    for i in range(len(genome)-1):
        
        if graph[position[genome[i]]][position[genome[i+1]]] == float('inf'):
            
            return float('inf')
        
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
    return population[0:number] 


def crossover(offspring, i, j, path):

    while 'x' in offspring:
    
        if i < len(path):
            if  path[i] not in offspring and j < len(offspring):
                offspring[j] = path[i]
                j += 1
            i += 1
        else:
            i = 0
            
    offspring.extend(offspring[0])
    path = "".join(offspring)
    
    return path

def ordered_crossover(parent_1, parent_2, crossover_start, crossover_end):
    
    p1_path = list(parent_1.path[0:len(parent_1.path) - 1])
    p2_path = list(parent_2.path[0:len(parent_1.path) - 1])
    offspring_1 = []
    offspring_2 = []
    
    
    for i in range(len(p1_path)):
        offspring_1.extend("x")
        offspring_2.extend("x")
    
    offspring_1[crossover_start:crossover_end] = p1_path[crossover_start:crossover_end]
    offspring_2[crossover_start:crossover_end] = p2_path[crossover_start:crossover_end]
     
    i = crossover_end
    j = 0
    while 'x' in offspring_1:
    
        if i < len(p2_path):
            if  p2_path[i] not in offspring_1 and j < len(offspring_1):
                offspring_1[j] = p2_path[i]
                j += 1
            i += 1
        else:
            i = 0
            
    offspring_1.extend(offspring_1[0])
    path = "".join(offspring_1)
    return offspring_1

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
    
    path = "".join(offspring) 
        
    new_offspring = genome(path + path[0], fitness(path)) 
    return new_offspring
     
                
def main():
    g1 = genome("PISKLMP", 0)
    g2 = genome("LISKPML", 0)
    g3 = genome("ILMPKSI", 0)
    g4 = genome("KPMLISK", 0)
    g5 = genome("SIPMLKS", 0)

    initial_population = []

    genomes = [g1, g2, g3, g4, g5]

    for i in genomes:    
        
        i.fitness = fitness(i.path)
        
        initial_population.append(i)
        
    selected = tournament_selection(initial_population, 3)

    for i in range(3):    
        
        print(selected[i].path , selected[i].fitness)
        
     
    new_genome = ordered_crossover(initial_population[0], initial_population[1], 2, 5)
    
    print (new_genome)
    
    mutated_offspring = mutation(initial_population[0])
    
    print(mutated_offspring.path)
        
if __name__ == "__main__":
    main()