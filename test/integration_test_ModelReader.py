import unittest
from OCC.Core.TopoDS import TopoDS_Solid
from ModelReader import ModelReader


class IntegrationTestModelReader(unittest.TestCase):
    def test_load_model_integration(self):
        # Путь к файлу с моделью для загрузки
        file_path = "prizma.stp"

        # Загрузка модели
        model_reader = ModelReader(file_path)
        model_reader.load_model()

        # Проверка, что загруженная модель является экземпляром TopoDS_Solid
        self.assertIsInstance(model_reader.model, TopoDS_Solid, "Loaded model should be an instance of TopoDS_Solid")


if __name__ == '__main__':
    unittest.main()
