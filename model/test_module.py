import unittest

from train import train_model

class TestModule(unittest.TestCase):

    def test_Module(self):
        
        # Arrange
        results = train_model()

        # Assert
        self.assertGreaterEqual(80, results["r2"])
        self.assertGreaterEqual(30, results["mape"])
