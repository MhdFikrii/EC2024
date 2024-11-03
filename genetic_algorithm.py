
python -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`

pip install streamlit

import random

def genetic_algorithm(target, mutation_rate=0.1):
    # Convert the target string into a list of characters
    target_chars = list(target)
    population = [random.choice(target_chars) for _ in range(len(target_chars))]
    generation = 0
    fitness = sum(1 for i, j in zip(target_chars, population) if i != j)
    
    while fitness != 0:
        new_population = []
        for gene in population:
            if random.random() < mutation_rate:
                gene = random.choice(target_chars)
            new_population.append(gene)
        
        population = new_population
        fitness = sum(1 for i, j in zip(target_chars, population) if i != j)
        generation += 1

        # Show the current state of evolution
        yield {
            "string": population,
            "generation": generation,
            "fitness": fitness
        }

    return population

import streamlit as st
from genetic_algorithm import genetic_algorithm

# Streamlit App Layout
st.title("Genetic Algorithm")

# Input fields for name and mutation rate
name = st.text_input("Enter your name", "")
mutation_rate = st.slider("Enter your mutation rate", min_value=0.0, max_value=1.0, value=0.1, step=0.01)

# Button to start the genetic algorithm
if st.button("Calculate"):
    # Run the genetic algorithm with the given name as target
    target = list(name)
    st.write(f"Target string: {target}")

    # Display evolution of the genetic algorithm
    for step in genetic_algorithm(target, mutation_rate=mutation_rate):
        st.write(f"String: {step['string']} Generation: {step['generation']} Fitness: {step['fitness']}")
        
        # Stop if the target is found
        if step["fitness"] == 0:
            st.success("Target found!")
            break

streamlit run app.py
git add .
git commit -m "Add genetic algorithm and Streamlit interface"
git push origin main


