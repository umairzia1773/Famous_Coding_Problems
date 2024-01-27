import random as r

cities = {               #city and coordinates
    'A': (0, 0),
    'B': (1, 3),
    'C': (4, 7),
    'D': (5, 8),
    'E': (2, 6)
}

def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

def initial_population(pop_size, cities):          #generating initial list of cities randomly
    population = []
    city_list = list(cities.keys())
    for i in range(pop_size):
        population.append(r.sample(city_list, len(city_list)))
    return population


def total_distance(route):
    dist = 0
    for i in range(len(route) - 1):
        dist += distance(route[i], route[i + 1])
    dist += distance(route[-1], route[0])
    return dist


def crossover(parent1, parent2):
    start = r.randint(0, len(parent1) - 1)
    end = r.randint(start, len(parent1))
    temp = parent1[start:end] #holding segment of cities
    child = [-1] * len(parent1) #placeholder, -1 list
    child[start:end] = temp

    index = end
    for city in parent2:
        #If a city in parent2 is not present in the temp segment copied 
        # from parent1, # it is added to the child route
        if city not in temp:  
            child[index % len(parent1)] = city
            index += 1
    return child

def Mutation(route):
    m1, m2 = r.sample(range(len(route)), 2)
    route[m1], route[m2] = route[m2], route[m1]
    return route

def genetic_algorithm(population, generations, mutation_rate):
    for generation in range(generations):
        new_population = []
        for i in range(len(population)):
            parent1 = r.choice(population)
            parent2 = r.choice(population)
            child = crossover(parent1, parent2)
            if r.random() < mutation_rate:
                child = Mutation(child)
            new_population.append(child)
        population = new_population

    best_route = min(population, key=total_distance)
    return best_route

def main():
    population_size = 200
    generations = 1000
    mutation_rate = 0.2
    initial_pop = initial_population(population_size, cities)
    best_solution = genetic_algorithm(initial_pop, generations, mutation_rate)

    print("Best Route:", best_solution)
    print("Total Distance:", total_distance(best_solution))

main()
