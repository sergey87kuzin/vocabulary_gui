import sqlite3
from tkinter import LabelFrame
from main import Vocabulary
from exersizes import (
    new_words, eng_to_rus,  # status_buttons
)


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
        for child in frame.winfo_children():
            if child.widgetName == 'Button':
                assert child['text'] in self.new_texts
        self.to_eng.translate(frame, 0, True)
        for child in frame.winfo_children():
            if child.widgetName == 'Button':
                assert child['text'] in self.to_eng_texts
        self.voc.root.destroy()
        self.voc.second_screen.destroy()

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
