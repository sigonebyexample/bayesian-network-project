from .model import BayesianNetwork

class InferenceEngine:
    """Inference engine for Bayesian Network"""
    
    def __init__(self, network=None):
        self.network = network or BayesianNetwork()
    
    def predict_proba(self, evidence):
        """Predict probabilities for all nodes given evidence"""
        results = []
        
        for node_name in self.network.states:
            if node_name in evidence:
                results.append(evidence[node_name])
            else:
                results.append(self._calculate_probability(node_name, evidence))
        
        return results
    
    def _calculate_probability(self, node_name, evidence):
        """Calculate probability distribution for a node given evidence"""
        node = self.network.get_node(node_name)
        
        if node_name == 'rain':
            return node.cpt[()]
        
        elif node_name == 'maintenance':
            if 'rain' in evidence:
                return node.cpt[(evidence['rain'],)]
            else:
                return self._marginalize_maintenance()
        
        elif node_name == 'train':
            return self._marginalize_train(evidence)
        
        elif node_name == 'appointment':
            return self._marginalize_appointment(evidence)
    
    def _marginalize_maintenance(self):
        """Marginalize maintenance over rain"""
        prob_dist = {'yes': 0.0, 'no': 0.0}
        rain_node = self.network.get_node('rain')
        
        for rain_val in ['none', 'light', 'heavy']:
            p_rain = rain_node.cpt[()][rain_val]
            p_maint = self.network.get_node('maintenance').cpt[(rain_val,)]
            prob_dist['yes'] += p_rain * p_maint['yes']
            prob_dist['no'] += p_rain * p_maint['no']
        
        return prob_dist
    
    def _marginalize_train(self, evidence):
        """Marginalize train over rain and maintenance"""
        prob_dist = {'on time': 0.0, 'delayed': 0.0}
        rain_node = self.network.get_node('rain')
        maint_node = self.network.get_node('maintenance')
        train_node = self.network.get_node('train')
        
        for rain_val in ['none', 'light', 'heavy']:
            if 'rain' in evidence and rain_val != evidence['rain']:
                continue
            
            p_rain = (1.0 if 'rain' in evidence else rain_node.cpt[()][rain_val])
            
            for maint_val in ['yes', 'no']:
                if 'maintenance' in evidence and maint_val != evidence['maintenance']:
                    continue
                
                p_maint = (1.0 if 'maintenance' in evidence 
                          else maint_node.cpt[(rain_val,)][maint_val])
                
                p_train = train_node.cpt[(rain_val, maint_val)]
                
                for train_val in ['on time', 'delayed']:
                    prob_dist[train_val] += p_rain * p_maint * p_train[train_val]
        
        return prob_dist
    
    def _marginalize_appointment(self, evidence):
        """Marginalize appointment over train"""
        prob_dist = {'attend': 0.0, 'miss': 0.0}
        train_node = self.network.get_node('train')
        appt_node = self.network.get_node('appointment')
        
        for train_val in ['on time', 'delayed']:
            if 'train' in evidence and train_val != evidence['train']:
                continue
            
            # Simplified marginalization for demo
            p_train = 0.5  # In real implementation, would marginalize properly
            
            p_appt = appt_node.cpt[(train_val,)]
            
            for appt_val in ['attend', 'miss']:
                prob_dist[appt_val] += p_train * p_appt[appt_val]
        
        return prob_dist
    
    def display_predictions(self, evidence, title="Predictions"):
        """Display predictions in formatted output"""
        print(f"\n=== {title} ===")
        print(f"Evidence: {evidence}")
        
        predictions = self.predict_proba(evidence)
        
        for node, prediction in zip(self.network.states, predictions):
            if isinstance(prediction, str):
                print(f"{node}: {prediction} (observed)")
            else:
                print(f"{node}:")
                for value, prob in prediction.items():
                    print(f"  {value}: {prob:.4f}")
        print()
