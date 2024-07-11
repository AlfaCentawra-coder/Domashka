grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5], [1, 2, 1, 3, 5]]
new_gardes = []
student = {"Simon", "Alex", "Max", "Britany", "Alan", "Jack"}
new_student = []

def grade_poit(gardes):
    x = 0
    z = 0
    a = 0
    b = 0
    w = 0
    for x in range (len(grades)):
        z = grades[x]
        x = x + 1
        w = 0
        for a in range (len(z)):
            b = z[a]
            a = a + 1
            w = w + b
        new_gardes.append(w / int(len(z)))

def alfabet_student(student):
   return(sorted(student, key = lambda x: x[0]))

grade_poit(grades)
set_ = list(alfabet_student(student))
len_ = 0
for len_ in range (len(grades)):
    new_student.append(str(set_[len_]) + str(new_gardes[len_]))
    len_ = len_ + 1
print(new_student)