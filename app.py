class Member():
    def __init__(self, full_name=""):
        self.full_name = full_name

    def introduce(self):
        print(f"Hi, my name is {self.full_name}")

bryant = Member('Bryant')
bryant.introduce()