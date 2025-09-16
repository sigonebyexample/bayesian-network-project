#!/usr/bin/env python3
"""
Quick start demo for the Bayesian Network.
Run this file to see immediate results.
"""

from src.inference import InferenceEngine
from src.probability import ProbabilityCalculator

def main():
    print("🚀 Bayesian Network Quick Start Demo")
    print("=" * 50)
    
    # Initialize
    inference = InferenceEngine()
    probability = ProbabilityCalculator()

    # Make predictions
    print("\n1. Making predictions with evidence: {'train': 'delayed'}")
    inference.display_predictions({"train": "delayed"})

    # Calculate probabilities
    print("\n2. Calculating joint probability:")
    evidence = {
        'rain': 'none',
        'maintenance': 'no',
        'train': 'on time',
        'appointment': 'attend'
    }
    joint_prob = probability.joint_probability(evidence)
    print(f"P({evidence}) = {joint_prob:.6f}")
    
    # Show some additional examples
    print("\n3. Additional examples:")
    
    # Conditional probability
    cond_prob = probability.conditional_probability(
        {'rain': 'heavy'},
        {'train': 'delayed'}
    )
    print(f"P(rain=heavy | train=delayed) = {cond_prob:.4f}")
    
    # Another prediction
    print("\n4. Prediction with multiple evidence:")
    inference.display_predictions({
        "rain": "light",
        "maintenance": "yes"
    }, "Light rain with maintenance")

if __name__ == "__main__":
    main()
