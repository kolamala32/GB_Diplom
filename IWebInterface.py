# Импортируем модуль для работы с абстрактными базовыми классами
import abc

# Создаем абстрактный базовый класс для интерфейса IWebInterface
class IWebInterface(abc.ABC):
  # Определяем абстрактные методы, которые должны быть реализованы в классе, наследующем от интерфейса

  @abc.abstractmethod
  def create_server(self):
    # Метод для создания сервера для обработки запросов от пользователей
    pass

  @abc.abstractmethod
  def create_pages(self):
    # Метод для создания страниц для отображения информации о модели, процессах и результатах
    pass

  @abc.abstractmethod
  def create_forms(self):
    # Метод для создания форм для ввода данных от пользователей
    pass

  @abc.abstractmethod
  def handle_requests(self):
    # Метод для обработки данных из форм и вызывания соответствующих методов других классов
    pass
