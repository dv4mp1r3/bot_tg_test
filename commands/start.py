from commands.abstract_command import AbstractCommand
from abc import abstractmethod
import json
import random
from question_helper import QuestionHelper


class Start(AbstractCommand):

    @staticmethod
    @abstractmethod
    def execute(context: dict, id: int) -> str:
        try:
            result = ''
            if id not in context:
                context[id] = {}
                context[id]['answers'] = {}
                context[id]['stage'] = 'running'
                questions = Start.load_questions('data.txt')
                context[id]['questions'] = questions
                context[id]['qnum'] = 0
                result = context[id]['questions'][context[id]['qnum']]
            else:
                result = context[id]['questions'][context[id]['qnum']]
                if context[id]['stage'] == 'running':
                    result = """Тест уже идет. Текущий вопрос:            
                            """ + context[id]['questions'][context[id]['qnum']]

            return QuestionHelper.get_question_text(result)
        except Exception as e:
            raise e


    @staticmethod
    def load_questions(filename: str) -> list:
        """
        Загрузка списка вопросов из файла и рандомное перемешивание
        :param filename: путь к файлу
        :return:
        """
        f = open(filename, 'r')
        data = json.loads(f.read())
        f.close()
        questions = random.sample(data, len(data))
        return questions
