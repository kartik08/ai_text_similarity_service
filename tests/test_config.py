import unittest
import sys
import os

sys.path.insert(0,"../")

from config import BaseConfig, DefaultConfig
from utils import INSTANCE_FOLDER_PATH

class TestConfig(unittest.TestCase):

    # Testing BaseConfig Class 
    def test_base_config(self):
        config = BaseConfig()
        self.assertTrue(os.path.isabs(config.PROJECT_ROOT))
    
    # Testing Default Config Class
    def test_default_config(self):
        config = DefaultConfig()

if __name__ == "__main__":
    unittest.main()
