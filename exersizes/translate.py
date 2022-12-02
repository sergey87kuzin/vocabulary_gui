import sqlite3
from tkinter import messagebox
from crs.enums.global_enums import Titles


def translate(frame, word):
    if not word:
        return
    answer = 'no such word'
    try:
        with sqlite3.connect('vocabulary.db') as conn:
            cursor = conn.cursor()
            result = cursor.execute(
                ''' SELECT english FROM words_word WHERE
                russian LIKE :word''', {'word': f'%{word}%'}
            ).fetchall()
            if len(result) > 0:
                answer = ', '.join([val[0] for val in result])
            else:
                result = cursor.execute(
                    ''' SELECT russian FROM words_word WHERE
                    english LIKE :word''', {'word': f'%{word}%'}
                ).fetchall()
                if len(result) > 0:
                    answer = ', '.join([val[0] for val in result])
    except Exception as e:
        messagebox.showinfo(title=Titles.ERROR.value, message=str(e))
        return
    messagebox.showinfo(title=Titles.ERROR.value, message=answer)
