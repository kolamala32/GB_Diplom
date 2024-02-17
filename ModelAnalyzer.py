from OCC.Core.TopExp import TopExp_Explorer
from OCC.Core.TopAbs import TopAbs_FACE
from OCC.Core.BRepAdaptor import BRepAdaptor_Surface
from OCC.Core.GeomAbs import GeomAbs_Circle


class ModelAnalyzer:
    def __init__(self, model_reader):
        self.model_reader = model_reader
        self.model = None

    def load_model(self):
        try:
            self.model_reader.load_model()
            self.model = self.model_reader.model
            print("Модель успешно загружена.")
        except Exception as e:
            print("Не удалось загрузить модель:", e)

    def analyze_model(self):
        if self.model is None:
            print("Модель не загружена. Пожалуйста, загрузите модель.")
            return

        num_faces = self.count_faces()
        num_holes = self.count_circular_holes()

        print(f"Количество граней в модели: {num_faces}")
        print(f"Количество круглых отверстий в модели: {num_holes}")

    def count_faces(self):
        if self.model is None:
            return 0

        face_explorer = TopExp_Explorer(self.model, TopAbs_FACE)
        num_faces = 0
        while face_explorer.More():
            num_faces += 1
            face_explorer.Next()
        return num_faces

    def count_circular_holes(self):
        if self.model is None:
            return 0

        face_explorer = TopExp_Explorer(self.model, TopAbs_FACE)
        num_holes = 0
        while face_explorer.More():
            face = face_explorer.Current()
            surface = BRepAdaptor_Surface(face)
            if surface.GetType() == GeomAbs_Circle:
                num_holes += 1
            face_explorer.Next()
        return num_holes

    def determine_dimensions(self):
        pass

    def determine_shape(self):
        pass

    def determine_other_characteristics(self):
        pass

    def determine_nodes(self):
        pass

    def count_holes(self):
        pass

    def count_edges(self):
        pass


if __name__ == "__main__":
    from ModelReader import ModelReader

    model_reader = ModelReader('prizma.stp')
    analyzer = ModelAnalyzer(model_reader)

    analyzer.load_model()
    analyzer.analyze_model()
