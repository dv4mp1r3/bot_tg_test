from commands.abstract_command import AbstractCommand
from abc import abstractmethod


class Test(AbstractCommand):

    @staticmethod
    @abstractmethod
    def execute(context: dict, id: int) -> str:
        return 'Тестовая месага'
