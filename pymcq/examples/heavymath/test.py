from pymcq import mcqjson
from pymcq import mcqtex
from pymcq.mcqtypes import TestInfo

from pymcq.examples.heavymath.testsuite1 import question1, question2

QUESTIONS = question1, question2

LOGO = 'logo.jpg'
INSTITUTION = 'Visoka tehnicka skola u Bjelovaru'
DEPARTMENT = 'Studij mehatronike'
COURSE = 'Teska matematika'
EXAM = 'Ispitni rok'
DATE = '11.09.2014.'
NOTE = r'''\textit{Za svaki krivo zacrnjen odgovor oduzima se 1/4 bodova
koje je moguce dobiti na zadanom pitanju. Ako su za isto pitanje zacrnjena
dva odgovora, zadatak se smatra nerijesenim i nosi 0 bodova.
}'''


if __name__ == '__main__':

    testinfo = TestInfo(LOGO, INSTITUTION, DEPARTMENT, COURSE, EXAM, DATE, NOTE)
    question_generators = [question.generate_question
                           for question in QUESTIONS]

    mcqjson.create_exam('student_list.csv', 'test.json',
                        testinfo, question_generators)
    mcqtex.create_test('header.tex', 'test.json', 'test.tex')
    mcqtex.create_answers('header.tex', 'test.json', 'answers.tex')
    mcqtex.create_matrix('header.tex', 'test.json', 'matrix.tex')
