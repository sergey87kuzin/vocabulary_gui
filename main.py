from tkinter import Tk, Button, messagebox, LabelFrame
from exersizes import new_words, eng_to_rus


class Vocabulary():
    def __init__(self, new, known_words, to_rus, to_eng):
        self.root = Tk()
        self.second_screen = Tk()
        self.new = new
        self.known_words = known_words
        self.to_rus = to_rus
        self.to_eng = to_eng

    def on_closing(self):
        ''' действия при закрытии одного из окон '''
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.second_screen.destroy()
            self.root.destroy()

    def start(self):
        ''' Создание окон, расположение на них нужных элементов '''
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.title('Английский')
        self.second_screen.title('Результат')
        self.second_screen.eval('tk::PlaceWindow . center')
        self.second_screen.protocol("WM_DELETE_WINDOW", self.on_closing)
        frame = LabelFrame(self.second_screen)
        frame.pack()

        Button(
            self.root, text='Просмотреть новые слова', width=20,
            command=lambda: self.new.show(frame, 0, True)
        ).grid(row=0)
        Button(
            self.root, text='Смутно знакомые слова', width=20,
            command=lambda: self.known_words.show(frame, 0, True)
        ).grid(row=1)
        Button(
            self.root, text='На русский', width=20,
            command=lambda: self.to_rus.translate(frame, 0, True)
        ).grid(row=2)
        Button(
            self.root, text='На английский', width=20,
            command=lambda: self.to_eng.translate(frame, 0, True)
        ).grid(row=3)


if __name__ == '__main__':
    new = new_words.Word(True, False)
    known_words = new_words.Word(False, True)
    to_rus = eng_to_rus.WellKnownWord(0, 1)
    to_eng = eng_to_rus.WellKnownWord(1, 0)
    voc = Vocabulary(new, known_words, to_rus, to_eng)
    voc.start()
    voc.root.mainloop()
