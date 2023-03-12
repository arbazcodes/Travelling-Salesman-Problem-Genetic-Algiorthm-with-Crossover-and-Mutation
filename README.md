# Travelling-Salesman-Problem-Genetic-Algiorthm-with-Crossover-and-Mutation

This code implements a genetic algorithm to solve the travelling salesman problem for a given graph. The algorithm works as follows:

*First, a population of random genomes is initialized, where each genome is a random path in the graph.
*Then, the fitness of each genome is calculated as the total distance travelled on the path.
*The genetic algorithm is then applied to the population for a number of generations.
*In each generation, the fittest individuals are selected using tournament selection.
*Then, crossover is applied to the selected individuals to create new offspring.
*Finally, mutation is applied to the offspring with a given mutation rate.
*The new offspring replace the weakest individuals in the population.
*This process is repeated for a number of generations until a stopping criterion is reached (in this case, a maximum number of generations is defined).
*The fittest individual in the final population is returned as the solution to the travelling salesman problem.

The code defines several functions to implement the genetic algorithm, including:

*fitness(): a function to calculate the fitness of a given genome (i.e. the total distance travelled on the path).
*select_population(): a function to select a random sample of individuals from a given population.
*tournament_selection(): a function to select the fittest individuals from a given population using tournament selection.
*ordered_crossover(): a function to apply ordered crossover to two parent genomes and generate new offspring.
*mutation(): a function to apply mutation to a given genome.
*total_population_score(): a function to calculate the total score of a given population (i.e. the sum of all the fitness scores of the individuals in the population).
*generate_path(): a function to generate a random path in the graph.
*initialize_population(): a function to initialize a random population of given size.
