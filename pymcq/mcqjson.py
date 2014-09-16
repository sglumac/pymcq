import csv
import json
from functools import partial


def generate_student_questions(question_generators, student_data, test_id):

    name, surname, student_id = student_data

    student = {'name': name, 'surname': surname,
               'student_id': student_id, 'test_id': test_id}

    student['questions'] = [generate_question()
                            for generate_question in question_generators]

    return student


def create_exam(student_list, test_path, testinfo, question_generators):

    test = dict()

    with open(student_list, 'rb') as csvf:

        reader = csv.reader(csvf)

        test['info'] = testinfo

        generate_questions = partial(generate_student_questions,
                                     question_generators)

        test['students'] = [generate_questions(student_data, test_id)
                            for test_id, student_data in enumerate(reader)]

    with open(test_path, 'wb') as testf:
        testf.write(json.dumps(test))
