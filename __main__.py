import teacher, student, random, pprint
import numpy
import numpy as np

# list of teacher and student objects
t_list = []
s_list = []

# # global index for solve method
# index_s = 0

# Making a first and second teachers list and making sure the random choice never repeats, if it doesnt, add it to the list
# first teachers column
first_teachers_column = []
second_teachers_column = []

# list of available teachers pool
teacher_pool = []

# list of numbers & names for random generator
binary = range(2)
names_list = ["Alpha", "Bravo", "Charlie", "Delta", "Echo", "Foxtrot", "Golf", "Hotel", "India", "Juliet", "Kilo",
              "Lima", "Mike", "November", "Oscar", "Papa", "Quebec", "Romeo", "Sierra", "Tango", "Uniform", "Victor",
              "Whiskey", "X-ray", "Yankee", "Zulu"]

# matrix of students with teachers
matrix = [
    [None, None, None]
]


# generates random students and teachers
def generate_data():
    # creates 30 teachers
    for x in range(31):
        # teacher
        # generates random name, day, and times for teachers
        name_t = random.choice(names_list)
        day_t = random.choices(binary, weights=[2,3], k=5)
        time_t = random.choices(binary, weights=[2,3], k=3)
        # adds a teacher to the teachers list
        teacher_obj = teacher.Teacher(name_t, day_t, time_t)
        t_list.append(teacher_obj)

    # creates 10 students
    for y in range(10):
        # student
        # generates random name
        name_s = random.choice(names_list)
        # adds a student to the students list
        s_list.append(student.Student(name_s))


def add_students():
    # making both matrix and s_list accessible by being global
    global matrix
    global s_list
    # range of students - 1 for adding rows into matrix because there is already a starting row
    num_of_students = range(1, len(s_list))

    print("Number of Students")
    print(num_of_students)
    # index of number of students, starting at one, adds a row of Nones to the matrix using vstack
    for x in num_of_students:
        print(x)
        row = [None, None, None]
        matrix = numpy.vstack((matrix, row))

    matrix_printed = numpy.array(matrix)
    print(matrix_printed)
    # index of number of students, starting at 0, adds student to matrix
    for z in range(len(s_list)):
        index = z
        s = s_list[index]
        matrix[index][0] = s
    # print matrix
    print("Add Students")
    print(np.matrix(matrix))


def add_teachers():
    # making both matrix and t_list accessible by being global
    global matrix
    global t_list
    global first_teachers_column
    index = range(len(t_list) - 1)
    # Making a first teachers list and making sure the random choice never repeats, if it doesnt, add it to the list
    while True:
        teacher1 = random.choice(t_list)
        # checks if teacher selected is not already in the list and
        # if length of teachers list is less than length of student list
        if teacher1 not in first_teachers_column and len(first_teachers_column) < len(s_list):
            first_teachers_column.append(teacher1)
            # if length of teachers list is equal to length of student list, then end while loop
            if len(first_teachers_column) == len(s_list):
                break
        else:
            continue
    # use len of student list as index for matrix and how many random teachers
    for index in range(len(first_teachers_column)):
        t = first_teachers_column[index]
        matrix[index][1] = t
    # print matrix
    print("add_teachers")
    print(np.matrix(matrix))


def possible(y,x,n):
    # n is teacher object
    global matrix
    # left, middle, and right column for the row we are checking
    left = None
    middle = None
    right = None
    # how many days match
    days_matched = 0
    if matrix[y][x] is None:
        # getting the objects for the row we are checking
        if x == 0:
            left = n
            middle = matrix[y][1]
            right = matrix[y][2]
        elif x == 1:
            left = matrix[y][0]
            middle = n
            right = matrix[y][2]
        elif x == 2:
            left = matrix[y][0]
            middle = matrix[y][1]
            right = n
        for index in range(5):
            # print(middle.day)
            # print(right.day)
            if 1 == middle.day[index] and 1 == right.day[index]:
                days_matched += 1
        if days_matched > 0:
            print("days_matched")
            print("works")
            return True
            # matrix[y][x] = n


def make_teacher_pool():
    global teacher_pool
    global matrix
    for t in t_list:
        if t not in matrix:
            teacher_pool.append(t)
            print("Adding teacher")
        else:
            print("Teacher already in matrix")


def refresh_teacher_pool():
    global teacher_pool
    global matrix
    # reset teacher pool
    teacher_pool = []
    for t in t_list:
        if t not in matrix:
            teacher_pool.append(t)
    print("refresh_teacher_pool")
    print(teacher_pool)


def turn_matrix_into_names():
    global matrix
    # using function instead of Lambda
    def function(a):
        try:
            return str(a.name)
        except:
            return None
    # using list comprehension, I used map to apply .name to every object in the matrix and make it readable
    matrix_names = [list(map(function, x)) for x in matrix]
    print(list(matrix_names))
    print("turn matrix into names")

# # finds index of empty element in third row
# def empty_third_row():
#     global matrix
#     for y in range(len(s_list)):
#         x = 2
#         if matrix[y][x] is None:
#             return y

def solve():
    # using backtracking/recursion
    global matrix
    global teacher_pool
    global s_list
    global second_teachers_column
    global t_list
    # teacher1 = random.choice(teacher_pool)
    # print(teacher_pool)
    # parsing through matrix
    for y in range(len(s_list)):
        print(y)
        x = 2
        if matrix[y][x] is None:
            for teacher1 in t_list:
                # checks if teacher selected is not already in the list and
                # if length of teachers list is less than length of student list
                if teacher1 not in second_teachers_column and len(second_teachers_column) < len(s_list)\
                        and possible(y, x, teacher1) is True and teacher1 not in matrix:
                    print("Inside If Statement")
                    print(y)
                    # print(second_teachers_column[y])
                    # second_teachers_column.append(teacher1)
                    matrix[y][x] = teacher1
                    second_teachers_column.append(teacher1)
                    # refresh_teacher_pool()
                    print("second teachers column")
                    print(second_teachers_column)
                    turn_matrix_into_names()
                    solve()
                    print("error recursing")
                    print(x)
                    print(y)
                    turn_matrix_into_names()
                    matrix[y][x] = None
                    # second_teachers_column.pop()
            return
        print("Exit")
    # y2 = 0
    # x2 = 2
    # for t in second_teachers_column:
    #     matrix[y2][x2] = t
    #     y2 += 1


def sort():
    global matrix
    add_students()
    add_teachers()
    make_teacher_pool()
    solve()
    turn_matrix_into_names()
    print(np.matrix(matrix))


def verify(y,x):
    # n is teacher object
    global matrix
    # left, middle, and right column for the row we are checking
    left = None
    middle = None
    right = None
    n = matrix[y][x]
    # how many days match
    days_matched = 0
    if matrix[y][x]:
        # getting the objects for the row we are checking
        if x == 0:
            left = n
            middle = matrix[y][1]
            right = matrix[y][2]
        elif x == 1:
            left = matrix[y][0]
            middle = n
            right = matrix[y][2]
        elif x == 2:
            left = matrix[y][0]
            middle = matrix[y][1]
            right = n
        for index in range(5):
            if 1 == middle.day[index] and 1 == right.day[index]:
                days_matched += 1
        if days_matched > 0:
            return True


def verify2():
    global s_list
    objects_verified = 0
    for y in range(len(s_list)):
        for x in range(3):
            if verify(y, x) is True:
                objects_verified += 1
    if objects_verified == len(matrix):
        return True
    else:
        return objects_verified

generate_data()
sort()
print("Test")
print(verify2())

# def solve():
#     global matrix
#     global t_list
#     global teacher_pool
#     global s_list
#     global second_teachers_column
#     index = 0
#     while True:
#         teacher1 = random.choice(teacher_pool)
#         print(teacher_pool)
#         # checks if teacher selected is not already in the list and
#         # if length of teachers list is less than length of student list
#         if teacher1 not in second_teachers_column and len(second_teachers_column) < len(s_list)\
#                 and possible(index, 2, teacher1) is True:
#             second_teachers_column.append(teacher1)
#             refresh_teacher_pool()
#             index += 1
#             # if length of teachers list is equal to length of student list, then end while loop
#             if len(second_teachers_column) == len(s_list):
#                 break
#             else:
#                 continue
#         else:
#             continue
#     x = 2
#     y = 0
#     for t in second_teachers_column:
#         matrix[y][x] = t
#         y += 1