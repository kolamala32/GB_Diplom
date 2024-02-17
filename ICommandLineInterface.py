# Импортируем модуль для работы с абстрактными базовыми классами
import abc

# Создаем абстрактный базовый класс для интерфейса ICommandLineInterface
class ICommandLineInterface(abc.ABC):
  # Определяем абстрактные методы, которые должны быть реализованы в классе, наследующем от интерфейса

  @abc.abstractmethod
  def parse_commands(self):
    # Метод для разбора команд, введенных пользователем в командной строке
    pass

  @abc.abstractmethod
  def print_output(self):
    # Метод для вывода информации о модели, процессах и результатах в командную строку
    pass

  @abc.abstractmethod
  def get_input(self):
    # Метод для получения данных от пользователя через командную строку
    pass