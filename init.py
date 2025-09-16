"""
Bayesian Network package for rain-maintenance-train-appointment scenario.
"""

from .model import BayesianNetwork, Node
from .inference import InferenceEngine
from .probability import ProbabilityCalculator
from .utils import format_probability, validate_evidence

__version__ = "0.1.0"
__all__ = [
    'BayesianNetwork',
    'Node',
    'InferenceEngine',
    'ProbabilityCalculator',
    'format_probability',
    'validate_evidence'
]
