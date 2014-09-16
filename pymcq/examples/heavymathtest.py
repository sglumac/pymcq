from pymcq import mcqjson
from pymcq import mcqtex
from pymcq.mcqtypes import TestInfo

from pymcq.examples.heavymath import question1
from pymcq.examples.heavymath import question2

QUESTIONS = question1, question2

COURSE = 'Teska matematika'
EXAM = 'Ispitni rok'
DATE = '11.09.2014.'
NOTE = r'''\textit{Za svaki krivo zacrnjen odgovor oduzima se 1/4 bodova
koje je moguce dobiti na zadanom pitanju. Ako su za isto pitanje zacrnjena
dva odgovora, zadatak se smatra nerijesenim i nosi 0 bodova.
}'''


if __name__ == '__main__':

    testinfo = TestInfo(COURSE, EXAM, DATE, NOTE)
    question_generators = [question.generate_question
                           for question in QUESTIONS]

    mcqjson.create_exam('student_list.csv', 'test.json',
                        testinfo, question_generators)
    mcqtex.create_test('test.json', 'test.tex')
    mcqtex.create_matrix('test.json', 'matrix.tex')
