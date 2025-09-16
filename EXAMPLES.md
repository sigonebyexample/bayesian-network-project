# Examples Guide

## Basic Usage

```python
from src.inference import InferenceEngine
from src.probability import ProbabilityCalculator

# Initialize
inference = InferenceEngine()
probability = ProbabilityCalculator()

# Simple prediction
inference.display_predictions({"train": "delayed"})

# Joint probability
prob = probability.joint_probability({
    'rain': 'none',
    'maintenance': 'no',
    'train': 'on time',
    'appointment': 'attend'
})
```
