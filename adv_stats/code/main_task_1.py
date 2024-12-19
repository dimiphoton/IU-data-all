from code.data.parameters import XI_2, task_1_threshold
from code.task_1.calculations import calculate_poisson_probabilities, calculate_poisson_median
from code.task_1.vizs import generate_and_save_poisson_graph

# Graph parameters


probabilities = calculate_poisson_probabilities(lambda_=XI_2,threshold=task_1_threshold)
distribution_params = {"lambda_": XI_2}


# Generate the graph
generate_and_save_poisson_graph(probabilities,lambda_=XI_2,expected_value=XI_2,median=calculate_poisson_median(XI_2))
