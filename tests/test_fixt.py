from crs.enums.global_enums import ErrorMessages, ButtonNames

CHILD_BUTTONS = [
    ButtonNames.NEW_WORDS.value, ButtonNames.KNOWN_WORDS.value,
    ButtonNames.TO_RUS.value, ButtonNames.TO_ENG.value
]
NEW_BUTTONS = [
    ButtonNames.NEXT.value, ButtonNames.PREVIOUS.value,
    ButtonNames.SET_KNOWN.value, ButtonNames.SET_WELL_KNOWN.value
]
TRANS_BUTTONS = [
    ButtonNames.CHECK.value, ButtonNames.SET_KNOWN.value,
    ButtonNames.SET_WELL_KNOWN.value
]


def test_child(tk_work):
    ''' Проверяем, что установленные на стартовом экране
    кнопки правильно подписаны '''
    tk_work.start()
    assert len(tk_work.root.winfo_children()) == len(CHILD_BUTTONS), (
        ErrorMessages.WRONG_BUTTON_COUNT.value
    )
    for child in tk_work.root.winfo_children():
        assert child['text'] in CHILD_BUTTONS, (
            ErrorMessages.WRONG_BUTTON_NAME.value
        )


def test_new_frame(tk_work):
    ''' проверяем, что установленные на экране новых слов
    кнопки подписаны правильно '''
    tk_work.start()
    # tk_work.new.show(tk_work.frame, 0, True)
    tk_work.root.children['!button'].invoke()
    for child in tk_work.frame.winfo_children():
        if child.widgetName == 'button':
            assert child['text'] in NEW_BUTTONS, (
                ErrorMessages.WRONG_BUTTON_NAME.value
            )
    assert len(tk_work.frame.winfo_children()) == len(NEW_BUTTONS) + 1, (
        ErrorMessages.WRONG_BUTTON_COUNT.value
    )


def test_translate_frame(tk_work):
    ''' проверяем, что установленные на экране перевода
    кнопки подписаны правильно '''
    tk_work.start()
    # tk_work.to_eng.translate(tk_work.frame, 0, True)
    tk_work.root.children['!button3'].invoke()
    for child in tk_work.frame.winfo_children():
        if child.widgetName == 'button':
            assert child['text'] in TRANS_BUTTONS, (
                ErrorMessages.WRONG_BUTTON_NAME.value
            )
    assert len(tk_work.frame.winfo_children()) == len(TRANS_BUTTONS) + 2, (
        ErrorMessages.WRONG_BUTTON_COUNT.value
    )
