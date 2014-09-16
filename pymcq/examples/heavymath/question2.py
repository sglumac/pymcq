from pymcq.mcqtypes import create_usual_question, create_usual_part
from pymcq.mcqtex import latex_format

from random import randrange


TITLE = "voce"


def generate_question():

    get_part_list = (__get_part_masa_jabuka,
                     __get_part_jabuka_postotak)

    return create_usual_question(TITLE, __generate_parameters,
                                 __get_main_text, get_part_list)


def __get_main_text(parameters):

    broj_jabuka, broj_krusaka = parameters[:2]
    masa_jabuke, masa_kruske = map(latex_format, parameters[2:])

    main_text = r'''
    U kosari ima tocno %s jabuka i %s krusaka. Ako je masa jedne jabuke
    $%s\;\mathrm{kg}$, a masa jedne kruske $%s\;\mathrm{kg}$ odredite:
    ''' % (broj_jabuka, broj_krusaka, masa_jabuke, masa_kruske)

    return main_text


def __calculate_masa_jabuka(parameters):
    broj_jabuka, _, masa_jabuke, _ = parameters
    return broj_jabuka * masa_jabuke


def __get_part_masa_jabuka(parameters):

    answer = __calculate_masa_jabuka(parameters)

    points = 1.0

    text = r'''(1 bod)
    ukupnu masu jabuka u kosari u kilogramima:'''

    return create_usual_part(text, answer, points)


def __calculate_postotak_jabuka(parameters):

    _, broj_krusaka, _, masa_kruske = parameters

    masa_jabuka = __calculate_masa_jabuka(parameters)

    masa_krusaka = broj_krusaka * masa_kruske

    return 100. * masa_jabuka / (masa_jabuka + masa_krusaka)


def __get_part_jabuka_postotak(parameters):

    answer = __calculate_postotak_jabuka(parameters)

    points = 1.0

    text = r"(1 bod) postotak $\%$ ukupne mase voca koju cine jabuke:"

    return create_usual_part(text, answer, points)


def __generate_parameters():
    broj_jabuka = randrange(5, 21)
    broj_krusaka = randrange(5, 21)

    masa_jabuke = randrange(10, 50) / 100.
    masa_kruske = randrange(10, 50) / 100.

    return broj_jabuka, broj_krusaka, masa_jabuke, masa_kruske
