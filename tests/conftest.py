''' если сделать вложенную папку и в ней сделать такой файл,
то только вложенные в эту папку файлы будут видеть его. Так можно
ограничить число фикстур на один файл. В этом файле можно создать
функцию, а потом с помощью другой функции, обернутой в декоратор
фикстуры, вернуть ее для передачи в тест.
в параметрах декоратора можно указать scope=session, он будет
выполняться один раз, а не при каждом обращении
если внутри фикстуры использовать yield, то до теста будет
выполнена часть до него, после теста выполнится часть после.
прямой аналог SetUpClass - TearDown '''
import pytest
from main import Vocabulary
from exersizes import (
    new_words, eng_to_rus,  # status_buttons
)


@pytest.fixture
def tk_work():
    new = new_words.Word(True, False)
    known_words = new_words.Word(False, True)
    to_rus = eng_to_rus.WellKnownWord(0, 1)
    to_eng = eng_to_rus.WellKnownWord(1, 0)
    voc = Vocabulary(
        new, known_words, to_rus, to_eng
    )
    yield voc
    voc.root.quit()
    voc.second_screen.quit()
