# Ke Shi on Feb 20th, 2022
from operator import itemgetter, attrgetter

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
]
sorted(student_tuples, key=lambda student: student[2])

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]

sorted(student_objects, key=lambda student: student.age)
sorted(student_tuples, key=itemgetter(2))
sorted(student_objects, key=attrgetter('age'))
sorted(student_tuples, key=itemgetter(1,2))
sorted(student_objects, key=attrgetter('grade', 'age'))
sorted(student_tuples, key=itemgetter(2), reverse=True)
sorted(student_objects, key=attrgetter('age'), reverse=True)

"""
In Py3.0, the cmp parameter was removed entirely 
(as part of a larger effort to simplify and unify the language, 
eliminating the conflict between rich comparisons and the __cmp__() magic method).

def numeric_compare(x, y):
    return x - y

sorted([5, 2, 4, 1, 3],cmp=numeric_compare)
"""

