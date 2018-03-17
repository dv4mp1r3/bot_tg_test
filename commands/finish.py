from commands.abstract_command import AbstractCommand
from abc import abstractmethod


class Finish(AbstractCommand):

    @staticmethod
    @abstractmethod
    def execute(context: dict, id: int) -> str:
        if id in context:
            context[id] = {}
        return 'Тестирование завершено'