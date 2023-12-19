import unittest
from dao.tasks import *


class MyTestCase(unittest.TestCase):
    # THIS TEST CASE WILL CHECK IF TEACHER DATA IS FETCHED OR NOT
    def testTeacherInfo(self):
        data = teacherInfo()
        if data != []:
            self.assertEqual(True, True)
        else:
            self.assertEqual(True, False)

    # THIS TEST CASE WILL CHECK IF STUDENT DATA IS FETCHED OR NOT
    def testStudentInfo(self):
        data = studentInfo()
        if data != []:
            self.assertEqual(True, True)
        else:
            self.assertEqual(True, False)

    # THIS TEST CASE WILL CHECK IF COURSE DATA IS FETCHED OR NOT
    def testCourseInfo(self):
        data = courseInfo()
        if data != []:
            self.assertEqual(True, True)
        else:
            self.assertEqual(True, False)

    # THIS TEST CASE WILL CHECK IF ENROLLMENT DATA IS FETCHED OR NOT
    def testEnrollmentInfo(self):
        data = enrollmentInfo()
        if data != []:
            self.assertEqual(True, True)
        else:
            self.assertEqual(True, False)

    # THIS TEST CASE WILL CHECK IF PAYMENT INFORMATION IS FETCHED OR NOT
    def testPaymentInfo(self):
        data = paymentInfo()
        if data != []:
            self.assertEqual(True, True)
        else:
            self.assertEqual(True, False)
if __name__ == '__main__':
    unittest.main()
