import sqlite3
import random
from tkinter import Label, Button, messagebox, Entry
from .status_buttons import add_buttons


class WellKnownWord():
    def __init__(self, from_lang=0, to_lang=1):
        self.word_list = []
        self.from_lang = from_lang
        self.to_lang = to_lang

    def translate(self, frame, word_id, new_list):
        word = self.get_word(word_id, new_list)
        Label(
            frame, text=word[self.from_lang], width=40
        ).grid(row=1, column=0)
        trans = Entry(frame, width=30)
        trans.grid(row=1, column=1)
        Button(
            frame, text='Проверить', command=lambda: self.check_trans(
                frame, word_id, trans.get()
            )
        ).grid(row=2, column=0, columnspan=2)
        add_buttons(frame, word)

    def get_word(self, word_id, new_list):
        word_id = word_id % 15
        if new_list:
            with sqlite3.connect('vocabulary.db') as conn:
                cursor = conn.cursor()
                word_list = cursor.execute(
                    ''' Select english, russian, id FROM words_word WHERE
                    is_well_known = :is_well_known ''',
                    {'is_well_known': True}
                ).fetchall()
                if not word_list:
                    messagebox.showinfo(
                        title='Внезапно',
                        message='Нет слов, подходящих под категорию'
                    )
                    return
                random.shuffle(word_list)
                self.word_list = word_list
        return self.word_list[word_id]

    def check_trans(
            self, frame, word_id, trans):
        word = self.word_list[word_id]
        if trans not in word[self.to_lang]:
            messagebox.showinfo(
                title='Ошибка',
                message=word[self.from_lang] + '  -  ' + word[self.to_lang]
            )
        self.translate(frame, int(word_id)+1, True)
