from pymcq.mcqtypes import read_question, TestInfo


def create_title(test, student):
    '''
    test - json dictionary
    student - json dictionary
    '''

    testinfo = TestInfo(*test['info'])
    course, exam, date, note = testinfo

    test_id = student['test_id']

    name = student['name']
    surname = student['surname']
    student_id = student['student_id']
    
    exam_title = r'''
    \begin{tabular}{l c}
        \begin{minipage}{0.1\textwidth}
            \begin{center}
            \includegraphics[width=\textwidth]{img/logo.jpg}
        \end{center}
        \end{minipage}
        &
        \begin{minipage}{\textwidth}
            \textbf{VISOKA TEHNICKA SKOLA U BJELOVARU}

            \textbf{STUDIJ MEHATRONIKE}

            \Large \textbf{%s - %s, %s}
        \end{minipage}
    \end{tabular}
    \vspace{0.5cm}

    \begin{tabularx}{\textwidth}{X r}
        \large \textbf{Test %s, %s %s, %s}
        &
        \normalsize \textbf{Potpis:} -------------------------------------- \\
    \end{tabularx}
    \vspace{0.2cm}

    %s
    \vspace{0.5cm}

    ''' % (course, exam, date, test_id, name, surname, student_id, note)

    return exam_title


def write_test_questions(writeline, questions):
    writeline(r"\begin{questions}")

    for question in questions:

        writeline(r"\question " + question.main_text)

        writeline(r"\begin{parts}")

        for part in question.parts:
            writeline(r"\part " + part.text)
            writeline('')

            writeline(r"\begin{oneparchoices}")
            for idx, choice in enumerate(part.choices):
                writeline(r"\CorrectChoice " \
                          if idx == part.correct_idx else r"\choice")
                writeline("$" + latex_format(choice) + "$")
            writeline(r"\end{oneparchoices}")

        writeline(r"\end{parts}")

    writeline(r"\end{questions}")


def write_matrix_choices(writeline, questions):
    writeline(r"$\phantom{x}\hspace{42pt}A\hspace{12pt}B\hspace{12pt}C\hspace{12pt}D\hspace{12pt}E$")

    writeline(r"\doublespacing")
    writeline(r"\begin{questions}")

    for question in questions:

        writeline(r"\question")
        writeline(r"\begin{parts}")
        for part in question.parts:
            writeline(r"\part")
            writeline(r"$\phantom{x}\bigcirc\phantom{x}\bigcirc\phantom{x}\bigcirc\phantom{x}\bigcirc\phantom{x}\bigcirc$")
        writeline(r"\end{parts}")
    
    writeline(r"\end{questions}")
    writeline(r"\singlespacing")


def create_tex(test_json, tex_path, write_questions, answers=False):

    with open(test_json, 'rb') as jsonf, open(tex_path, 'wb') as testf:

        writeline = lambda line: testf.write(line + '\n')

        test = json.loads(jsonf.read())

        writeline(r"\documentclass[answers]{exam}"
                  if answers else
                  r"\documentclass{exam}")

        writeline(r'''
        \input{header.tex}

        \begin{document}
        ''')

        for student in test['students']:

            writeline(create_title(test, student))

            questions = map(read_question, student['questions'])
            write_questions(writeline, questions) 

            writeline(r"\clearpage")

        writeline(r"\end{document}")


def create_test(test_json, tex_path):
    create_tex(test_json, tex_path, write_test_questions)


def create_answers(test_json, tex_path):
    create_tex(test_json, tex_path, write_test_questions, answers=True)


def create_matrix(test_json, tex_path):
    create_tex(test_json, tex_path, write_matrix_choices)


def latex_format(x, max_exponent=2, decimal_places=2, sign=False):

    scientific_string = "{0:e}".format(x).split('e')

    mantissa = float(scientific_string[0])
    exponent = int(scientific_string[1])

    if abs(exponent) > max_exponent:
        mantissa = round(mantissa, decimal_places)
        strx = r"%s \times 10^{%s}" % (mantissa, exponent)
    else:
        number = mantissa * 10 ** exponent

        strx = '%s' % round(number, decimal_places - exponent)

    return '+' + strx  if x >= 0 and sign else strx


