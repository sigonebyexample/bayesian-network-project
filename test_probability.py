import unittest
from src.probability import ProbabilityCalculator

class TestProbability(unittest.TestCase):
    def setUp(self):
        self.probability = ProbabilityCalculator()
    
    def test_joint_probability_full(self):
        # Test full joint probability
        prob = self.probability.joint_probability({
            'rain': 'none',
            'maintenance': 'no',
            'train': 'on time',
            'appointment': 'attend'
        })
        self.assertGreaterEqual(prob, 0)
        self.assertLessEqual(prob, 1)
    
    def test_joint_probability_partial(self):
        # Test partial evidence
        prob = self.probability.joint_probability({'rain': 'heavy', 'train': 'delayed'})
        self.assertGreaterEqual(prob, 0)
        self.assertLessEqual(prob, 1)
    
    def test_conditional_probability(self):
        # Test conditional probability
        prob = self.probability.conditional_probability(
            {'rain': 'heavy'},
            {'train': 'delayed'}
        )
        self.assertGreaterEqual(prob, 0)
        self.assertLessEqual(prob, 1)
    
    def test_marginal_probability(self):
        # Test marginal probability
        prob = self.probability.marginal_probability('appointment', 'miss', {'rain': 'light'})
        self.assertGreaterEqual(prob, 0)
        self.assertLessEqual(prob, 1)

if __name__ == '__main__':
    unittest.main()
