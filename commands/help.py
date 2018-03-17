from commands.abstract_command import AbstractCommand
from abc import abstractmethod


class Help(AbstractCommand):

    @staticmethod
    @abstractmethod
    def execute(context: dict, id: int) -> str:
        result = """Список команд:
        /help - вызов справки (это сообщение и есть справка)
        /start - начало тестирования
        /finish - закончить тестирование"""
        return result