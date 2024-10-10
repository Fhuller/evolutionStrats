import numpy as np

# A função Sphere (ou função Parabolic Ridge) é um dos benchmarks mais comuns usados na pesquisa de algoritmos evolutivos.
# Ela tem uma estrutura simples, o que a torna ideal para testar e demonstrar o comportamento das estratégias evolutivas.
# Veja a seguir como ela se conecta ao (1+1)-ES:

def sphere_function(x):
    return sum(x_i ** 2 for x_i in x)

# Evolution Strategy (1+1) algorithm
def evolution_strategy_1_plus_1(dimensions, max_generations, mutation_strength):
    # Começa com uma solução aleatória
    parent = np.random.uniform(-5.0, 5.0, dimensions)
    parent_fitness = sphere_function(parent)

    for generation in range(max_generations):
        # Faz a mutação
        offspring = parent + np.random.normal(0, mutation_strength, dimensions)
        offspring_fitness = sphere_function(offspring)

        # Seleciona a melhor solução
        if offspring_fitness < parent_fitness:
            parent, parent_fitness = offspring, offspring_fitness

        # Opcional, a cada 10 gerações vai mostrar um print
        if generation % 10 == 0:
            print(f"Generation {generation}: Best fitness = {parent_fitness}")

    return parent, parent_fitness

# Roda o algoritmo
best_solution, best_fitness = evolution_strategy_1_plus_1(dimensions=5, max_generations=100, mutation_strength=0.1)

print("\nBest solution found:", best_solution)
print("Best fitness:", best_fitness)

import random