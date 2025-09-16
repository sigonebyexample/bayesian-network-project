import unittest
from src.inference import InferenceEngine

class TestInference(unittest.TestCase):
    def setUp(self):
        self.inference = InferenceEngine()
    
    def test_predict_proba_with_evidence(self):
        # Test with observed train
        predictions = self.inference.predict_proba({"train": "delayed"})
        self.assertEqual(predictions[2], "delayed")  # train should be observed
        
        # Test with multiple evidence
        predictions = self.inference.predict_proba({"rain": "heavy", "maintenance": "yes"})
        self.assertEqual(predictions[0], "heavy")  # rain observed
        self.assertEqual(predictions[1], "yes")    # maintenance observed
    
    def test_predict_proba_no_evidence(self):
        predictions = self.inference.predict_proba({})
        # All should be probability distributions, not strings
        for pred in predictions:
            self.assertIsInstance(pred, dict)
    
    def test_marginalize_maintenance(self):
        result = self.inference._marginalize_maintenance()
        self.assertIn('yes', result)
        self.assertIn('no', result)
        self.assertAlmostEqual(result['yes'] + result['no'], 1.0, places=6)

if __name__ == '__main__':
    unittest.main()test_inference
