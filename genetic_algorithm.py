import streamlit as st
import random

# Set up Streamlit page configuration
st.set_page_config(page_title="Genetic Algorithm")
st.header("Genetic Algorithm", divider="gray")

# Constants
POP_SIZE = 500  # Number of Chromosomes in our list.
TARGET = 'fikri'  # Our goal.
GENES = ' abcdefghijklmnopqrstuvwxyz'  # Options for population creation

# Function to initialize population
def initialize_pop(TARGET):
    population = []
    tar_len = len(TARGET)

    for _ in range(POP_SIZE):
        temp = [random.choice(GENES) for _ in range(tar_len)]
        population.append(temp)

    return population

# Fitness calculation
def fitness_cal(TARGET, chromo_from_pop):
    difference = sum(1 for tar_char, chromo_char in zip(TARGET, chromo_from_pop) if tar_char != chromo_char)
    return [chromo_from_pop, difference]

# Selection function
def selection(population, TARGET):
    sorted_chromo_pop = sorted(population, key=lambda x: x[1])
    return sorted_chromo_pop[:int(0.5 * POP_SIZE)]

# Crossover function
def crossover(selected_chromo, CHROMO_LEN, population):
    offspring_cross = []
    for _ in range(int(POP_SIZE)):
        parent1 = random.choice(selected_chromo)
        parent2 = random.choice(population[:int(POP_SIZE * 0.5)])
        p1 = parent1[0]
        p2 = parent2[0]
        crossover_point = random.randint(1, CHROMO_LEN - 1)
        child = p1[:crossover_point] + p2[crossover_point:]
        offspring_cross.append(child)
    return offspring_cross

# Mutation function
def mutate(offspring, MUT_RATE):
    mutated_offspring = []
    for arr in offspring:
        for i in range(len(arr)):
            if random.random() < MUT_RATE:
                arr[i] = random.choice(GENES)
        mutated_offspring.append(arr)
    return mutated_offspring

# Replacement function
def replace(new_gen, population):
    for i in range(len(population)):
        if population[i][1] > new_gen[i][1]:
            population[i][0] = new_gen[i][0]
            population[i][1] = new_gen[i][1]
    return population

# Main function
def main(POP_SIZE, MUT_RATE, TARGET, GENES):
    initial_population = initialize_pop(TARGET)
    found = False
    population = []
    generation = 1

    # Calculate the fitness for the initial population
    for chromo in initial_population:
        population.append(fitness_cal(TARGET, chromo))

    # Loop until the target is found
    while not found:
        selected = selection(population, TARGET)
        population = sorted(population, key=lambda x: x[1])
        crossovered = crossover(selected, len(TARGET), population)
        mutated = mutate(crossovered, MUT_RATE)

        new_gen = [fitness_cal(TARGET, child) for child in mutated]
        population = replace(new_gen, population)

        if population[0][1] == 0:
            st.write('Target found')
            st.write(f'String: {population[0][0]} | Generation: {generation} | Fitness: {population[0][1]}')
            found = True
        else:
            st.write(f'String: {population[0][0]} | Generation: {generation} | Fitness: {population[0][1]}')
            generation += 1

# Streamlit input for mutation rate
if 'mutation_rate' not in st.session_state:
    st.session_state.mutation_rate = 0.2  # Default mutation rate

# Input field for custom mutation rate
custom_mutation_rate = st.number_input("Enter your mutation rate (0.0 - 1.0)", 
                                        value=st.session_state.mutation_rate, 
                                        min_value=0.0, max_value=1.0, 
                                        step=0.01)

# Update session state with the custom mutation rate
st.session_state.mutation_rate = custom_mutation_rate

# Button to start the genetic algorithm
if st.button("Run Genetic Algorithm"):
    main(POP_SIZE, st.session_state.mutation_rate, TARGET, GENES)

# To run the app, execute this command in the terminal
# streamlit run app.py

# Git commands for version control
# git add .
# git commit -m "Combine genetic algorithm logic with user input for mutation rate"
# git push origin main
