import sqlite3
import random
from tkinter import Label, Button, messagebox
from .status_buttons import add_buttons
from crs.enums.global_enums import ButtonNames, Titles, InfoMessages


class Word():
    def __init__(self, is_new, is_known):
        self.word_list = []
        self.is_new = is_new
        self.is_known = is_known

    def show(self, frame, word_id, new_list):
        ''' очистить область и показать элементы для просмотра
        новых слов '''
        for widget in frame.winfo_children():
            widget.destroy()
        word = self.get_word(word_id, new_list)
        Label(
            frame, text=word[0] + '  -  ' + word[1], pady=10,
            width=50
        ).grid(row=0, column=0, columnspan=2)
        Button(
            frame, text=ButtonNames.NEXT.value,
            width=25, command=lambda: self.show(frame, int(word_id) + 1, False)
        ).grid(row=1, column=1)
        Button(
            frame, text=ButtonNames.PREVIOUS.value,
            width=25, command=lambda: self.show(frame, int(word_id) - 1, False)
        ).grid(row=1, column=0)
        add_buttons(frame, word)

    def get_word(self, word_id, new_list):
        ''' получить случайное слово из списка '''
        word_id = word_id % 15
        if new_list:
            with sqlite3.connect('vocabulary.db') as conn:
                cursor = conn.cursor()
                word_list = cursor.execute(
                    ''' Select english, russian, id FROM words_word WHERE
                    is_new = :is_new AND is_known = :is_known''',
                    {'is_new': self.is_new, 'is_known': self.is_known}
                ).fetchall()
                if not word_list:
                    messagebox.showinfo(
                        title=Titles.OOPS.value,
                        message=InfoMessages.NOT_FOUND.value
                    )
                    return
                random.shuffle(word_list)
                self.word_list = word_list
        if len(self.word_list) < word_id:
            return self.word_list[0]
        return self.word_list[word_id]
