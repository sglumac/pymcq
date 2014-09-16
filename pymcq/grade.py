import sys
import json
import csv
from itertools import chain, izip, count
from operator import itemgetter

from mcqtypes import read_question


def grade_question(marked_idxs, correct_idx, points):
    if len(marked_idxs) == 1:
        marked_idx = marked_idxs[0]
        return points if marked_idx == correct_idx else -0.25 * points
    else:
        return 0


def get_marked_marked_idxs(marks):
    return [idx for idx, mark in enumerate(marks) if mark]


def main():
    json_path = sys.argv[1]
    csv_path = sys.argv[2]

    with open(json_path, 'rb') as json_file, open(csv_path, 'rb') as csv_file:
        test = json.loads(json_file.read())

        studenti = test['students']

        csv_reader = csv.reader(csv_file)

# ORDER MATTERS !!!!!!!!!!!!
        for broj, row, student in izip(count(), csv_reader, studenti):
            marked = map(int, row[4:])

# group by 5 questions
            shallow_iters = [iter(marked)] * 5
            answers = zip(*shallow_iters)

            marked_idxs = map(get_marked_marked_idxs, answers)

            correct_idxs, points = \
                zip(*[(part.correct_idx, part.points) for question
                      in map(read_question, student['questions'])
                      for part in question.parts])

            maximum = sum(points)

            total = sum(map(grade, zip(marked_idxs, correct_idxs, points))

            print "%s, %s / %s" % (student['surname'], total, moguce)

if __name__ == '__main__':
    main()

