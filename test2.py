import random


def mendel(parent1, parent2):

    yellow_round = 0
    yellow_wrinkled = 0
    green_round = 0
    green_wrinkled = 0

    n = 10000 # Sample size
    
    for i in range(n):
        g1 = random.choice(parent1)
        g2 = random.choice(parent2)
        offsprings_genotype = g1 + g2
    
        if 'Y' in offsprings_genotype:
            if 'R' in offsprings_genotype:
                yellow_round += 1
            else:
                yellow_wrinkled += 1
        else:
            if 'R' in offsprings_genotype:
                green_round += 1
            else:
                green_wrinkled += 1
    
    yellow_round_p = (yellow_round/n) * 100
    yellow_wrinkled_p = (yellow_wrinkled/n) * 100
    green_round_p = (green_round/n) * 100
    green_wrinkled_p = (green_wrinkled/n) * 100
    
    return [yellow_round_p, yellow_wrinkled_p, green_round_p, green_wrinkled_p]

if __name__ == "__main__":
    parent1_g1 = ["Y", "R"] #[random.choice(seed_color_alleles), random.choice(seed_texture_alleles)]
    parent1_g2 = ["y", "r"] #[random.choice(seed_color_alleles), random.choice(seed_texture_alleles)]
    
    parent2_g1 = ["Y", "r"] #[random.choice(seed_color_alleles), random.choice(seed_texture_alleles)]
    parent2_g2 = ["y", "r"] #[random.choice(seed_color_alleles), random.choice(seed_texture_alleles)]
    
    parent1 = [parent1_g1, parent1_g2]
    parent2 = [parent2_g1, parent2_g2]
    
    print(mendel(parent1, parent2))
    
