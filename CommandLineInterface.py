import abc
from GUI import GUI
from ModelAnalyzer import ModelAnalyzer
from ModelReader import ModelReader
from ProcessDesigner import ProcessDesigner
from ResultExporter import ResultExporter
from ResultVisualizer import ResultVisualizer

class ICommandLineInterface(abc.ABC):
    @abc.abstractmethod
    def parse_commands(self):
        pass

    @abc.abstractmethod
    def print_output(self):
        pass

    @abc.abstractmethod
    def get_input(self):
        pass

class CommandLineInterface(GUI, ICommandLineInterface):
    def __init__(self):
        super().__init__()
        self.commands = []
        self.output = ""
        self.input = ""

    def parse_commands(self):
        self.input = input("Введите команды: ")
        self.commands = self.input.split()
        for command in self.commands:
            if command == "load":
                self.load_model()
            elif command == "analyze":
                self.analyze_model()
            elif command == "design":
                self.design_processes()
            elif command == "visualize":
                self.visualize_results()
            elif command == "export":
                self.export_results()
            elif command == "help":
                self.print_help()
            elif command == "exit":
                self.exit()
            else:
                self.print_error()

    def print_output(self):
        print(self.output)

    def get_input(self):
        return self.input

    def load_model(self):
        try:
            model_reader = ModelReader()
            source = input("Введите источник данных (файл, URL или база данных): ")
            path = input("Введите путь к файлу, URL или имя базы данных: ")
            if source == "файл":
                model_reader.load_model_from_file(path)
            elif source == "URL":
                model_reader.load_model_from_url(path)
            elif source == "база данных":
                model_reader.load_model_from_database(path)
            self.output += "Модель успешно загружена\n"
        except Exception as e:
            self.output += f"Ошибка загрузки модели: {str(e)}\n"

    def analyze_model(self):
        try:
            model_analyzer = ModelAnalyzer()
            model_analyzer.determine_dimensions()
            model_analyzer.determine_shape()
            model_analyzer.determine_nodes()
            model_analyzer.determine_other_characteristics()
            self.output += "Модель имеет следующие особенности:\n"
            self.output += f"Размеры: {model_analyzer.dimensions}\n"
            self.output += f"Форма: {model_analyzer.shape}\n"
            self.output += f"Узлы: {model_analyzer.nodes}\n"
            self.output += f"Другие характеристики: {model_analyzer.other_characteristics}\n"
        except Exception as e:
            self.output += f"Ошибка анализа модели: {str(e)}\n"

    def design_processes(self):
        try:
            process_designer = ProcessDesigner()
            type = input("Введите тип детали (круглая, прямоугольная или сложная): ")
            quantity = input("Введите количество деталей: ")
            optimization = input("Включить оптимизацию процессов (да или нет): ")
            process_designer.create_processes(type, quantity, optimization)
            self.output += "Процессы успешно созданы\n"
        except Exception as e:
            self.output += f"Ошибка создания процессов: {str(e)}\n"

    def visualize_results(self):
        try:
            result_visualizer = ResultVisualizer()
            result_visualizer.display_model()
            result_visualizer.display_graphs()
            result_visualizer.display_diagrams()
            result_visualizer.display_other_elements()
            self.output += "Результаты визуализированы по ссылке: https://example.com/visualization\n"
        except Exception as e:
            self.output += f"Ошибка визуализации результатов: {str(e)}\n"

    def export_results(self):
        try:
            result_exporter = ResultExporter()
            format = input("Введите формат данных (CSV, JSON или XML): ")
            filename = input("Введите имя файла: ")
            result_exporter.export_results(format, filename)
            self.output += f"Результаты успешно экспортированы в файл: {filename}\n"
        except Exception as e:
            self.output += f"Ошибка экспорта результатов: {str(e)}\n"

    def print_help(self):
        self.output += "Доступные команды:\n"
        self.output += "load - загрузить модель из файла или другого источника данных\n"
        self.output += "analyze - анализировать модель и выявить ее особенности\n"
        self.output += "design - создать процессы изготовления деталей штампов\n"
        self.output += "visualize - визуализировать результаты проектирования процессов\n"
        self.output += "export - экспортировать результаты проектирования процессов в различные форматы данных\n"
        self.output += "help - вывести справочную информацию о доступных командах\n"
        self.output += "exit - выйти из программы\n"

    def exit(self):
        self.output += "Выход из программы\n"
        # Дополнительные операции, если необходимо
