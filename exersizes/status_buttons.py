import sqlite3
from tkinter import Button, messagebox
from crs.enums.global_enums import ButtonNames, Titles, InfoMessages


def add_buttons(frame, word):
    Button(
        frame, text=ButtonNames.SET_KNOWN.value,
        width=25, command=lambda: set_status(word, 1, 0)
    ).grid(row=3, column=0)
    Button(
        frame, text=ButtonNames.SET_WELL_KNOWN.value,
        command=lambda: set_status(word, 0, 1), width=25
    ).grid(row=3, column=1)


def set_status(word, is_known, is_well_known):
    with sqlite3.connect('vocabulary.db') as conn:
        cursor = conn.cursor()
        cursor.execute(''' UPDATE words_word SET
                       is_new = :new,
                       is_known = :known,
                       is_well_known = :well_known
                       WHERE id = :id ''',
                       {
                           'new': 0,
                           'known': is_known,
                           'well_known': is_well_known,
                           'id': word[2]
                       })
        conn.commit()
    messagebox.showinfo(
        title=Titles.GOT_IT.value,
        message=InfoMessages.CHANGED.value
    )
