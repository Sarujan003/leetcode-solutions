from abc import ABC, abstractmethod

class LibraryItem(ABC):
    @abstractmethod
    def get_info(self):
        pass

    @abstractmethod
    def get_fee(self, days_late):
        pass

class Book(LibraryItem):
    def __init__(self, title, author):
        super().__init__()
        self.__title = title
        self.__author = author

    def get_info(self):
        return f"Book title: {self.__title}, Author: {self.__author}"

    def get_fee(self, days_late):
        return 50 * days_late


b = Book("The Alchemist", "Paulo Coelho")

print(b.get_info())

print(b.get_fee(3))