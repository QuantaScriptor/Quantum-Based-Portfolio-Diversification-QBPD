
import unittest
from qbpd import QuantumPortfolioDiversification

class TestQBPD(unittest.TestCase):
    def setUp(self):
        self.assets = ['AAPL', 'GOOGL', 'AMZN', 'MSFT', 'TSLA']
        self.qbpd = QuantumPortfolioDiversification(self.assets)

    def test_optimize_portfolio(self):
        result = self.qbpd.optimize_portfolio()
        self.assertIsInstance(result, dict)
        self.assertTrue(len(result) > 0)

if __name__ == '__main__':
    unittest.main()
    