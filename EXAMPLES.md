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
## Multiple observed variables
``` bash
inference.display_predictions({
    "rain": "heavy",
    "maintenance": "yes",
    "train": "delayed"
})
```
## Conditional Probabilities
``` bash
# P(rain=heavy | train=delayed)
cond_prob = probability.conditional_probability(
    {'rain': 'heavy'},
    {'train': 'delayed'}
)

# P(appointment=miss | rain=light, maintenance=no)
cond_prob = probability.conditional_probability(
    {'appointment': 'miss'},
    {'rain': 'light', 'maintenance': 'no'}
)
```
## Marginal Probabilities
``` bash
# P(train=delayed | rain=light)
marg_prob = probability.marginal_probability(
    'train', 'delayed', {'rain': 'light'}
)
```
# Network Structure

## The Bayesian Network has the following structure:

    Rain → Maintenance

    Rain → Train

    Maintenance → Train

    Train → Appointment
