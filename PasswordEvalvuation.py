import urwid


def on_ask_change(edit, new_edit_text):
    reply.set_text("Рейтинг пароля: %s" % rating(new_edit_text))
    rating(new_edit_text)
    

def is_very_long(password):
    return len(password) >= 12
   
          
def has_digit(password):
    return any(symbol.isdigit() for symbol in password)


def has_letters(password):
    return any(symbol.isalpha() for symbol in password)
    

def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)


def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)
    

def has_symbols(password):
    return any(not symbol.isdigit() and not symbol.isalpha() for symbol in password)


def rating(password):
    score = 0
    for function in functions:
        if function(password):
            score += 2
    return score


if __name__ == '__main__':
    functions = [
        is_very_long,
        has_digit,
        has_letters,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]
    ask=urwid.Edit('Введите пароль: ', mask='*')
    reply=urwid.Text("")
    menu=urwid.Pile([ask, reply])
    menu=urwid.Filler(menu, valign='top')
    urwid.connect_signal(ask, 'change', on_ask_change)
    urwid.MainLoop(menu).run()
        

 