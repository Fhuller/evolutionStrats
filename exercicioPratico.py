
# Imagine que temos uma lista de números e que nosso objetivo é encontrar o menor número usando um processo simples semelhante ao da evolução.

# Lista de números
numbers = [45, 12, 78, 4, 56, 23, 9, 88, 1, 37]

# Evolution Strategy para encontrar o menor número
def find_smallest_number(numbers, max_attempts):
    # Começa com um número aleatório
    parent = random.choice(numbers)
    print(f"Starting number: {parent}")

    for attempt in range(max_attempts):
        # Escolhe um novo número aleatório
        offspring = random.choice(numbers)
        print(f"Attempt {attempt + 1}: Trying {offspring}")

        # Se o novo for menor, ele sobscreve o pai
        if offspring < parent:
            parent = offspring
            print(f"Novo menor número: {parent}")

    return parent

# Roda o algoritmo
smallest_number = find_smallest_number(numbers, max_attempts=10)

print("\nO menor número encontrado é:", smallest_number)