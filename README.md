# Bayesian Network Implementation

A pure Python implementation of a Bayesian Network for the rain-maintenance-train-appointment scenario.

## Features

- **Pure Python**: No external dependencies required
- **Flexible Inference**: Handle any combination of evidence
- **Probability Calculations**: Joint, conditional, and marginal probabilities
- **Well-tested**: Comprehensive test suite
- **Modular Design**: Easy to extend and modify

## Installation

```bash
git clone https://github.com/sigonebyexample/bayesian-network-project.git
cd bayesian-network-project
pip install -e .
```
## Project Structure
``` bash
src/
├── model.py          # Network structure and nodes
├── inference.py      # Prediction and evidence handling
├── probability.py    # Probability calculations
└── utils.py          # Utility functions

examples/            # Usage examples
tests/               # Unit tests
docs/                # Documentation
```
## Running Examples
``` bash
# Basic usage
python examples/basic_usage.py

# Advanced inference
python examples/advanced_inference.py

# Probability calculations
python examples/probability_calculations.py
```
## Running Tests
``` bash
python -m unittest discover tests
```
