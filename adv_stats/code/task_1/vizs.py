import matplotlib.pyplot as plt
import numpy as np


def generate_and_save_poisson_graph(probabilities, expected_value, median,lambda_):
    """
    Generate and save the graph for the Poisson distribution.

    Args:
        probabilities: A NumPy array containing the probabilities.
        lambda_: The lambda parameter of the Poisson distribution.
        expected_value: The expected value of the Poisson distribution.
        median: The median of the Poisson distribution.
    """
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(np.arange(len(probabilities)), probabilities)

    ax.set_xlabel("Number of Events")
    ax.set_ylabel("Probability")
    ax.set_title(f"Poisson Distribution ($\lambda$ = {lambda_})")


    ax.axvline(expected_value, color='red', linestyle='--', label='Expected Value')
    ax.axvline(median, color='green', linestyle='--', label='Median')
    ax.legend()
    # save it in pdf
    plt.savefig("poisson_distribution.pdf")