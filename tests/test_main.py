'''
pytest -s -v
если добавить еще ключ duration=<время в секундах> -vv, будут указаны
медленные тесты
если добавить --alluredir=<package_name>, а потом запустить allire
serve <package_name>, то получим красоту
Тесты можно пропускать, обернув в декоратор
@pytest.mark.skip
Если нужно выполнить один тест с разными наборами параметров,
можно задать эти наборы параметров с помощью
@pytest.mark.parametrize(
    'first_value', 'second_value', 'result', [
        (1, 2, 3), (4, 5, 9)...
    ]
)
значения записать в качестве параметров оборачиваемой функции
и использовать по назначению
если маркировать тесты декоратором @pytest.prod.<имя из pytest.ini>,
то при вызове через pytest -k <имя из pytest.ini>, запустятся только
они '''

import sqlite3
from tkinter import LabelFrame
from main import Vocabulary
from exersizes import (
    new_words, eng_to_rus,  # status_buttons
)
from crs.enums.global_enums import ErrorMessages


class TestMain():

    @classmethod
    def setup_class(cls):
        cls.button_texts = [
            'Просмотреть новые слова', 'Смутно знакомые слова',
            'На русский', 'На английский'
        ]
        cls.new_texts = [
            'Следующее', 'Предыдущее', 'отметить как знакомое',
            'отметить как хорошо знакомое'
        ]
        cls.to_eng_texts = [
            'Проверить', 'отметить как знакомое',
            'отметить как хорошо знакомое'
        ]
        cls.new = new_words.Word(True, False)
        cls.known_words = new_words.Word(False, True)
        cls.to_rus = eng_to_rus.WellKnownWord(0, 1)
        cls.to_eng = eng_to_rus.WellKnownWord(1, 0)
        cls.voc = Vocabulary(
            cls.new, cls.known_words, cls.to_rus, cls.to_eng
        )

    def test_children(self):
        self.voc.start()
        ''' Проверяем, верно ли указаны названия кнопок на
        главной странице '''
        for child in self.voc.root.winfo_children():
            assert child['text'] in self.button_texts
        frame = LabelFrame(self.voc.second_screen)
        frame.pack()
        ''' Проверяем, верно ли указаны названия кнопок на
        странице новых слов '''
        self.new.show(frame, 0, True)
        # self.voc.root.winfo_children()[0].invoke()

        for child in frame.winfo_children():
            if child.widgetName == 'button':
                assert child['text'] in self.new_texts, (
                    ErrorMessages.WRONG_BUTTON_NAME.value
                )
        self.to_eng.translate(frame, 0, True)
        # self.voc.root.winfo_children()[1].invoke()
        for child in frame.winfo_children():
            if child.widgetName == 'button':
                assert child['text'] in self.to_eng_texts
        self.voc.root.quit()
        self.voc.second_screen.quit()

    def test_exersizes(self):
        ''' Проверяем, корректно ли выбираются слова для списка
        неизвестных слов '''
        word = self.new.get_word(0, 1)
        with sqlite3.connect('vocabulary.db') as conn:
            cursor = conn.cursor()
            result = cursor.execute(
                ''' SELECT english, russian, id, is_new, is_known
                FROM words_word
                WHERE id=:id ''', {'id': word[2]}
            ).fetchone()
            assert word[0] == result[0]
            assert word[1] == result[1]
            assert word[2] == result[2]
            assert result[3] == 1
            assert result[4] == 0
