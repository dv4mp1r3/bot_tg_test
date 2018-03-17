import telepot
import time
from config import api_key
from telepot.loop import MessageLoop
from question_helper import QuestionHelper

context = {}
bot = telepot.Bot(api_key)


def proceed_message(text: str, id: int) -> str:
    """
    Обработка полученного сообщения, если это не команда
    :param text: текст сообщения
    :param id: идентификатор пользователя, от которого получено сообщение
    :return: результат обработки
    """
    if 'stage' not in context[id]:
        return execute_command('help', id)
    else:
        if context[id]['stage'] != 'running':
            return "Для запуска теста заного введите /start"
        if int(text) <= 0:
            return "Необходимо ввести только номер варианта ответа!"

        if id in context:
            qnum = context[id]['qnum']
            context[id]['answers'][qnum] = int(text)
            context[id]['qnum'] = qnum + 1
            if context[id]['qnum'] == len(context[id]['questions']):
                return test_finished(id)
        result = context[id]['questions'][context[id]['qnum']]
        return QuestionHelper.get_question_text(result)


def test_finished(id: int) -> str:
    """
    Обработка ответов на вопросы, вывод результатов пользователю
    :param id:
    :return:
    """
    correct_count = 0
    current = 0
    context[id]['stage'] = 'finished'
    while current < len(context[id]['questions']):
        if QuestionHelper.is_correct(context[id]['questions'][current], context[id]['answers'][current]):
            correct_count = correct_count+1
        current = current + 1

    return 'Количество верных ответов: ' + str(correct_count)


def is_command(text: str) -> bool:
    """
    Проверка на то что отправленное пользователем сообщение - команда
    :param text:
    :return:
    """
    return text[0] == '/'


def execute_command(name: str, id: int) -> str:
    """
    Запуск команды
    :param name: имя команды без символа /
    :param id: идентификатор пользователя
    :return: результат выполнения команды
    """
    if name.lower() == 'abstract_command':
        raise ModuleNotFoundError
    module_name = "commands." + name
    classname = name.title()
    module = __import__(module_name, fromlist=[classname])
    command = getattr(module, classname)
    return command.execute(context, id)


def handle(msg: dict):
    """
    Обработка входящего сообщения
    :param msg:
    """
    id = msg['chat']['id']
    try:
        if 'text' in msg:
            text = msg['text']
            if is_command(text):
                result = execute_command(text[1:], id)
            else:
                result = proceed_message(text, id)
            bot.sendMessage(id, result)
        else:
            bot.sendMessage(id, "Обрабатываются только текстовые сообщения")
    except ModuleNotFoundError as e:
        bot.sendMessage(id, 'Не найден обработчик для команды '+msg['text'])
    except Exception as err:
        bot.sendMessage(id, 'Что-то пошло не так :(')


MessageLoop(bot, handle).run_as_thread()
while 1:
    time.sleep(10)

