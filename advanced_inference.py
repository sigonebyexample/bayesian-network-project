#!/usr/bin/env python3
"""
Advanced inference examples for the Bayesian Network.
"""

from src.inference import InferenceEngine
from src.probability import ProbabilityCalculator

def main():
    print("=== Advanced Inference Examples ===")
    
    inference = InferenceEngine()
    probability = ProbabilityCalculator()
    
    # Multiple evidence scenarios
    scenarios = [
        ({"rain": "heavy", "maintenance": "yes"}, "Heavy rain with maintenance"),
        ({"train": "on time", "appointment": "attend"}, "Train on time, appointment attended"),
        ({"rain": "light", "maintenance": "no", "train": "delayed"}, "Light rain, no maintenance, train delayed"),
        ({}, "No evidence (prior probabilities)")
    ]
    
    for evidence, title in scenarios:
        inference.display_predictions(evidence, title)
    
    # Complex probability calculations
    print("\n=== Advanced Probability Calculations ===")
    
    # P(rain=heavy | train=delayed, maintenance=yes)
    prob1 = probability.conditional_probability(
        {'rain': 'heavy'},
        {'train': 'delayed', 'maintenance': 'yes'}
    )
    print(f"P(rain=heavy | train=delayed, maintenance=yes) = {prob1:.4f}")
    
    # P(appointment=miss | rain=light, maintenance=no)
    prob2 = probability.conditional_probability(
        {'appointment': 'miss'},
        {'rain': 'light', 'maintenance': 'no'}
    )
    print(f"P(appointment=miss | rain=light, maintenance=no) = {prob2:.4f}")

if __name__ == "__main__":
    main()
