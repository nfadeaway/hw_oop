students = []
lecturers = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students.append(self)

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer,
                      Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.course_grades:
                lecturer.course_grades[course] += [grade]
            else:
                lecturer.course_grades[course] = [grade]
        else:
            return 'Ошибка'

    def _avr_hw_grade(self):
        sum_grades = 0
        count_grades = 0
        for grades in self.grades.values():
            sum_grades += sum(grades)
            count_grades += len(grades)
        return sum_grades / count_grades

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за домашние задания: {round(Student._avr_hw_grade(self), 1)}\n' \
               f'Курсы в процессе изучения: {", ".join(self.courses_in_progress)}\n' \
               f'Завершенные курсы: {", ".join(self.finished_courses)}'

    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Такого студента нет')
            return
        return self._avr_hw_grade() < other._avr_hw_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            print('Такого студента нет')
            return
        return self._avr_hw_grade() == other._avr_hw_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            print('Такого студента нет')
            return
        return self._avr_hw_grade() <= other._avr_hw_grade()

    def __ge__(self, other):
        if not isinstance(other, Student):
            print('Такого студента нет')
            return
        return self._avr_hw_grade() >= other._avr_hw_grade()


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.course_grades = {}
        lecturers.append(self)

    def _avr_lecture_grade(self):
        sum_grades = 0
        count_grades = 0
        for grades in self.course_grades.values():
            sum_grades += sum(grades)
            count_grades += len(grades)
        return sum_grades / count_grades

    def __str__(self):
        return f'Имя: {self.name}\n' \
               f'Фамилия: {self.surname}\n' \
               f'Средняя оценка за лекции: {round(Lecturer._avr_lecture_grade(self), 1)}'

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Такого лектора нет')
            return
        return self._avr_lecture_grade() < other._avr_lecture_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            print('Такого лектора нет')
            return
        return self._avr_lecture_grade() == other._avr_lecture_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            print('Такого лектора нет')
            return
        return self._avr_lecture_grade() <= other._avr_lecture_grade()

    def __ge__(self, other):
        if not isinstance(other, Lecturer):
            print('Такого лектора нет')
            return
        return self._avr_lecture_grade() >= other._avr_lecture_grade()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}'


def avr_course_hw_grade(students, course):
    sum_grades = 0
    count_grades = 0
    for i in range(len(students)):
        sum_grades += sum(students[i].grades[course])
        count_grades += len(students[i].grades[course])
        print(f'Среднее арифметическое по ДЗ за курс {course} у студента {students[i].name} {students[i].surname}'
              f' = {round(sum(students[i].grades[course]) / len(students[i].grades[course]), 1)}')
    print(f'Среднее арифметическое по ДЗ за курс {course} по всем студентам = {round(sum_grades / count_grades, 1)}')
    return


def avr_course_lecturers_grade(lecturers, course):
    sum_grades = 0
    count_grades = 0
    for i in range(len(lecturers)):
        sum_grades += sum(lecturers[i].course_grades[course])
        count_grades += len(lecturers[i].course_grades[course])
        print(f'Среднее арифметическое по курсу {course} у лектора {lecturers[i].name} {lecturers[i].surname}'
              f' = {round(sum(lecturers[i].course_grades[course]) / len(lecturers[i].course_grades[course]), 1)}')
    print(f'Среднее арифметическое по курсу {course} по всем лекторам = {round(sum_grades / count_grades, 1)}')
    return


# добавляем студентов
ivanov = Student('Иван', 'Иванов', 'м')
ivanov.courses_in_progress += ['Python', 'GIT', 'HTML']
ivanov.finished_courses += ['Вводный курс', 'Английский язык']

petrov = Student('Петр', 'Петров', 'м')
petrov.courses_in_progress += ['GIT', 'HTML']
petrov.finished_courses += ['Вводный курс']

# добавляем лекторов
zhukov = Lecturer('Жуков', 'Александр')
zhukov.courses_attached += ['Python', 'GIT']

malikov = Lecturer('Маликов', 'Антон')
malikov.courses_attached += ['HTML', 'GIT']

# добавляем ревьюера и курсы, которые проверяет
cepko = Reviewer('Цепко', 'Татьяна')
cepko.courses_attached += ['Python', 'GIT', 'HTML']

# # ревьюер выставляет оценку за дз
cepko.rate_hw(ivanov, 'Python', 5)
cepko.rate_hw(ivanov, 'Python', 7)
cepko.rate_hw(ivanov, 'GIT', 5)
cepko.rate_hw(ivanov, 'GIT', 8)
cepko.rate_hw(ivanov, 'HTML', 10)
cepko.rate_hw(ivanov, 'HTML', 4)
cepko.rate_hw(petrov, 'GIT', 9)
cepko.rate_hw(petrov, 'GIT', 7)

# студенты оценивают лекторов
ivanov.rate_lecturer(zhukov, 'Python', 10)
ivanov.rate_lecturer(zhukov, 'GIT', 7)
ivanov.rate_lecturer(zhukov, 'GIT', 6)
petrov.rate_lecturer(zhukov, 'GIT', 5)
petrov.rate_lecturer(malikov, 'HTML', 10)
petrov.rate_lecturer(malikov, 'HTML', 10)
petrov.rate_lecturer(malikov, 'HTML', 10)
petrov.rate_lecturer(malikov, 'GIT', 7)
petrov.rate_lecturer(malikov, 'GIT', 3)
petrov.rate_lecturer(malikov, 'GIT', 10)


print(' Студенты '.center(50, '*'))

print(ivanov)
print()
print(petrov)
print()

print(' Лекторы '.center(50, '*'))

print(zhukov)
print()
print(malikov)
print()

print(' Ревьюер '.center(50, '*'))

print(cepko)
print()

print(' Операторы сравнения '.center(50, '*'))
print()
print('Проверка логики сравнения: средняя оценка за ДЗ студента Иванова больше Петрова? -', ivanov > petrov)
print()
print('Проверка логики сравнения: средняя оценка за лекции лектора Жукова больше Маликова? -', zhukov > malikov)
print()

avr_course_hw_grade(students, 'GIT')
print()
avr_course_lecturers_grade(lecturers, 'GIT')
