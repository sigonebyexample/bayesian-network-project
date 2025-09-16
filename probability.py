from .model import BayesianNetwork

class ProbabilityCalculator:
    """Probability calculator for Bayesian Network"""
    
    def __init__(self, network=None):
        self.network = network or BayesianNetwork()
    
    def joint_probability(self, evidence_dict):
        """Calculate joint probability with optional evidence"""
        total_prob = 0.0
        
        # Iterate over all possible combinations
        for rain_val in ['none', 'light', 'heavy']:
            if 'rain' in evidence_dict and evidence_dict['rain'] != rain_val:
                continue
                
            for maint_val in ['yes', 'no']:
                if 'maintenance' in evidence_dict and evidence_dict['maintenance'] != maint_val:
                    continue
                    
                for train_val in ['on time', 'delayed']:
                    if 'train' in evidence_dict and evidence_dict['train'] != train_val:
                        continue
                        
                    for appt_val in ['attend', 'miss']:
                        if 'appointment' in evidence_dict and evidence_dict['appointment'] != appt_val:
                            continue
                        
                        # Calculate probability for this combination
                        p_rain = self.network.get_node('rain').probability(rain_val, {})
                        p_maint = self.network.get_node('maintenance').probability(maint_val, {'rain': rain_val})
                        p_train = self.network.get_node('train').probability(train_val, {'rain': rain_val, 'maintenance': maint_val})
                        p_appt = self.network.get_node('appointment').probability(appt_val, {'train': train_val})
                        
                        total_prob += p_rain * p_maint * p_train * p_appt
        
        return total_prob
    
    def conditional_probability(self, query, given):
        """Calculate conditional probability P(query | given)"""
        full_evidence = {**given, **query}
        p_joint = self.joint_probability(full_evidence)
        p_given = self.joint_probability(given)
        
        return p_joint / p_given if p_given > 0 else 0.0
    
    def marginal_probability(self, variable, value, evidence=None):
        """Calculate marginal probability P(variable=value | evidence)"""
        if evidence is None:
            evidence = {}
        
        query_evidence = {variable: value}
        full_evidence = {**evidence, **query_evidence}
        
        p_joint = self.joint_probability(full_evidence)
        p_evidence = self.joint_probability(evidence)
        
        return p_joint / p_evidence if p_evidence > 0 else 0.0
