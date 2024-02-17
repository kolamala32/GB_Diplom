class ResultExporter:
    def __init__(self, model, processes):
        self.model = model
        self.processes = processes
        self.files = []

    def create_files(self):
        print("Создание файлов для экспорта результатов проектирования...")
        # Логика создания файлов для экспорта, включая параметры: имя, формат, расположение и т.д.
        # Предположим, что для каждого процесса создается отдельный файл
        for process in self.processes:
            file_name = f"{process.name}_result.csv"  # Пример формирования имени файла
            file_format = "CSV"  # Пример формата файла
            file_location = "/path/to/export/directory"  # Пример расположения файла
            file = {"name": file_name, "format": file_format, "location": file_location}
            self.files.append(file)

    def write_data(self):
        print("Запись данных о модели, процессах и других элементах в файлы...")
        # Логика записи данных о модели, процессах и других элементах в файлы
        # Предположим, что данные записываются в соответствии с форматом каждого файла
        for file_info in self.files:
            file_name = file_info["name"]
            file_format = file_info["format"]
            file_location = file_info["location"]
            with open(f"{file_location}/{file_name}", "w") as file:
                # Запись данных в файл
                file.write("Model data:\n")
                file.write(str(self.model))
                file.write("\n\nProcesses data:\n")
                for process in self.processes:
                    file.write(str(process))
                    file.write("\n")

    def format_results(self):
        print("Форматирование результатов проектирования для экспорта...")
        # Логика форматирования результатов проектирования в соответствии с выбранным форматом экспорта
        # В данном примере используется формат CSV
        formatted_results = []
        for process in self.processes:
            process_data = {
                "Name": process.name,
                "Time": process.time,
                "Cost": process.cost,
                "Quality": process.quality
            }
            formatted_results.append(process_data)
        return formatted_results