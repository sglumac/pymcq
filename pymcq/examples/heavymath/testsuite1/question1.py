from pymcq.mcqtypes import create_usual_question, create_usual_part
from pymcq.mcqtex import latex_format

from random import randrange


TITLE = "minus_plus"


def generate_question():

    get_part_list = (__get_part_plus,
                     __get_part_minus)

    return create_usual_question(TITLE, __generate_parameters,
                                 __get_main_text, get_part_list)


def __get_main_text(parameters):
    x, y = map(latex_format, parameters)
    main_text = r'''
    Ako je $x = %s$, a $y = %s$, odredite iznose sljedecih izraza:
    ''' % (x, y)

    return main_text


def __get_part_plus(parameters):

    x, y = parameters

    answer = x + y

    points = 1.0

    text = r"(1 bod) $x + y$"

    return create_usual_part(text, answer, points)


def __get_part_minus(parameters):

    x, y = parameters

    answer = x - y

    points = 1.0

    text = r"(1 bod) $x - y$"

    return create_usual_part(text, answer, points)


def __generate_parameters():
    x = randrange(100) / 100. + randrange(20)
    y = randrange(1000000000) / 100. + randrange(20)

    return x, y
