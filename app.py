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
        self.reason = reason

michael = Student("Michael", "I need to learn!")
michael.introduce()

class Instructor(Member):
    def __init__(self, full_name="", bio="", skills=[]):
        Member.__init__(self, full_name)
        self.bio = bio
        self.skills = skills

    def add_skill(self, skill):
        self.skills.append(skill)
        print(f"{self.full_name} learned a new skill. He now knows {self.skills}")

peter = Instructor("Peter", "I teach d3", ['d3', 'topomaps'])
peter.introduce()
peter.add_skill('svg')