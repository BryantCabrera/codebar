class Member():
    def __init__(self, full_name=""):
        self.full_name = full_name

    def introduce(self):
        print(f"Hi, my name is {self.full_name}")

    def __str__(self):
        return ', '.join(['{key}={value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])

bryant = Member('Bryant')
bryant.introduce()

class Student(Member):
    def __init__(self, full_name="", reason=""):
        Member.__init__(self, full_name)
        self.account = 'student'
        self.reason = reason

michael = Student("Michael", "I need to learn!")
michael.introduce()

class Instructor(Member):
    def __init__(self, full_name="", bio="", skills=[]):
        Member.__init__(self, full_name)
        self.account = 'instructor'
        self.bio = bio
        self.skills = skills

    def add_skill(self, skill):
        self.skills.append(skill)
        print(f"{self.full_name} learned a new skill. He now knows {self.skills}")

peter = Instructor("Peter", "I teach d3", ['d3', 'topomaps'])
peter.introduce()
peter.add_skill('svg')

class Workshop():
    def __init__(self, date="", subject="", instructors=[], students=[]):
        self.date = date
        self.subject = subject
        self.instructors = instructors
        self.students = students

    def add_participant(self, person):
        if person.account == 'student':
            self.students.append(person)
        elif person.account == 'instructor':
            self.instructors.append(person)

    def print_details(self):
        print(f"Workshop - {self.date} - {self.subject}\nStudents")
        for index, student in enumerate(self.students):
            print(f"{index + 1}. {student.full_name}")
        print('\n Instructors')
        for index, instructor in enumerate(self.instructors):
            print(f"{index + 1}. {instructor.full_name}")

workshop = Workshop("12/03/2014", "Shutl")

jane = Student("Jane Doe", "I am trying to learn programming and need some help")
lena = Student("Lena Smith", "I am really excited about learning to program!")
vicky = Instructor("Vicky Python", "I want to help people learn coding.")
vicky.add_skill("HTML")
vicky.add_skill("JavaScript")
nicole = Instructor("Nicole McMillan", "I have been programming for 5 years in Python and want to spread the love")
nicole.add_skill("Python")

workshop.add_participant(jane)
workshop.add_participant(lena)
workshop.add_participant(vicky)
workshop.add_participant(nicole)
workshop.print_details()