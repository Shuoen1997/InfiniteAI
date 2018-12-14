import random 
from level_fitness import *

map_height = 20
map_width = 200
POPULATION_SIZE = 10

class Individual(object):
    
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = self.cal_fitness()
        self.passRate = 0
    
    def cal_fitness(self):
        return metrices(self.chromosome)

    #Generate a random gene at a location
    @classmethod
    def mutate_genes(self):
        pass

    #Select from parent 1 or 2
    def mate(self, par2):
        print(self)
        print(par2)

    @classmethod
    def init_level(self):
        levels = [[" " for col in range(map_width)] for row in range(map_height)]
        levels[map_height-1][:] = "-" * map_width
        levels[0][:] = "-" * map_width
        transform_levels(self.chromosome, levels)
        #print(ge)
        return levels

def generate_obstacles(self):
    print("Got here")
    elt_num = random.randint(20, 100)
    ge = [
        random.choice([("1_lo_wall", random.randint(1, 4), random.randint(5, 8), random.randint(10, map_width - 5)),
                        ("2_hi_wall", random.randint(1, 4), random.randint(5, 8), random.randint(10, map_width - 5)),
                        ("3_lo_short_wall", random.randint(1, 4), random.randint(2, 5),
                         random.randint(10, map_width - 5)),
                        ("4_hi_short_wall", random.randint(1, 4), random.randint(2, 5),
                         random.randint(10, map_width - 5)),
                        ("5_dust", random.randint(1, 3), random.randint(1, 3),
                         (random.randint(1, 16), random.randint(10, map_width - 5)))]) for i in range(elt_num)]
    return ge


def transform_levels(ge, levels):
    #transform the DE into actual array elements
    for item in ge:
        pos = item[3]
        height = item[2]
        width = item[1]
        if item[0][0] in ["1", "3"]:
            for h in range(len(levels)-height, len(levels)-1):
                for w in range(pos, pos+width):
                    levels[h][w] = "x"
        elif item[0][0] in ["2", "4"]:
            for h in range(1, height):
                for w in range(pos, pos+width):
                    levels[h][w] = "x"
        else:
            for h in range( height ):
                for w in range( width ):
                    levels[pos[0] + h][pos[1] + w] = "x"

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
            parent1 = random.choice(population[:5])
            parent2 = random.choice(population[:5])
            child = parent1.mate(parent2)
            new_generation.append(child)

        population = new_generation

        generation += 1

if __name__ == '__main__':
    main()
                   
# def init_designer():
#     #create designer genome, can add more parameters
#     designer_genome = { "ge": [],
#                         "prob_floating_wall": random.randint(1, 20) }
#     for i in range(random.randint(20, 100)):
#         designer_genome["ge"].append(( random.choice(["1_lo_wall", "2_hi_wall"]), random.randint(3, 5), random.randint(7, 14) ) )
#     return designer_genome


# def random_obstacles(items, prob, amount):
#     return random.choices(population=items, weights=prob, k=amount)