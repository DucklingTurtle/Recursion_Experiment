class Teacher(object):
    def __init__(self, name, day, time):
        self.name = name
        self.day = day
        self.time = time
        self.student1 = None
        self.student2 = None

    def __str__(self):
        if self.student1 is None and self.student2 is None:
            return "----------\n\nName: " + self.name + "\nDays Available: " + str(self.day) + "\nHours Available: " + str(self.time)
        elif self.student1 is not None and self.student2 is None:
            return "----------\n\nName: " + self.name + "\nDays Available: " + self.day + "\nHours Available: " + self.time\
                + "\nStudent 1: " + self.student1.name
        elif self.student1 is not None and self.student2 is not None:
            return "----------\n\nName: " + self.name + "\nDays Available: " + self.day + "\nHours Available: " + self.time\
                + "\nStudent 1: " + self.student1.name + "\nStudent 2: " + self.student2.name
        elif self.student1 is None and self.student2 is not None:
            return "----------\n\nName: " + self.name + "\nDays Available: " + self.day + "\nHours Available: " + self.time\
                + "\nStudent 2: " + self.student2.name