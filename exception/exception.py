# THIS EXCEPTION WILL RAISE WHEN ENROLLMENT ALREADY EXISTS
class DuplicateEnrollmentException(Exception):
    def __init__(self,msg="ENROLLMENT ALREADY EXISTS"):
        super().__init__(msg)


# THIS EXCEPTION WILL RAISE WHEN COURSE ALREADY EXISTS
class CourseNotFoundException(Exception):
    def __init__(self,msg="COURSE NOT FOUND"):
        super().__init__(msg)


# THIS EXCEPTION WILL RAISE WHEN STUDENT DO NOT EXIST
class StudentNotFoundException(Exception):
    def __init__(self,msg="STUDENT NOT FOUND"):
        super().__init__(msg)


# THIS EXCEPTION WILL RAISE WHEN TEACHER DO NOT EXIST
class TeacherNotFoundException(Exception):
    def __init__(self,msg="TEACHER NOT FOUND"):
        super().__init__(msg)


# THIS EXCEPTION WILL RAISE WHEN PAYMNET IS INVALID
class PaymentValidationException(Exception):
    def __init__(self,msg="INVALID PAYMENT AMOUNT/DATE"):
        super().__init__(msg)


# THIS EXCEPTION WILL RAISE WHEN STUDENT DATA IS INVALID
class InvalidStudentDataException(Exception):
    def __init__(self,msg="INVALID STUDENT DATA"):
        super().__init__(msg)


# THIS EXCEPTION WILL RAISE WHEN COURSE DATA IS INVALID
class InvalidCourseDataException(Exception):
    def __init__(self,msg="INVALID COURSE DATA"):
        super().__init__(msg)


# THIS EXCEPTION WILL RAISE WHEN ENROLLMENT DATA IS INVALID
class InvalidEnrollmentDataException(Exception):
    def __init__(self,msg="INVALID ENROLLMENT DATA"):
        super().__init__(msg)


# THIS EXCEPTION WILL RAISE WHEN TEACHER DATA IS INVALID
class InvalidTeacherDataException(Exception):
    def __init__(self,msg="INVALID TEACHER DATA"):
        super().__init__(msg)


# THIS EXCEPTION WILL RAISE WHEN STUDENT HAS INSUFFICIENT FUNDS
class InsufficientFundsException(Exception):
    def __init__(self,msg="STUDENT HAS INSUFFICIENT FUNDS"):
        super().__init__(msg)