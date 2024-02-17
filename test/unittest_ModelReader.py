import unittest
from ModelReader import ModelReader

class TestModelReader(unittest.TestCase):
    def setUp(self):
        self.file_path = "prizma.stp"
        self.model_reader = ModelReader(self.file_path)

    def test_load_model(self):
        self.model_reader.load_model()
        self.assertIsNotNone(self.model_reader.model, "Model should not be None after loading")
        # Add more assertions as needed

if __name__ == "__main__":
    unittest.main()
