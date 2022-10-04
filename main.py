from tkinter import Tk, Button, messagebox, LabelFrame
from exersizes import new_words, eng_to_rus

new = new_words.Word(True, False)
known_words = new_words.Word(False, True)
to_rus = eng_to_rus.WellKnownWord(0, 1)
to_eng = eng_to_rus.WellKnownWord(1, 0)

root = Tk()


def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        second_screen.destroy()
        root.destroy()


root.protocol("WM_DELETE_WINDOW", on_closing)
root.title('Английский')
second_screen = Tk()
second_screen.title('Результат')
second_screen.eval('tk::PlaceWindow . center')
second_screen.protocol("WM_DELETE_WINDOW", on_closing)
frame = LabelFrame(second_screen)
frame.pack()

Button(
    root, text='Просмотреть новые слова', width=20,
    command=lambda: new.show(frame, 0, True)
).grid(row=0)
Button(
    root, text='Смутно знакомые слова', width=20,
    command=lambda: known_words.show(frame, 0, True)
).grid(row=1)
Button(
    root, text='На русский', width=20,
    command=lambda: to_rus.translate(frame, 0, True)
).grid(row=2)
Button(
    root, text='На английский', width=20,
    command=lambda: to_eng.translate(frame, 0, True)
).grid(row=3)

root.mainloop()
