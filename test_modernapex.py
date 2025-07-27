# test_modernapex.py
"""
Tests for ModernApex module.
"""

import unittest
from modernapex import ModernApex

class TestModernApex(unittest.TestCase):
    """Test cases for ModernApex class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = ModernApex()
        self.assertIsInstance(instance, ModernApex)
        
    def test_run_method(self):
        """Test the run method."""
        instance = ModernApex()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
