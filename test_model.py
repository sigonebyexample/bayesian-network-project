import unittest
from src.model import BayesianNetwork, Node

class TestModel(unittest.TestCase):
    def setUp(self):
        self.network = BayesianNetwork()
    
    def test_network_structure(self):
        self.assertEqual(len(self.network.nodes), 4)
        self.assertEqual(self.network.nodes['rain'].parents, [])
        self.assertEqual(self.network.nodes['maintenance'].parents, ['rain'])
        self.assertEqual(self.network.nodes['train'].parents, ['rain', 'maintenance'])
        self.assertEqual(self.network.nodes['appointment'].parents, ['train'])
    
    def test_probability_calculation(self):
        # Test rain probability
        rain_prob = self.network.nodes['rain'].probability('none', {})
        self.assertAlmostEqual(rain_prob, 0.7)
        
        # Test maintenance probability given rain
        maint_prob = self.network.nodes['maintenance'].probability('yes', {'rain': 'none'})
        self.assertAlmostEqual(maint_prob, 0.4)
        
        # Test train probability given rain and maintenance
        train_prob = self.network.nodes['train'].probability('on time', {'rain': 'none', 'maintenance': 'yes'})
        self.assertAlmostEqual(train_prob, 0.8)
    
    def test_get_node(self):
        node = self.network.get_node('rain')
        self.assertIsNotNone(node)
        self.assertEqual(node.name, 'rain')
        
        node = self.network.get_node('nonexistent')
        self.assertIsNone(node)

if __name__ == '__main__':
    unittest.main()
