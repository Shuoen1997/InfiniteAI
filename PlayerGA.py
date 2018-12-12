import random
from checks import *
from behaviors import *
# def is_obstacle_in_way():
#     print("in obstacle in way")
#     return True

# def move_forward():
#     print("Moving forward")

# def move_random_vert():
#     print("Moving to random vertical")
map_height = 20
map_width = 240


# GENES = [(is_obstacle_in_way, stay), (is_obstacle_in_way, move_random_vert)]
GENES = [(is_obstacle_in_way, move_random_vert), (is_obstacle_in_way, move_alittle)]

G_LENGTH = 1

POPULATION_SIZE = 20

class Individual(object):

    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()

    @classmethod
    def mutated_genes(self):
        gene = random.choice(GENES)
        return gene

    @classmethod
    def create_gnome(self):
        return [self.mutated_genes() for _ in range(G_LENGTH)]

    def mate(self, par2):
        # chromosome for offspring
        child_chromosome = []
        for gp1, gp2 in zip(self.chromosome, par2.chromosome):

            # random probability
            prob = random.random()

            # if prob is less than 0.45, insert gene
            # from parent 1
            if prob < 0.45:
                child_chromosome.append(gp1)

                # if prob is between 0.45 and 0.90, insert
            # gene from parent 2
            elif prob < 0.90:
                child_chromosome.append(gp2)

                # otherwise insert random gene(mutate),
            # for maintaining diversity
            else:
                child_chromosome.append(self.mutated_genes())

                # create new Individual(offspring) using
        # generated chromosome for offspring
        return Individual(child_chromosome)

    def cal_fitness(self):
        fitness = 0
        return fitness

    # Driver code


def main():
    global POPULATION_SIZE

    # current generation
    generation = 1

    found = False
    population = []

    # create initial population
    for _ in range(POPULATION_SIZE):
        gnome = Individual.create_gnome()
        population.append(Individual(gnome))

    while not found:

        # sort the population in increasing order of fitness score
        population = sorted(population, key=lambda x: x.fitness)

        # if the individual having lowest fitness score ie.
        # 0 then we know that we have reached to the target
        # and break the loop
        if population[0].fitness <= 0:
            found = True
            break

        # Otherwise generate new offsprings for new generation
        new_generation = []

        # Perform Elitism, that mean 10% of fittest population
        # goes to the next generation
        s = int((10 * POPULATION_SIZE) / 100)
        new_generation.extend(population[:s])

        # From 50% of fittest population, Individuals
        # will mate to produce offspring
        s = int((90 * POPULATION_SIZE) / 100)
        for _ in range(s):
            parent1 = random.choice(population[:50])
            parent2 = random.choice(population[:50])
            child = parent1.mate(parent2)
            new_generation.append(child)

        population = new_generation


        generation += 1

    item = population[0].chromosome
    print(item)


if __name__ == '__main__':
    main()
