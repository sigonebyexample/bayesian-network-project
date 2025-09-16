class Node:
    """Represents a node in the Bayesian Network"""
    
    def __init__(self, name, cpt):
        self.name = name
        self.cpt = cpt  # Conditional Probability Table
        self.parents = []

    def probability(self, value, evidence):
        """Get probability of value given evidence"""
        if self.parents:
            key = tuple(evidence[parent] for parent in self.parents)
        else:
            key = ()
        return self.cpt[key][value]


class BayesianNetwork:
    """Bayesian Network implementation for the rain-maintenance-train-appointment scenario"""
    
    def __init__(self):
        self.nodes = {}
        self.states = ['rain', 'maintenance', 'train', 'appointment']
        
        # Define CPTs
        self._setup_network()
        
    def _setup_network(self):
        """Setup the network structure and probabilities"""
        rain_cpt = {(): {'none': 0.7, 'light': 0.2, 'heavy': 0.1}}
        
        maintenance_cpt = {
            ('none',): {'yes': 0.4, 'no': 0.6},
            ('light',): {'yes': 0.2, 'no': 0.8},
            ('heavy',): {'yes': 0.1, 'no': 0.9}
        }
        
        train_cpt = {
            ('none', 'yes'): {'on time': 0.8, 'delayed': 0.2},
            ('none', 'no'): {'on time': 0.9, 'delayed': 0.1},
            ('light', 'yes'): {'on time': 0.6, 'delayed': 0.4},
            ('light', 'no'): {'on time': 0.7, 'delayed': 0.3},
            ('heavy', 'yes'): {'on time': 0.4, 'delayed': 0.6},
            ('heavy', 'no'): {'on time': 0.5, 'delayed': 0.5}
        }
        
        appointment_cpt = {
            ('on time',): {'attend': 0.9, 'miss': 0.1},
            ('delayed',): {'attend': 0.6, 'miss': 0.4}
        }
        
        # Create nodes
        self.nodes['rain'] = Node('rain', rain_cpt)
        self.nodes['maintenance'] = Node('maintenance', maintenance_cpt)
        self.nodes['train'] = Node('train', train_cpt)
        self.nodes['appointment'] = Node('appointment', appointment_cpt)
        
        # Set parent relationships
        self.nodes['maintenance'].parents = ['rain']
        self.nodes['train'].parents = ['rain', 'maintenance']
        self.nodes['appointment'].parents = ['train']
    
    def get_node(self, name):
        """Get node by name"""
        return self.nodes.get(name)
