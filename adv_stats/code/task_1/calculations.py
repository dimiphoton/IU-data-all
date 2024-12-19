
import numpy as np
from scipy.stats import poisson

def calculate_poisson_probabilities(lambda_, threshold):
    """
    Calculate probabilities for a Poisson distribution 
    until the probability is below the threshold.

    Args:
        lambda_: The lambda parameter of the Poisson distribution.
        threshold: The probability threshold.

    Returns:
        A NumPy array containing the probabilities.
    """
    
    probabilities = [poisson.pmf(0, lambda_)]
    k = 1  # Start from 1 since you already calculated the 0th probability
    
    while True:
        probability = poisson.pmf(k, lambda_)
        
        # Break when both conditions are met
        if probability < threshold and probability < probabilities[-1]:
            break
        
        probabilities.append(probability)
        k += 1  # Increment k
    
    return np.array(probabilities)




def calculate_poisson_median(lambda_):
    """
    Calculate the median of a Poisson distribution.
    Args:
        lambda_: The lambda parameter of the Poisson distribution.
    Returns:
    The median of the Poisson distribution.
    """
    return poisson.median(lambda_)


