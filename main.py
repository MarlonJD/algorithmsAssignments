import numpy as np
import timeit
from scipy.optimize import linear_sum_assignment
import geneticalgorithm as ga
from simanneal import Annealer
import random
import matplotlib.pyplot as plt
import os
import  io
from memory_profiler import profile

# Örnek Veri
cost_matrix = np.random.randint(1, 10, (1000, 1000))

@profile
def run_hungarian_method():
    global cost_matrix  # Global değişkeni kullan
    # Eğer matris kare değilse, kareye çevir
    if cost_matrix.shape[0] != cost_matrix.shape[1]:
        num_jobs, num_machines = cost_matrix.shape
        max_dim = max(num_jobs, num_machines)
        cost_matrix = np.pad(cost_matrix, ((0, max_dim - num_jobs), (0, max_dim - num_machines)), 'constant')
    row_ind, col_ind = linear_sum_assignment(cost_matrix)
    print("Optimal Atamalar (Hungarian):")
    # tek dizide sonucu göster
    print(col_ind)
    print("Toplam Maliyet (Hungarian):", cost_matrix[row_ind, col_ind].sum())
    return cost_matrix[row_ind, col_ind].sum()

@profile
def run_annealer():
    num_jobs, num_machines = cost_matrix.shape

    class AssignmentProblem(Annealer):

        def __init__(self, state, cost_matrix):
            self.cost_matrix = cost_matrix
            super(AssignmentProblem, self).__init__(state)

        def move(self):
            """Rastgele iki işin yerini değiştirir."""
            a = random.randint(0, len(self.state) - 1)
            b = random.randint(0, len(self.state) - 1)
            self.state[a], self.state[b] = self.state[b], self.state[a]

        def energy(self):
            """Toplam maliyeti döndürür."""
            e = 0
            for i in range(len(self.state)):
                e += self.cost_matrix[i][self.state[i]]
            return e

    # initial state
    init_state = list(range(num_jobs))

    ap = AssignmentProblem(init_state, cost_matrix)
    # ap.set_schedule(ap.auto(minutes=1)) # set approximate time to find solution
    best_state, best_cost = ap.anneal()
    
    print("\n\nOptimal Atamalar (Annealer):", best_state)
    print("Toplam Maliyet (Annealer): ", best_cost)

@profile
def run_genetic_algorithm():
    num_jobs, num_machines = cost_matrix.shape

    def objective_function(assignments):
        total_cost = 0
        for i in range(num_jobs):
            total_cost += cost_matrix[i, int(assignments[i])]
        return total_cost

    algorithm_param = {
        'max_num_iteration': 1000,
        'population_size': 20,
        'mutation_probability': 0.1,
        'elit_ratio': 0.01,
        'crossover_probability': 0.5,
        'crossover_type': 'uniform',
        'max_iteration_without_improv': None,
        'parents_portion': 0.3,
        'verbose': False,
    }

    model = ga.geneticalgorithm(
        convergence_curve=False,
        function=objective_function,
        dimension=num_jobs,
        variable_type='int',
        variable_boundaries=np.array([(0, num_machines - 1)] * num_jobs),  # Fix: Convert variable_boundaries to a numpy array
        algorithm_parameters=algorithm_param,
    )

    model.run()
    
    print("Toplam Maliyet (Genetik):", model.output_dict['function'])
    return model.output_dict['function']

# Memory Profiling
hungarian_method_time = timeit.timeit(run_hungarian_method, number=1)
simulated_annealer_time = timeit.timeit(run_annealer, number=1)
genetic_algorithm_time = timeit.timeit(run_genetic_algorithm, number=1)

print("Zaman Karşılaştırması:")
print("Uygulama\tZaman")
print("Macar Algoritması\t", hungarian_method_time)
print("Simulated Annealer\t", simulated_annealer_time)
print("Genetik Algoritma\t", genetic_algorithm_time)


# plot the hungarian_method_time and simulated_annealer_time line chart

x = ['Hungarian', 'Simulated Annealer', 'Genetic Algorithm']
y = [hungarian_method_time, simulated_annealer_time, genetic_algorithm_time]

print(str(cost_matrix))
plt.title(str(cost_matrix.shape[0]) + "x" + str(cost_matrix.shape[1]) + " Maliyet Matrisi İçin Zaman Karşılaştırması")
plt.bar(x, y)
plt.show()