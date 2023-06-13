from pathlib import Path
from utils import *
from genetic_algorithm import *


if __name__ == "__main__":
	
	missions_nb, centers_nb = prompt_instance_parameters()

	instance_path = Path(f"src/instances/{missions_nb}Missions-{centers_nb}centres/")

	employees = open_employees_csv(instance_path)
	missions = open_missions_csv(instance_path)
	centers = open_centers_csv(instance_path)
	distance_matrix = open_distances_matrix(instance_path)

	size, crossover_rate, mutation_rate, max_execution_time, k, mutated_genes_per_chromosome_rate = prompt_genetic_algorithm_parameters(100, .7, .8, 120, 5, .025)

	solution = genetic_algorithm(employees, missions, centers, distance_matrix, size, crossover_rate, mutation_rate, max_execution_time, k, mutated_genes_per_chromosome_rate)

	print("\nSolution:")

	#print_solution_assignments(solution, missions, employees)

	print_solution_evaluation(solution.evaluate(distance_matrix, employees, missions, len(centers)))
	