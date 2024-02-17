import unittest
from unittest.mock import patch
import tkinter as tk
from tkinter import filedialog
from GUI import GUI


class TestGUI(unittest.TestCase):
    @patch('tkinter.filedialog.askopenfilename', return_value='prizma.stp')
    def test_load_model_button(self, mock_askopenfilename):
        gui = GUI()

        # Нажатие на кнопку "Load Model"
        gui.buttons[0].invoke()

        # Проверка, что модель успешно загружена
        self.assertTrue(hasattr(gui, 'model_analyzer'))
        self.assertEqual(gui.model_analyzer.model_reader.file_path, 'prizma.stp')
        self.assertIn("Model loaded successfully.", gui.text_field.get("1.0", "end"))

    @patch('tkinter.filedialog.askopenfilename', return_value='prizma.stp')
    def test_analyze_model_button(self, mock_askopenfilename):
        gui = GUI()

        # Нажатие на кнопку "Load Model"
        gui.buttons[0].invoke()

        # Нажатие на кнопку "Analyze Model"
        gui.buttons[1].invoke()

        # Проверка, что модель была анализирована
        self.assertTrue(hasattr(gui, 'model_analyzer'))
        self.assertIn("Model loaded successfully.", gui.text_field.get("1.0", "end"))


if __name__ == '__main__':
    unittest.main()
