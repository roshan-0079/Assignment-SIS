from dao.students import Students
from dao.teachers import Teachers
from dao.courses import Courses
from dao.enrollments import Enrollments
from dao.payments import Payments


# OBJECT CREATION
s = Students()
t = Teachers()
c = Courses()
e = Enrollments()
p = Payments()


# TASK 8 - ADDING A STUDENT JOHN AND ENROLLING HIM IN TWO COURSES
def studentEnrollment():
    s.insert(7, 'John', 'Doe', '1995-08-15', 'johndoe@example.com', '1234567890')
    s.EnrollInCourse(105)
    s.EnrollInCourse(104)


# TASK 9 - ADDING A NEW TEACHER AND ASSIGNING HIM/HER TO A COURSE
def teacherAssignment():
    t.insert(7, 'Sarah', 'Smith', 'sarah.smith@example.com')
    c.AssignTeacher(t, 7, 302)


# TASK 10 - RECORDS THE PAYMENT IN THE DATABASE
def paymentRecord():
    p.GetStudent(101)
    s.GetPaymentHistory(101)


# TASK 11 - ENROLLMENT REPORT GENERATION
def enrollmentReportGeneration():
    data = c.GetEnrollments()
    print(f"THE TOTAL ENROLLMENTS FOR THE {data[0][0]} COURSE ARE {len(data)}")
    print("HERE ARE THE STUDENT ID'S, STUDENT NAMES AND THE DATE OF ENROLLMENT")
    for i in data:
        print(i)


# ADDITIONAL DATA FETCHING METHODS
# THIS METHOD WILL FETCH STUDENT DATA
def studentInfo():
    data = s.select()
    for i in data:
        print(i)
    return data


# THIS METHOD WILL FETCH TEACHER DATA
def teacherInfo():
    data = t.select()
    for i in data:
        print(i)
    return data


# THIS METHOD WILL FETCH COURSE DATA
def courseInfo():
    data = c.select()
    for i in data:
        print(i)
    return data


# THIS METHOD WILL FETCH ENROLLMENT DATA
def enrollmentInfo():
    data = e.select()
    for i in data:
        print(i)
    return data


# THIS METHOD WILL FETCH PAYMENT DATA
def paymentInfo():
    data = p.select()
    for i in data:
        print(i)
    return data