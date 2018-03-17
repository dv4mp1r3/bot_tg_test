

class QuestionHelper:

    @staticmethod
    def get_question_text(question: dict) -> str:
        """
        Форматирование словаря с информацией по вопросу
        в сообщение с вопросом и вариантами ответа
        :param question:
        :return:
        """
        text = question['text']
        for key, value in question['answers'].items():
            text += "\r\n" + key + ". " + value['text']
        return text

    @staticmethod
    def is_correct(question: dict, answer_number: int) -> bool:
        """
        Проверка правильности ответа на вопрос
        :param question: словарь со всей информацией по вопросу
        :param answer_number: выбранный пользователем вариант ответа
        :return:
        """
        return question['correct'] == answer_number

