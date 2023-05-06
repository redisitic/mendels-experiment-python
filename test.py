import random

n = 10000 #Samplesize

seed_color_alleles = ["Y", "y"] #Y is Yellow and y is Green
seed_texture_alleles = ["R", "r"] #R is round and r is wrinkled

#Can use random.choice() to randomly select an allele from a list
#For now edit this to change the parents' genotypes
parent1_g1 = ["Y", "R"] #[random.choice(seed_color_alleles), random.choice(seed_texture_alleles)]
parent1_g2 = ["y", "r"] #[random.choice(seed_color_alleles), random.choice(seed_texture_alleles)]

parent2_g1 = ["Y", "r"] #[random.choice(seed_color_alleles), random.choice(seed_texture_alleles)]
parent2_g2 = ["y", "r"] #[random.choice(seed_color_alleles), random.choice(seed_texture_alleles)]

parent1 = [parent1_g1, parent1_g2]
parent2 = [parent2_g1, parent2_g2]

#Uncomment this and comment line(10-17) to get the results of a 2nd Gen Punnett Square.

"""parent1_g1 = ["Y", "R"] 
parent1_g2 = ["y", "r"]
parent1_g3 = ["Y", "r"]
parent1_g4 = ["y", "R"]

parent2_g1 = ["Y", "R"] 
parent2_g2 = ["y", "r"]
parent2_g3 = ["Y", "r"]
parent2_g4 = ["y", "R"]

parent1 = [parent1_g1, parent1_g2, parent1_g3, parent1_g4]
parent2 = [parent2_g1, parent2_g2, parent2_g3, parent2_g4]"""

yellow_round = 0
yellow_wrinkled = 0
green_round = 0
green_wrinkled = 0

offsprings_genotype = []
for i in range(n):
    g1 = random.choice(parent1)
    g2 = random.choice(parent2)
    offsprings_genotype = [g1, g2]
    
    #g1 = Y, R
    if(offsprings_genotype == [['Y', 'R'], ['Y', 'R']]):
        yellow_round += 1
    elif(offsprings_genotype == [['Y', 'R'], ['Y', 'r']]):
        yellow_round += 1
    elif(offsprings_genotype == [['Y', 'R'], ['y', 'R']]):
        yellow_round += 1
    elif(offsprings_genotype == [['Y', 'R'], ['y', 'r']]):
        yellow_round += 1
        
    #g1 = Y, r
    elif(offsprings_genotype == [['Y', 'r'], ['Y', 'R']]):
        yellow_round += 1
    elif(offsprings_genotype == [['Y', 'r'], ['Y', 'r']]):
        yellow_wrinkled += 1
    elif(offsprings_genotype == [['Y', 'r'], ['y', 'R']]):
        yellow_round += 1
    elif(offsprings_genotype == [['Y', 'r'], ['y', 'r']]):
        yellow_wrinkled += 1
    
    #g1 = y, R    
    elif(offsprings_genotype == [['y', 'R'], ['Y', 'R']]):
        yellow_round += 1
    elif(offsprings_genotype == [['y', 'R'], ['Y', 'r']]):
        yellow_round += 1
    elif(offsprings_genotype == [['y', 'R'], ['y', 'R']]):
        green_round += 1
    elif(offsprings_genotype == [['y', 'R'], ['y', 'r']]):
        green_round += 1
        
    #g1 = y, r
    elif(offsprings_genotype == [['y', 'r'], ['Y', 'R']]):
        yellow_round += 1
    elif(offsprings_genotype == [['y', 'r'], ['Y', 'r']]):
        yellow_wrinkled += 1
    elif(offsprings_genotype == [['y', 'r'], ['y', 'R']]):
        green_round += 1
    elif(offsprings_genotype == [['y', 'r'], ['y', 'r']]):
        green_wrinkled += 1
        
yellow_round_p = (yellow_round/n) * 100
yellow_wrinkled_p = (yellow_wrinkled/n) * 100
green_round_p = (green_round/n) * 100
green_wrinkled_p = (green_wrinkled/n) * 100

print("Yellow Round Percentage: ", yellow_round_p, "%")
print("Yellow Wrinkled Percentage: ", yellow_wrinkled_p, "%")
print("Green Round Percentage: ", green_round_p, "%")
print("Green Wrinkled Percentage: ", green_wrinkled_p, "%")
