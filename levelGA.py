import random 
from fitness import *

map_height = 20
map_width = 240
class Level(object):
    
    def __init__(self, chromosome):
        self.chromosome = chromosome
        self.fitness = None
    
    def cal_fitness(self, player_pop):
        
        self.fitness = level_metrices(self.init_level(), player_pop)
        return self.fitness
    
    @classmethod
    def create_genome(self):
        
        elt_num = random.randint(20, 100)
        ge = [random.choice([("1_lo_wall", random.randint(1, 4), random.randint(5, 12), random.randint(10, map_width-5)), 
                         ("2_hi_wall", random.randint(1, 4), random.randint(5, 12), random.randint(10, map_width-5)),
                         ("3_lo_short_wall", random.randint(1, 4), random.randint(2, 5), random.randint(10, map_width-5)),
                         ("4_hi_short_wall", random.randint(1, 4), random.randint(2, 5), random.randint(10, map_width-5)),
                         ("5_dust", random.randint(1, 3), random.randint(1, 3), (random.randint(1, 16), random.randint(10, map_width - 5)))]) for i in range(elt_num)]
        return ge
    

    def init_level(self):
        levels = [[" " for col in range(map_width)] for row in range(map_height)]
        levels[map_height-1][:] = "-" * map_width
        levels[0][:] = "-" * map_width
        transform_levels(self.chromosome, levels)
        #print(ge)
        return levels
    

   

    def mate(self, other):
        pa = random.randint(0, len(self.chromosome) - 1)
        pb = random.randint(0, len(other.chromosome) - 1)
        a_part = self.chromosome[:pa] if len(self.chromosome) > 0 else []
        b_part = other.chromosome[pb:] if len(other.chromosome) > 0 else []
        ga = a_part + b_part
        b_part = other.chromosome[:pb] if len(other.chromosome) > 0 else []
        a_part = self.chromosome[pa:] if len(self.chromosome) > 0 else []
        gb = b_part + a_part
        if random.random() > 0.9:
            gb = mutate(gb)
            ga = mutate(ga)
        return random.choice([Level(ga), Level(gb)])





def mutate(genome):
    new_genome = genome[:-1]
    return new_genome


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
                   
# def init_designer():
#     #create designer genome, can add more parameters
#     designer_genome = { "ge": [],
#                         "prob_floating_wall": random.randint(1, 20) }
#     for i in range(random.randint(20, 100)):
#         designer_genome["ge"].append(( random.choice(["1_lo_wall", "2_hi_wall"]), random.randint(3, 5), random.randint(7, 14) ) )
#     return designer_genome


# def random_obstacles(items, prob, amount):
#     return random.choices(population=items, weights=prob, k=amount)