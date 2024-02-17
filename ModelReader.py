from OCC.Extend.DataExchange import read_step_file


class ModelReader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.model = None

    def load_model(self):
        print(f"Загрузка модели из файла: {self.file_path}")
        try:
            # Attempt to read the STEP file
            self.model = read_step_file(self.file_path)
            print("Модель успешно загружена.")
        except FileNotFoundError:
            print(f"File '{self.file_path}' not found.")
        except Exception as e:
            print(f"Не удалось прочитать модель из файла: {e}")

