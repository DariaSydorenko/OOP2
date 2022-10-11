import pprint


class Student:
    def __init__(self, name, surname, book_number, grades):
        self.name = name
        self.surname = surname
        self.book_number = book_number
        self.grades = grades
        self.average = self.get_average()

    def get_average(self):
        return sum(self.grades)/len(self.grades)

    def __repr__(self):
        return f'{self.name} {self.surname} №{self.book_number}: {self.grades} - {self.average}'


class Group:
    def __init__(self, students):
        if len(students) < 5 or len(students) > 20:
            raise ValueError('Неправильна кількість студентів')
        self.students = students

    def print_five_best(self):
        return list(sorted(self.students, key=lambda x: x.average, reverse=True))


student = [Student('A', 'a', '1', [1, 2, 3, 4, 3]),
           Student('B', 'b', '2', [2, 2, 5, 4, 2]),
           Student('C', 'c', '3', [1, 3, 3, 3, 3]),
           Student('D', 'd', '4', [5, 3, 2, 4, 3]),
           Student('E', 'e', '5', [5, 5, 1, 2, 4]),
           Student('F', 'f', '6', [4, 1, 3, 4, 3]),
           Student('G', 'g', '7', [1, 1, 1, 2, 5]),
           Student('H', 'h', '8', [4, 2, 2, 4, 3])]
group = Group(student)
pprint.pprint(group.print_five_best()[:5])
