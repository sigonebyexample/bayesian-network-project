#!/usr/bin/env python3
"""
Basic usage examples for the Bayesian Network.
"""

from src.inference import InferenceEngine
from src.probability import ProbabilityCalculator

def main():
    print("=== Basic Usage Examples ===")
    
    # Initialize engines
    inference = InferenceEngine()
    probability = ProbabilityCalculator()
    
    # Example 1: Basic inference
    print("\n1. Basic Inference:")
    inference.display_predictions({"train": "delayed"}, "Train delayed")
    
    # Example 2: Joint probability
    print("\n2. Joint Probability:")
    joint_prob = probability.joint_probability({
        'rain': 'none',
        'maintenance': 'no',
        'train': 'on time',
        'appointment': 'attend'
    })
    print(f"P(rain=none, maintenance=no, train=on time, appointment=attend) = {joint_prob:.6f}")
    
    # Example 3: Conditional probability
    print("\n3. Conditional Probability:")
    cond_prob = probability.conditional_probability(
        {'appointment': 'miss'},
        {'rain': 'heavy'}
    )
    print(f"P(appointment=miss | rain=heavy) = {cond_prob:.4f}")

if __name__ == "__main__":
    main()
