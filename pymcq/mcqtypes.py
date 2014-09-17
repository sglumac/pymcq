from collections import namedtuple
from random import randrange


TestInfo = namedtuple('TestInfo',
                      ('logo', 'institution', 'department', 'course', 'exam', 'date', 'note'))

Question = namedtuple('Question',
                      ('title', 'parameters', 'main_text', 'parts'))

Part = namedtuple('Part',
                  ('text', 'choices', 'correct_idx', 'points'))


def create_usual_part(text, answer, points):

    correct_idx = randrange(5)

    mid = answer / (0.8 + correct_idx * 0.1)

    choices = (0.8 * mid, 0.9 * mid, 1.0 * mid, 1.1 * mid, 1.2 * mid)

    return Part(text, choices, correct_idx, points)



def create_usual_question(title, generate_parameters, get_main_text,
                          get_part_list):

    parameters = generate_parameters()

    parts = tuple(get_part(parameters) for get_part in get_part_list)

    main_text = get_main_text(parameters)

    return Question(title, parameters, main_text, parts)


def read_question(question_list):
    ''' maybe ineffective '''

    tmp_question = Question(*question_list)

    parts = tuple(Part(*part_list) for part_list in tmp_question.parts)

    question  = Question(tmp_question.title, tmp_question.parameters,
                         tmp_question.main_text, parts)

    return question
