from enum import Enum


class ErrorMessages(Enum):
    WRONG_BUTTON_NAME = 'неправильно названа кнопка'
    WRONG_BUTTON_COUNT = 'неверное количество кнопок'


class ButtonNames(Enum):
    NEW_WORDS = 'Просмотреть новые слова'
    KNOWN_WORDS = 'Смутно знакомые слова'
    TO_RUS = 'На русский'
    TO_ENG = 'На английский'
    NEXT = 'Следующее'
    PREVIOUS = 'Предыдущее'
    SET_KNOWN = 'отметить как знакомое'
    SET_WELL_KNOWN = 'отметить как хорошо знакомое'
    CHECK = 'Проверить'
    TRANSLATE = 'Перевести'


class Titles(Enum):
    EXIT = 'Выход'
    ENGLISH = 'Английский'
    RESULT = 'Результат'
    GOT_IT = 'Принято'
    OOPS = 'Внезапно'
    ERROR = 'Ошибка'


class InfoMessages(Enum):
    CHANGED = 'состояние изменено'
    NOT_FOUND = 'Нет слов, подходящих под категорию'
    EXIT = 'Вы хотите выйти?'
