def format_probability(prob):
    """Format probability for display"""
    return f"{prob:.6f}"

def validate_evidence(evidence, allowed_vars=None):
    """Validate evidence dictionary"""
    if allowed_vars is None:
        allowed_vars = ['rain', 'maintenance', 'train', 'appointment']
    
    for key in evidence:
        if key not in allowed_vars:
            raise ValueError(f"Invalid variable: {key}. Allowed variables: {allowed_vars}")
    return True

def normalize_probability(distribution):
    """Normalize a probability distribution to sum to 1"""
    total = sum(distribution.values())
    if total > 0:
        return {k: v / total for k, v in distribution.items()}
    return distribution
