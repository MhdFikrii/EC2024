import random
import streamlit as st

def genetic_algorithm(target, mutation_rate=0.1):
    # Convert the target string into a list of characters
    target_chars = list(target)
    # Initialize population as a random string of the same length as the target
    population = [''.join(random.choice(target_chars) for _ in range(len(target_chars)))]
    generation = 0
    
    # Calculate fitness: number of characters that are not in the target position
    def calculate_fitness(population):
        return sum(1 for i, j in zip(target_chars, population[0]) if i != j)

    fitness = calculate_fitness(population)

    while fitness != 0:
        new_population = []
        for _ in range(len(population)):
            # Create a new individual based on mutation
            if random.random() < mutation_rate:
                gene = ''.join(random.choice(target_chars) for _ in range(len(target_chars)))
            else:
                gene = population[0]  # No mutation, keep the same individual
            new_population.append(gene)

        population = new_population
        fitness = calculate_fitness(population)
        generation += 1

        # Show the current state of evolution
        yield {
            "string": population[0],
            "generation": generation,
            "fitness": fitness
        }

    return population[0]

# Streamlit App Layout
st.title("Genetic Algorithm")

# Input fields for name and mutation rate
name = st.text_input("Enter your name", "")
if 'mutation_rate' not in st.session_state:
    st.session_state.mutation_rate = 0.1  # Default mutation rate

# Display the current mutation rate
st.write(f"Current Mutation Rate: {st.session_state.mutation_rate:.2f}")

# Plus and Minus buttons to adjust the mutation rate
col1, col2 = st.columns(2)
if col1.button("+ Increase Mutation Rate"):
    st.session_state.mutation_rate = min(st.session_state.mutation_rate + 0.01, 1.0)  # Cap at 1.0
if col2.button("- Decrease Mutation Rate"):
    st.session_state.mutation_rate = max(st.session_state.mutation_rate - 0.01, 0.0)  # Cap at 0.0

# Button to start the genetic algorithm
if st.button("Calculate"):
    # Run the genetic algorithm with the given name as target
    target = name
    st.write(f"Target string: {target}")

    # Display evolution of the genetic algorithm
    results = []
    for step in genetic_algorithm(target, mutation_rate=st.session_state.mutation_rate):
        results.append(step)
        st.write(f"String: {step['string']} | Generation: {step['generation']} | Fitness: {step['fitness']}")
        
        # Stop if the target is found
        if step["fitness"] == 0:
            st.success("Target found!")
            break

# To run the app, execute this command in the terminal
# streamlit run app.py

# Git commands for version control
# git add .
# git commit -m "Add genetic algorithm and Streamlit interface"
# git push origin main
