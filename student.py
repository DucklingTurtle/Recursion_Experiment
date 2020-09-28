class Student:
    def __init__(self, name):
        self.name = name
        self.teacher1 = None
        self.teacher2 = None
        self.day = None
        self.time = None

    def __str__(self):
        if self.name and self.teacher1 is None and self.teacher2 is None and self.day is None and self.time is None:
            return "----------\n\nName: " + self.name
        else:
            print("Remember to code in the rest of the variables printing")