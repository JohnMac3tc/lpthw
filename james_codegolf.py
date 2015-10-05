class WTHxeption(Exception):
    pass

def long_func(x):
    if x == 5:
        return 5
    elif x == 'Hello':
        return 'Hello Yourself!'
    elif x == 'What is the answer to the ultimate question?':
        return 42
    else:
        raise WTHxeption('I don\'t know what {0} is' .format(x,type(x)))

def main():
    user_inputs = ['Hello',
                   'Waht is teh snsera to QEWRTASDF',
                   'wHAT IS THE ANSWER TO THE ULTIMATE QUESTION?',
                   5,
                   'AAAGREHASDF',
                   None]

    for user_input in user_inputs:
        try:
            print long_func(user_input)
        except WTHxeption as e:
            print e.message
