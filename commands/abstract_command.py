import abc


class AbstractCommand(abc.ABC):

    @staticmethod
    @abc.abstractmethod
    def execute(self, context: dict, id: int) -> str:
        pass
