import random
import statistics
import streamlit as st

st.title("🧬 Simulatore Genetico Altezza")

# Funzione per calcolare l'effetto genetico
def genotype_effect(genotype):
    if genotype[0] == genotype[1]:
        return 5 + random.normalvariate(0, 2) if genotype[0].isupper() else random.normalvariate(0, 2)
    else:
        return 2.5 + random.normalvariate(0, 2)

def calculate_height(genotypes, base_height=150):
    return base_height + sum(genotype_effect(gen) for gen in genotypes)

def generate_progeny(parent1, parent2, n=100):
    return [
        calculate_height([
            ''.join(sorted([random.choice(g1), random.choice(g2)]))
            for g1, g2 in zip(parent1, parent2)
        ])
        for _ in range(n)
    ]

def simulate_extreme_height(parent, simulations=100, mode='max'):
    heights = [calculate_height(parent) for _ in range(simulations)]
    return max(heights) if mode == 'max' else min(heights)

# Definizione genotipi parentali
high_parents = (["Aa", "BB", "CC", "Dd", "Ee", "FF"], ["AA", "BB", "Cc", "dd", "Ee", "Ff"])
low_parents = (["Aa", "BB", "CC", "Dd", "Ee", "FF"], ["AA", "BB", "Cc", "dd", "Ee", "Ff"])

# Calcolo altezze parentali estreme
high_p1 = simulate_extreme_height(high_parents[0], mode='max')
high_p2 = simulate_extreme_height(high_parents[1], mode='max')
low_p1 = simulate_extreme_height(low_parents[0], mode='min')
low_p2 = simulate_extreme_height(low_parents[1], mode='min')

# Generazione progenie
high_progeny = generate_progeny(*high_parents)
low_progeny = generate_progeny(*low_parents)

# Statistiche progenie
def summary(heights):
    return statistics.mean(heights), min(heights), max(heights)

high_mean, high_min, high_max = summary(high_progeny)
low_mean, low_min, low_max = summary(low_progeny)

# Output su Streamlit
st.subheader("📊 Coppia 'alti'")
st.write(f"👤 Genitore 1 (max simulato): **{high_p1:.2f} cm**")
st.write(f"👤 Genitore 2 (max simulato): **{high_p2:.2f} cm**")
st.write(f"👶 Progenie (n=100): **media = {high_mean:.2f} cm**, min = {high_min:.2f}, max = {high_max:.2f}")

st.subheader("📉 Coppia 'bassi'")
st.write(f"👤 Genitore 1 (min simulato): **{low_p1:.2f} cm**")
st.write(f"👤 Genitore 2 (min simulato): **{low_p2:.2f} cm**")
st.write(f"👶 Progenie (n=100): **media = {low_mean:.2f} cm**, min = {low_min:.2f}, max = {low_max:.2f}")
